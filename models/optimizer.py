from typing import List, Dict, Set, Tuple
import numpy as np
from pulp import *
from .sensor import Sensor

class SensorOptimizer:
    """Classe qui implémente les algorithmes d'optimisation pour les capteurs."""
    
    def __init__(self, sensors: List[Sensor], num_zones: int):
        self.sensors = sensors
        self.num_zones = num_zones
        self.solution = None
        self.objective_value = 0
    
    def solve_linear_programming(self) -> Dict[int, List[int]]:
        """
        Résout le problème en utilisant la programmation linéaire.
        Retourne un dictionnaire avec les temps d'activation pour chaque capteur.
        """
        # Créer le problème d'optimisation
        prob = LpProblem("Sensor_Optimization", LpMaximize)
        
        # Variables de décision: x[i,t] = 1 si le capteur i est actif au temps t
        x = {}
        for i, sensor in enumerate(self.sensors):
            for t in range(int(sensor.battery_duration)):
                x[i,t] = LpVariable(f"x_{i}_{t}", cat='Binary')
        
        # Fonction objectif: maximiser la durée totale
        prob += lpSum(x[i,t] for i in range(len(self.sensors)) 
                     for t in range(int(self.sensors[i].battery_duration)))
        
        # Contraintes de couverture des zones
        max_time = int(max(s.battery_duration for s in self.sensors))
        for zone in range(self.num_zones):
            for t in range(max_time):
                prob += lpSum(
                    x[i, t]
                    for i, sensor in enumerate(self.sensors)
                    if zone in sensor.coverage_zones and t < int(sensor.battery_duration)
                ) >= 1
        
        # Contraintes de batterie
        for i, sensor in enumerate(self.sensors):
            prob += lpSum(x[i,t] for t in range(int(sensor.battery_duration))) <= sensor.battery_duration
        
        # Résoudre le problème
        prob.solve(PULP_CBC_CMD(msg=False))
        
        # Traiter la solution
        solution = {}
        for i, sensor in enumerate(self.sensors):
            solution[i] = [t for t in range(int(sensor.battery_duration)) 
                         if value(x[i,t]) == 1]
        
        self.solution = solution
        self.objective_value = value(prob.objective)
        return solution
    
    def solve_simulated_annealing(self, initial_temp: float = 100.0, 
                                cooling_rate: float = 0.95,
                                iterations: int = 1000) -> Dict[int, List[int]]:
        """
        Implémente l'algorithme de recuit simulé.
        """
        current_solution = self._generate_initial_solution()
        best_solution = current_solution.copy()
        best_value = self._evaluate_solution(best_solution)
        temperature = initial_temp
        
        for _ in range(iterations):
            new_solution = self._get_neighbor_solution(current_solution)
            new_value = self._evaluate_solution(new_solution)
            
            # Critère d'acceptation
            if new_value > best_value or \
               np.random.random() < np.exp((new_value - best_value) / temperature):
                current_solution = new_solution
                if new_value > best_value:
                    best_solution = new_solution.copy()
                    best_value = new_value
            
            temperature *= cooling_rate
        
        self.solution = best_solution
        self.objective_value = best_value
        return best_solution
    
    def _generate_initial_solution(self) -> Dict[int, List[int]]:
        """Génère une solution initiale valide."""
        solution = {}
        for i, sensor in enumerate(self.sensors):
            solution[i] = list(range(int(sensor.battery_duration)))
        return solution
    
    def _get_neighbor_solution(self, current_solution: Dict[int, List[int]]) -> Dict[int, List[int]]:
        """Génère une solution voisine en modifiant aléatoirement la solution actuelle."""
        new_solution = current_solution.copy()
        sensor_id = np.random.randint(0, len(self.sensors))
        
        # Modifier aléatoirement les temps d'activation
        if len(new_solution[sensor_id]) > 0:
            new_solution[sensor_id] = sorted(np.random.choice(
                range(int(self.sensors[sensor_id].battery_duration)),
                size=np.random.randint(0, len(new_solution[sensor_id]) + 1),
                replace=False
            ))
        
        return new_solution
    
    def _evaluate_solution(self, solution: Dict[int, List[int]]) -> float:
        """Évalue la qualité d'une solution."""
        total_duration = sum(len(times) for times in solution.values())
        
        # Pénalité pour les zones non couvertes
        coverage_penalty = 0
        for zone in range(self.num_zones):
            zone_covered = False
            for sensor_id, times in solution.items():
                if zone in self.sensors[sensor_id].coverage_zones and len(times) > 0:
                    zone_covered = True
                    break
            if not zone_covered:
                coverage_penalty += 1000
        
        return total_duration - coverage_penalty
    
    def get_solution_summary(self) -> str:
        """Retourne un résumé de la solution trouvée."""
        if not self.solution:
            return "Aucune solution trouvée."
        
        summary = f"Valeur de l'objectif: {self.objective_value}\n"
        summary += "Activation des capteurs:\n"
        
        for sensor_id, times in self.solution.items():
            sensor = self.sensors[sensor_id]
            summary += f"Capteur {sensor_id}: actif aux temps {times}\n"
        
        return summary 
from models.sensor import Sensor
from models.optimizer import SensorOptimizer

def create_example_sensors():
    """Crée des capteurs d'exemple pour les tests."""
    sensors = [
        Sensor(id=0, battery_duration=5.0, coverage_zones={0, 1, 2}),
        Sensor(id=1, battery_duration=4.0, coverage_zones={1, 2, 3}),
        Sensor(id=2, battery_duration=6.0, coverage_zones={0, 3, 4}),
        Sensor(id=3, battery_duration=3.0, coverage_zones={2, 4}),
    ]
    return sensors

def main():
    # Créer des capteurs d'exemple
    sensors = create_example_sensors()
    num_zones = 5  # Nombre total de zones à couvrir
    
    # Créer l'optimiseur
    optimizer = SensorOptimizer(sensors, num_zones)
    
    # Résoudre avec la programmation linéaire
    print("Résolution avec la programmation linéaire...")
    lp_solution = optimizer.solve_linear_programming()
    print(optimizer.get_solution_summary())
    
    # Résoudre avec le recuit simulé
    print("\nRésolution avec le recuit simulé...")
    sa_solution = optimizer.solve_simulated_annealing()
    print(optimizer.get_solution_summary())

if __name__ == "__main__":
    main() 
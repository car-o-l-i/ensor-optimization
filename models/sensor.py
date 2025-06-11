from dataclasses import dataclass
from typing import List, Set

@dataclass
class Sensor:
    """Classe qui représente un capteur de surveillance."""
    id: int
    battery_duration: float  # Durée de la batterie en unités de temps
    coverage_zones: Set[int]  # Ensemble des identifiants des zones couvertes
    is_active: bool = False
    
    def can_cover_zone(self, zone_id: int) -> bool:
        """Vérifie si le capteur peut couvrir une zone spécifique."""
        return zone_id in self.coverage_zones
    
    def get_coverage_count(self) -> int:
        """Retourne le nombre de zones qui peuvent être couvertes."""
        return len(self.coverage_zones)
    
    def activate(self) -> None:
        """Active le capteur."""
        self.is_active = True
    
    def deactivate(self) -> None:
        """Désactive le capteur."""
        self.is_active = False
    
    def __str__(self) -> str:
        return f"Sensor {self.id} (Battery: {self.battery_duration}, Zones: {self.coverage_zones})" 
"""
Exemple de données pour le projet d'optimisation des capteurs.
"""

def get_example_sensors():
    """
    Retourne un exemple de configuration de capteurs.
    """
    return [
        {
            "id": 0,
            "battery_duration": 5.0,
            "coverage_zones": {0, 1, 2},
            "description": "Capteur 1: zones 1, 2, 3"
        },
        {
            "id": 1,
            "battery_duration": 4.0,
            "coverage_zones": {1, 2, 3},
            "description": "Capteur 2: zones 2, 3, 4"
        },
        {
            "id": 2,
            "battery_duration": 6.0,
            "coverage_zones": {0, 3, 4},
            "description": "Capteur 3: zones 1, 4, 5"
        },
        {
            "id": 3,
            "battery_duration": 3.0,
            "coverage_zones": {2, 4},
            "description": "Capteur 4: zones 3, 5"
        }
    ]

def get_example_zones():
    """
    Retourne un exemple de configuration des zones.
    """
    return [
        {
            "id": 0,
            "name": "Zone 1",
            "covered_by": [0, 2]  # Couverte par les capteurs 1 et 3
        },
        {
            "id": 1,
            "name": "Zone 2",
            "covered_by": [0, 1]  # Couverte par les capteurs 1 et 2
        },
        {
            "id": 2,
            "name": "Zone 3",
            "covered_by": [0, 1, 3]  # Couverte par les capteurs 1, 2 et 4
        },
        {
            "id": 3,
            "name": "Zone 4",
            "covered_by": [1, 2]  # Couverte par les capteurs 2 et 3
        },
        {
            "id": 4,
            "name": "Zone 5",
            "covered_by": [2, 3]  # Couverte par les capteurs 3 et 4
        }
    ] 
# Optimisation des Capteurs de Surveillance 🎯

## Description Simple
Ce projet aide à optimiser l'activation des capteurs de surveillance. Il utilise deux méthodes:
- Programmation Linéaire (PL)
- Recuit Simulé (RS)

## Comment Utiliser le Projet 🚀

### 1. Installation
```bash
# Cloner le projet
git clone https://github.com/car-o-l-i/ensor-optimization.git

# Aller dans le dossier
cd ensor-optimization

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Exécution
```bash
# Lancer le programme
python main.py
```

## Résultats 📊

### Exemple de Données
```
N = 4 capteurs
M = 5 zones

s1: zones 1, 2, 3 — batterie = 5
s2: zones 2, 3, 4 — batterie = 4
s3: zones 1, 4, 5 — batterie = 6
s4: zones 3, 5 — batterie = 3
```

### Graphiques
Le programme crée deux graphiques:
1. `sensor_activation.png`: Montre quand chaque capteur est actif
2. `method_comparison.png`: Compare les résultats de PL et RS

## Structure du Projet 📁
```
ensor-optimization/
├── main.py              # Programme principal
├── models/
│   ├── sensor.py       # Classe pour les capteurs
│   └── optimizer.py    # Algorithmes d'optimisation
├── visualization.py    # Création des graphiques
└── requirements.txt    # Dépendances
```

## Dépendances 📦
- Python 3.8+
- PuLP (pour la PL)
- NumPy
- Matplotlib
- Pandas

## Exemple de Code 💻

### Création d'un Capteur
```python
sensor = Sensor(
    id=0,
    battery_duration=5.0,
    coverage_zones={0, 1, 2}
)
```

### Résolution du Problème
```python
optimizer = SensorOptimizer(sensors, num_zones)
solution = optimizer.solve_linear_programming()
```

## Résultats Obtenus 📈
- Valeur optimale: 18.0
- Temps d'activation des capteurs:
  - Capteur 0: [0, 1, 2, 3, 4]
  - Capteur 1: [0, 1, 2, 3]
  - Capteur 2: [0, 1, 2, 3, 4, 5]
  - Capteur 3: [0, 1, 2]

## Auteur 👩‍💻
- Carol

## Licence 📄
Ce projet est sous licence MIT. 
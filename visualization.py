import matplotlib.pyplot as plt
import numpy as np

# Definir colores girly
PINK_COLORS = ['#FFB6C1', '#FFC0CB', '#FF69B4', '#FF1493']  # Tonos de rosa
PURPLE_COLORS = ['#E6E6FA', '#D8BFD8', '#DDA0DD', '#EE82EE']  # Tonos de púrpura

def plot_sensor_activation(sensor_times):
    """
    Crée un graphique montrant l'activation des capteurs dans le temps.
    Style girly avec des couleurs roses et violettes.
    """
    # Crear la figura con fondo rosa claro
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#FFF0F5')  # Fondo rosa muy claro
    
    # Colores alternados entre rosa y púrpura
    colors = PINK_COLORS + PURPLE_COLORS
    
    # Dibujar las líneas de activación para cada sensor
    for i, (sensor_id, times) in enumerate(sensor_times.items()):
        ax.plot(times, [i] * len(times), 'o-', 
                color=colors[i], 
                label=f'Capteur {sensor_id}',
                linewidth=3,
                markersize=10,
                markerfacecolor='white',
                markeredgecolor=colors[i],
                markeredgewidth=2)
    
    # Configurar los ejes
    ax.set_yticks(range(len(sensor_times)))
    ax.set_yticklabels([f'Capteur {i}' for i in range(len(sensor_times))])
    ax.set_xlabel('Temps', fontsize=12, color='#FF69B4')
    ax.set_title('Activation des Capteurs dans le Temps', 
                 fontsize=14, color='#FF1493', pad=20)
    
    # Personalizar la cuadrícula
    ax.grid(True, linestyle='--', alpha=0.3, color='#FFB6C1')
    
    # Personalizar los ejes
    ax.spines['bottom'].set_color('#FF69B4')
    ax.spines['top'].set_color('#FF69B4')
    ax.spines['left'].set_color('#FF69B4')
    ax.spines['right'].set_color('#FF69B4')
    
    # Ajustar los límites de los ejes
    max_time = max(max(times) for times in sensor_times.values())
    ax.set_xlim(-0.5, max_time + 0.5)
    
    # Personalizar la leyenda
    legend = ax.legend(loc='upper right', 
                      frameon=True, 
                      facecolor='#FFF0F5',
                      edgecolor='#FFB6C1')
    for text in legend.get_texts():
        text.set_color('#FF1493')
    
    # Guardar el gráfico
    plt.savefig('sensor_activation.png', 
                dpi=300, 
                bbox_inches='tight',
                facecolor='#FFF0F5')
    plt.close()

def plot_method_comparison(lp_value, sa_value):
    """
    Crée un graphique comparant les résultats de la PL et du Recuit Simulé.
    Style girly avec des couleurs roses.
    """
    # Crear la figura con fondo rosa claro
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#FFF0F5')  # Fondo rosa muy claro
    
    # Datos para el gráfico
    methods = ['Programmation Linéaire', 'Recuit Simulé']
    values = [lp_value, sa_value]
    colors = ['#FFB6C1', '#FF69B4']  # Tonos de rosa
    
    # Crear las barras
    bars = ax.bar(methods, values, color=colors, edgecolor='#FF1493', linewidth=2)
    
    # Añadir los valores encima de las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', 
                fontsize=12,
                color='#FF1493',
                fontweight='bold')
    
    # Configurar los ejes
    ax.set_ylabel('Valeur de la Fonction Objectif', 
                 fontsize=12, 
                 color='#FF69B4')
    ax.set_title('Comparaison des Méthodes d\'Optimisation', 
                 fontsize=14, 
                 color='#FF1493',
                 pad=20)
    
    # Personalizar la cuadrícula
    ax.grid(True, linestyle='--', alpha=0.3, axis='y', color='#FFB6C1')
    
    # Personalizar los ejes
    ax.spines['bottom'].set_color('#FF69B4')
    ax.spines['top'].set_color('#FF69B4')
    ax.spines['left'].set_color('#FF69B4')
    ax.spines['right'].set_color('#FF69B4')
    
    # Ajustar los límites del eje Y
    max_value = max(values)
    ax.set_ylim(0, max_value * 1.1)
    
    # Personalizar las etiquetas del eje X
    plt.xticks(color='#FF1493')
    
    # Guardar el gráfico
    plt.savefig('method_comparison.png', 
                dpi=300, 
                bbox_inches='tight',
                facecolor='#FFF0F5')
    plt.close()

def main():
    # Datos de ejemplo
    sensor_times = {
        0: [0, 1, 2, 3, 4],  # s1
        1: [0, 1, 2, 3],     # s2
        2: [0, 1, 2, 3, 4, 5], # s3
        3: [0, 1, 2]         # s4
    }
    
    # Crear el gráfico de activación de sensores
    plot_sensor_activation(sensor_times)
    
    # Crear el gráfico de comparación de métodos
    plot_method_comparison(18.0, 18.0)

if __name__ == "__main__":
    main() 
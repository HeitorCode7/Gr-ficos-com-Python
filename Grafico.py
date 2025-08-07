import matplotlib.pyplot as plt
import numpy as np


epsilon = 1e-6  
input_sizes = [10, 100, 1000, 10000, 100000, 1000000]
times = {
    "Shell Sort": [max(0.000000, epsilon), max(0.000000, epsilon), max(0.000000, epsilon), max(0.000000, epsilon), 0.005000, 0.057000],
    "Merge Sort": [max(0.000000, epsilon), max(0.000000, epsilon), max(0.000000, epsilon), max(0.000000, epsilon), 0.021000, 0.156000],
    
}


plt.figure(figsize=(10, 6))
colors = ['blue', 'orange', 'green', 'red', 'purple']  
markers = ['o', 's', 'd', '^', 'x']  

for (name, time), color, marker in zip(times.items(), colors, markers):
    plt.plot(input_sizes, time, marker=marker, color=color, label=name, markersize=6, linewidth=1.5)


plt.xscale('log')
plt.yscale('log')
plt.xlabel("Tamanho da Entrada", fontsize=12)
plt.ylabel("Tempo de Execução (s)", fontsize=12)
plt.title("Comparação dos Algoritmos", fontsize=12)
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.legend(fontsize=10, loc="upper left")
plt.tight_layout()

# Mostrar o gráfico
plt.show()

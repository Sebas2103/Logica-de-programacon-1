import matplotlib.pyplot as plt
import numpy as np


#constante
a=20
#valor de x en un rango de 1 a 10 con paso 1
x = np.arange(-10, 10, 0.1)
#formula de la catenaria 
y = a * np.cosh(x / a)
#print de la grafica 
plt.plot(x, y, color='cyan')
plt.text(-2.30, 22.5, "Simon Castrillón", color='orange', fontsize=12, fontstyle='italic')
plt.text(-2.30, 22.3, "Juan Sebastián Díaz", color='orange', fontsize=12, fontstyle='italic')
plt.grid(True)
plt.xlabel('Eje x',fontsize=14, color='red')
plt.ylabel('Eje y',fontsize=14, color='purple')
plt.show()
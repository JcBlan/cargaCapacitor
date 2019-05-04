
# Ejercicio 1 

import json 
import math
def minimosCuadrados(archivo):
    
    #Cargar datos desde json
    with open(archivo, "r") as datos:
        valores = json.load(datos)
    datos.close()

    #cantidad de valores
    n = len(valores)
    #sumatoria en x
    sumX = 0.0
    #sumatoria en y
    sumY = 0.0
    #sumatoria de x*y
    sumXY = 0.0
    #sumatoria de x^2
    sumX2 = 0.0

    # hallar sumatorias
    for x, y in valores.items():
        sumX = sumX + float(x)
        sumY = sumY + float(y)
        sumXY = sumXY + (float(x) * float(y))
        sumX2 = sumX2 + math.pow(sumX, 2)

    # calcular ajuste por minimos cuadrados
    #chapra 17.1.2 fig 17.6 pag 470
    a1 = ( (n* sumXY) - (sumX * sumY) ) / ((n * sumX2) - math.pow(sumX, 2) )

    # chapra 17.1.2 fig 17.7 pag 470
    a0 = ( sumY / n ) - ( a1 * ( sumX / n ) )

    return (a0, a1)

if __name__ == "__main__":
    coeficientes = minimosCuadrados("datos.json")
    print("a0: ", coeficientes[0])
    print("a1: ", coeficientes[1])

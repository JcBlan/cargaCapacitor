from colorama import init, Fore, Back, Style
from scipy.interpolate import lagrange
import json 
import math
import matplotlib.pyplot as plt
import numpy as np

#
#    Ejercicio 1
#

def funcionLinealizada(x):
    return ((-1/ (12000 * 0.00022)) * x + math.log(10))


def valoresCoeficientes(archivo):
    
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

    valoresY = []
    # crear lista con imagenes de funcion linealizada
    for x in valores.keys():
        valoresY.append(funcionLinealizada(float(x)))

    # crear lista con valores x
    valoresX = []
    for x in valores.keys():
        valoresX.append(float(x))

    #calcular sumatorias
    for x in range(len(valoresX)):
        sumY = sumY + float(valoresY[x])
        sumX = sumX + float(valoresX[x])
        sumXY = sumXY + (float(valoresX[x]) * float(valoresY[x]))
        sumX2 = sumX2 + math.pow(float(valoresX[x]), 2)


    # calcular ajuste por minimos cuadrados
    #chapra 17.1.2 fig 17.6 pag 470
    a1 = ( (n* sumXY) - (sumX * sumY) ) / ((n * sumX2) - math.pow(sumX, 2) )

    # chapra 17.1.2 fig 17.7 pag 470
    a0 = ( sumY / n ) - ( a1 * ( sumX / n ) )

    return a0, a1

#
#EJERCICIO 2    
#

def graficaPreliminar(valoresX, valoresY):
    plt.plot(valoresX, valoresY, ".")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.title("Ejercicio 2")
    plt.show()

def valorIncognita(archivo):
    a0, a1 = valoresCoeficientes(archivo)
    
    tau =( -1 /  a1)
    print("Incognita (tau): ", tau)
    print("Error cometido: ", (12000*0.00022) - tau)


   
    
#        
#EJERCICIO 3
#

def funcionExponencial(a0, a1, x):
    return ( math.exp(a0) * (1- math.exp(a1* x)))

def graficaSuperpuesta(valoresX, valoresY):    
    
    a0, a1 = valoresCoeficientes("datos.json")

    imagenesFuncion = []
    for x in valoresX:     
        imagenesFuncion.append(funcionExponencial(a0, a1, x))
    
    plt.plot(valoresX,imagenesFuncion, '-', label="Datos teoricos")
    
    plt.plot(valoresX, valoresY, ".", label="Datos experimentales")
    plt.title("Ejercicio 3")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.legend()

    plt.show()





#EJERCICIO 4
def interpolacionLineal():
    R = 12000
    C = 0.00022
    x = R * C
    # Datos obtenidos de los experimentos
    xCero = 2.6262626e+00
    xUno = 2.7272727e+00
    fXcero = 6.1825397e+00
    fXUno = 6.4982541e+00
    fX = fXcero + ((fXUno - fXcero) / (xUno - xCero)) * (x - xCero)
    print("Valor del parametro incognita\n\ttau: " + str(fX))





#EJERCICIO 5
def ajusteSinCuadradoMin(valoresX, valoresY):
    #plt.plot(valoresX, valoresY, ".")
    #lag_pol = lagrange(valoresX, valoresY)
    #print(lag_pol)

    p = np.polynomial.Chebyshev.fit(valoresX, valoresY, 90)
    print(type(p))    
    #x = np.linspace(valoresX[0], valoresX[11])
    plt.plot(valoresX, valoresY, 'r.', label="Datos Experimentales")
    t = np.linspace(0, 10, 10)
    #plt.xlabel("T")
    #plt.ylabel("V")
    #plt.plot(x, lag_pol(x),  "-")
    plt.plot(t, p(t), '-', lw=2, label="Curva adaptada")
    plt.title("Ejercicio 5") 
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.show()

if __name__ == "__main__":

        
    # Cargar datos desde json
    with open("datos.json", "r") as datos:
        valores = json.load(datos)
    datos.close()

    #convertir dict a list
    valoresX = []
    valoresY = []

    #convertir string a float
    for x, y in valores.items():
        valoresX.append(float(x))
        valoresY.append(float(y))


    #EJERCICIO 1
    print(f"\n\n{Fore.RED}Ejercicio1:{Style.RESET_ALL} \nLos valores de los coeficientes a0 y a1 son: " + str(valoresCoeficientes("datos.json")) + " Respectivamente" )

    #EJERCICIO 2
    print(f"\n \n{Fore.RED}Ejercicio2:{Style.RESET_ALL} \nGrafica Preliminar De Los Datos")
    graficaPreliminar(valoresX, valoresY)
    valorIncognita("datos.json")

    #EJERCICIO 3
    print(f"\n\n{Fore.RED}Ejercicio 3:{Style.RESET_ALL} \nGrafica De Los Datos Experimentales y de los valores Obtenidos por la ecuacion linealizada")
    graficaSuperpuesta( valoresX, valoresY)

    #EJERCICIO 4
    print(f"\n\n{Fore.RED}Ejercicio 4:{Style.RESET_ALL}\nInterpolacion lineal de Newton")
    interpolacionLineal()

    #EJERCICIO 5
    print(f"\n\n{Fore.RED}Ejercicio 5:{Style.RESET_ALL} \nAjuste de curva con Chebyshev")
    ajusteSinCuadradoMin(valoresX, valoresY)
"""
Nombre del Alumno: Victor Ariel Bazan Gonzalez 
Matricula: UX25II210
Fecha: 25/05/26
Examen Segundo Parcial - Programacion Estructurada
"""

import datetime
import math
import random
import statistics
import sys

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

def obtener_info_sistema():
    print(" INFORMACION DEL SISTEMA ")
    print("Plataforma: " + sys.platform)
    print("Version de Python: " + sys.version)
    print("Ruta del script: " + sys.argv[0])

def simular_metricas_entrenamiento(cantidad_epochs):
    eventos = ["Epoch exitoso", "Gradiente inestable", "Actualizacion de pesos"]
    lista_loss = []
    lista_latencia = []

    hora_inicio = datetime.datetime.now()
    print("Inicio: " + hora_inicio.strftime("%d/%m/%Y %H:%M:%S"))

    for i in range(cantidad_epochs):
        loss = random.uniform(0.1, 1.0)
        probabilidad = random.random()
        evento = random.choice(eventos)
        latencia = random.uniform(0.5, 3.0)

        lista_loss.append(loss)
        lista_latencia.append(latencia)

        print("Epoch " + str(i + 1) + " | Loss: " + str(round(loss, 4)) + " | Evento: " + evento)

        if loss > UMBRAL_ERROR_CRITICO:
            print(" Error critico detectado en epoch " + str(i + 1))

    hora_fin = datetime.datetime.now()
    diferencia = hora_fin - hora_inicio
    print("Fin: " + hora_fin.strftime("%d/%m/%Y %H:%M:%S"))
    print("Duracion total: " + str(diferencia))

    return lista_loss, lista_latencia

def analizar_rendimiento(lista_loss, lista_latencia):
    media = statistics.mean(lista_loss)
    desviacion = statistics.stdev(lista_loss)
    mediana = statistics.median(lista_latencia)

    print(" ANALISIS DE RENDIMIENTO ")
    print("Media : " + str(round(media, 4)))
    print("Desviacion : " + str(round(desviacion, 4)))
    print("Mediana : " + str(round(mediana, 4)) + " segundos")

def calcular_rmse(predicciones, reales):
    suma = 0
    for i in range(len(predicciones)):
        diferencia = predicciones[i] - reales[i]
        suma += math.pow(diferencia, 2)

    promedio = suma / len(predicciones)
    rmse = math.sqrt(promedio)
    epochs_redondeados = math.ceil(rmse * 10)

    print("  CALCULO DE RMSE ")
    print("RMSE: " + str(round(rmse, 4)))
    print("Epochs ajustados: " + str(epochs_redondeados))

    return rmse

def generar_datos_prueba():
    predicciones = []
    reales = []
    for i in range(5):
        predicciones.append(random.uniform(0.1, 1.0))
        reales.append(random.uniform(0.1, 1.0))
    return predicciones, reales

def main():
    print(" INICIANDO SIMULADOR DE AGENTES DE IA ")

    obtener_info_sistema()

    print("\n SIMULACION DE ENTRENAMIENTO ")
    lista_loss, lista_latencia = simular_metricas_entrenamiento(MAX_EPOCHS)

    print()
    analizar_rendimiento(lista_loss, lista_latencia)

    predicciones, reales = generar_datos_prueba()
    print()
    rmse = calcular_rmse(predicciones, reales)

    if rmse > UMBRAL_ERROR_CRITICO:
        print("Loss critico - Saliendo del sistema ")
        sys.exit(1)
    else:
        print("\n SIMULACION COMPLETADA EXITOSAMENTE ")

if __name__ == "__main__":
    main()

"""
Cuestionario  

1= Uso de Objetos y Metodos
En datetime.datetime.now() el primer datetime es la biblioteca el segundo datetime es la clase y now() es el metodo
Una biblioteca agrupa clases y funciones, al importar datetime entramos a la clase y llamamos su metodo para obtener la hora actual

2= Diferenciacion Tecnica
Con import math debemos escribir math.sqrt() cada vez
Con from math import sqrt podemos escribir solo sqrt()
La primera forma es mas clara porque sabemos de donde viene cada funcion

3= Flujo y Logica
La funcion simular_metricas_entrenamiento genera datos aleatorios de entrenamiento y almacena los valores de loss en listas
Despues esas listas se envian a analizar_rendimiento para calcular media, desviacion estandar y mediana
Finalmente se generan listas de predicciones y valores reales que se pasan a calcular_rmse para obtener el error del modelo

4= Mapeo de Tipos de Datos
Use listas para lista_loss y lista_latencia porque necesitaba guardar multiples valores por epoch
una variable simple solo guarda un valor, la lista guarda todos para analizarlos con statistics

5= Autoevaluacion de Abstraccion
No programe la formula de desviacion estandar
Solo llame statistics.stdev() y la biblioteca hizo el calculo
Esto es abstraccion no necesitamos saber como esta implementada, solo la llamamos y nos da el resultado
"""
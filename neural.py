#encoding: utf-8

#Red neuronal de juguete:
#Objetivo emular la tabla de verdad AND
#Basado en:
#http://blog.facialix.com/tutorial-desarrolla-tu-primera-neurona-artificial-sin-usar-librerias-externas/
import random, itertools

VALOR_UMBRAL = 1
TASA_APRENDIZAJE = .3
C_E = CASOS_ENTRADA =  tuple(
				itertools.product((1,0), (1,0))
			)
S_E = SALIDA_ESPERADA = (1, 0, 0, 0)

#random.uniform da un número flotante entre -1,1.
#recordar que hay limites en este calculo, por ser en
#computadora, punto fijo y esas cosas.
p1, p2, p_umbral = pesos = [random.uniform(-1, 1) for i in range(3)]

def funcion_activacion(salida_real: float) -> int:
	return int(salida_real > 0)
	
def perceptron(entradas: tuple, pesos: list) -> int:
	e1, e2 = entradas
	p1, p2, p_umbral = pesos
	return funcion_activacion(e1*p1 + e2*p2 + VALOR_UMBRAL*p_umbral)
	
def desviacion_y_error(salida_esperada: int, salida_obtenida: int) -> tuple:
	error = salida_esperada - salida_obtenida
	desviacion = TASA_APRENDIZAJE * error
	return (desviacion, error != 0)
	
def coeficiente_de_correccion(entrada: int, peso: float, desviacion: float) -> float:
	return	peso + entrada * desviacion
	
def corregir_pesos(entradas: tuple, desviacion: float) -> None:
	#global pesos
	entradas = (*entradas, VALOR_UMBRAL)
	desviaciones = (desviacion, )*3
	pesos[:] = [*map(coeficiente_de_correccion, entradas, pesos, desviaciones)]
	
	
def mostrar_pesos() -> None:
	print(f'\nIteraciones: {iteracion}')
	for i, peso in enumerate(pesos, 1):
		print(f'Peso {i}: {peso}')
		
def comparar_resultados() -> None:
	for i in range(4):
		salida_obtenida = perceptron(C_E[i], pesos)
		print(f'Entradas: {C_E[i]}  | Salida esperada: {S_E[i]} | Salida perceptron: {salida_obtenida}')
		
if __name__ == '__main__':

	iteracion = 0
	aprendiendo = True
	while aprendiendo:
		iteracion += 1
		aprendiendo = False
		
		for i in range(4):
			#Ingresando datos al perceptron y obteniendólos.
			salida_obtenida = perceptron(C_E[i], pesos)
			
			#Calculando la desviación en caso de error.
			desviacion, error = desviacion_y_error(S_E[i], salida_obtenida)

			#Verificación de errores y correción.
			if error:
				corregir_pesos(C_E[i], desviacion)
				aprendiendo = True
				
	#Visualización de resultados obtenidos, tras las correcciones.
	mostrar_pesos()
	print()
	comparar_resultados()

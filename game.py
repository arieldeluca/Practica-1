from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

contador_correcto=0
contador_incorrecto=0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    correct_answer = eval (str(number_1) + str(operator) + str(number_2))
    
    
    if ( float(result) == float(correct_answer)) :
        contador_correcto=contador_correcto + 1
        print("respuesta correcta") 

    elif (float(result) != float(correct_answer)) :
        contador_incorrecto=contador_incorrecto + 1
        print("respuesta incorrecta")
    

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f" \n Tardaste {total_time.seconds} segundos.")
print(f" Tuviste {contador_correcto} respuestas correctas y {contador_incorrecto} respuestas incorrectas.")
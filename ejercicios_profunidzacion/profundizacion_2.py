# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
menu = 'OK' # Variable que controla el while seteada para que entre
while menu != 'FIN':
    menu = input('\nEliga la operación que desee realizar (ingrese el símbolo correspondiente):\n'
                '- Suma (+)\n- Resta (-)\n- Multiplicación (*)\n- División (/)\n- Exponente/Potencia (**)'
                '\n Ingrese "FIN" para cerrar la calculadora.\n')
    if menu == 'FIN' or menu == 'fin' or menu == 'Fin': # Cuando el usuario quiera terminar
        break # Sale del while y el programa termina
    elif menu == '+' or menu == '-' or menu == '*' or menu == '/' or menu == '**': # En caso de que haya ingresado una operación
        print('A continuación ingrese 2 números para realizar una operación.') # Pedido de nros.
        num_1 = int(input('Ingrese un número para operar: '))
        num_2 = int(input('Ingrese otro número para operar: '))
        if menu == '+': # Suma
            resultado = num_1 + num_2
        elif menu == '-': # Resta
            resultado = num_1 - num_2
        elif menu == '*': # Multiplicación
            resultado = num_1 * num_1
        elif menu == '/': # División
            resultado = num_1 / num_2
        elif menu == '**': # Exponente/Potencia
            resultado = num_1 ** num_2
        print(f'El resultado de operar {num_1} {menu} {num_2} es: {resultado}') # Se imprime el resultado
    else: # En caso de que ingrese un caracter invalido a la variable 'menu'
        print(f'Error, {menu} no es un carácter válido. Por favor ingrese nuevamente.')
        
# el ciclo while se va repitiendo mientras se cumpla una condicion
numero=0
print("tabla del 7")
# ciclo while para la tabla del 7
while numero<=10:
    # pythob maneja identacion que es el primer estacio despues del while en el siguiente renglon
    print(f'7X{numero}={numero*7}') # interpolacion de texto y variables la f prepara al print para mezcla tex con variables
    numero += 1
print("fin")
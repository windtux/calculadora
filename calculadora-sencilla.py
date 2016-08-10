def suma():
    nume1 = float(input('ingrese un numero (no necesariamente deben ser enteros) '))
    nume2 = float(input('ingrese otro numero (no necesariamente deben ser enteros) '))
    resultado = nume1 + nume2
    print ('el resultado de ambos numeros es ',resultado)
    pregunta = (input('desea continuar usando la aplicacion? Si(s) o No(n) '))
    if pregunta =='s':
        suma()
    elif pregunta == 'n':
        return 0
print ('aplicacion solo para sumar dos numeros')
suma()
print ('saliendo del programa, hasta luego')
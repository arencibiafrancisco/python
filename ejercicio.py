#Entrada de datos
a= int(input("Entre el primer número "))
if type(a) != int:
    raise TypeError       
b= int(input ("Entre el segundo número "))
if type(b) != int:
    raise TypeError

#Procesamiento de datos
a= a/10
b=b/10
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b

#Salida de resultados
print(str(a) , ' + ' , str(b) + ' = ' + str(suma))
print(str(a) + ' - ' + str(b) + ' = ' + str(resta))
print(str(a) + ' * ' + str(b) + ' = ' + str(multiplicacion))
print(str(a) + ' / ' + str(b) + ' = ' + str(division))

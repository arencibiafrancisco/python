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
suma =round(a+b,2)
resta =round( a-b,2)

multiplicacion =round( a*b,2)
division = round(a/b,2)

#Salida de resultados
print(str(a) , ' + ' , str(b) + ' = ' + str(suma))
print(str(a) + ' - ' + str(b) + ' = ' + str(resta))
print(str(a) + ' * ' + str(b) + ' = ' + str(multiplicacion))
print(str(a) + ' / ' + str(b) + ' = ' + str(division))

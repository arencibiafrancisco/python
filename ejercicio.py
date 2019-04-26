a= int(input("Entre el primer número "))
if type(a) != int:
    raise TypeError       

a= a/10
b= int(input ("Entre el segundo número "))
if type(b) != int:
    raise TypeError
b=b/10
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
print(str(a) + ' + ' + str(b) + ' = ' + str(suma))
print(str(a) + ' - ' + str(b) + ' = ' + str(resta))
print(str(a) + ' * ' + str(b) + ' = ' + str(multiplicacion))
print(str(a) + ' / ' + str(b) + ' = ' + str(division))

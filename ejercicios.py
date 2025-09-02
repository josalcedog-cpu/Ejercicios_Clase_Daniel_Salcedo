# Autor: José Daniel Salcedo Gutiérrez
# Ejercicios de Clase

# ______________________Conversión de Datos______________________
#En este ejercicio se realizaran las conversiones entre 3 datos distintos; int, float y str entre cada uno de ellos.

# Variable de entrada enteros (int): 

print("int a float:")
x1 = float(int(input("Escriba el valor para operar: \n ")))
print(f"El tipo de dato es: {type(x1)} y el valor del dato es {x1}")
print("La suma de la variable int a float es",x1 + x1)


print("int a str:")
x2 = str(int(input("Escriba el valor para operar: \n ")))
print(f"El tipo de dato es: {type(x2)} y el valor del dato es {x2}")
print("La suma de la variable int a srt es",x2 + x2)

# Variable de entrada decimales (float)

print("float a int:")
x3 = int(float(input("Escriba el valor para operar: \n ")))
print(f"El tipo de dato es:  {type(x3)} y el valor del dato es {x3}")
print("La suma de la variable float a int es",x3 + x3)


print("float a str:")
x4 = str(float(input("Escriba el valor para operar: \n ")))
print(f"El tipo de dato es: {type(x4)} y el valor del dato es {x4}")
print("La suma de la variable float a str es",x4 + x4)

# Variable de entrada cadena de texto (srt)
 
print("str a int:")
x5 = int(input("Escriba el valor para operar: \n "))
print(f"El tipo de dato es: {type(x5)} y el valor del dato es {x5}")
print("La suma de la variable str a int es",x5 + x5)

print("str a float:")
x6 = float(input("Escriba el valor para operar: \n "))
print(f"El tipo de dato es: {type(x6)} y el valor del dato es {x6}")
print("La suma de la variable str a float es",x6 + x6)


print ("==========================================================================================================")

# ______________________Funcion Input______________________
#En este ejercicio se utiliza la función input para resolver una ecuación lineal con constantes dadas por el usuario.


print(" Tenemos la siguiente ecuación lineal: AX = B - C \n Encuantre el valor de la variable X según los valores de A,B y C.")

print ("Introduzca los valores enteros para A, B y C: ")
A = int(input ("A:"))
B = int(input ("B:"))
C = int(input ("C:"))

print(" Ahora procedemos a despejar la variable que desconocemos (X)")
print(f"{A}*X = {B} - {C} \n Luego,")
print(f"X = ( {B} - {C} )/{A} \n y luego operamos,")
X = (B-C)/A

print (f"  X = {X} \n El valor de X es {X}")

print("==========================================================================================================")

# ______________________Ejercicios de Condicionales______________________
#En este ejercicio se realizaran 7 funciones if con los diferentes operadores comparativos que se vieron en clase.

#Igual:

print("-Igual a")

y1 = input("Digite su contraseña: ")

if(y1 == "12345"):
    print("Bienvenido.")
else: 
    print ("La contraseña es incorrecta.")

#Diferente de: 

print("-Diferente de")
y2 = int(input("Digite un valor entero: "))

if(y2 != 10):
    print("El valor que introdujo es diferente de diez")
else: 
    print ("Su valor es igual a 10")

# Mayor que: 

print("-Mayor que: ")
y3 = int(input("Digite un valor entero: "))

if(y3 > 10):
    print("El valor que introdujo es mayor de diez")
else: 
    print ("Su valor es menor a 10")    

#Menor que: 

print("-Menor que: ")

y4 = int(input("Digite un valor entero: "))

if(y4 < 10):
    print("El valor que introdujo es menor de diez")
else: 
    print ("Su valor es mayor a 10")    

#Mayor o igual que: 

print("-Mayor o igual que: ")

y5 = int(input("Digite un valor entero: "))

if(y5 >= 10):
    print("El valor que introdujo es mayor o igual a diez")
else: 
    print ("Su valor es menor a 10")   

#Menor o igual que: 

print("-Menor o igual que: ")

y6 = int(input("Digite un valor entero: "))

if(y6 < 10):
    print("El valor que introdujo es menor o igual a diez")
else: 
    print ("Su valor es mayor a 10")     


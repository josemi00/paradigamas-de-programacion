#===============================================================
# Input permite obtener del usuario en prompter
#===============================================================
nombre = input("Dame tu nombre: ")
print ("Hola como estas", nombre)

#===============================================================
# Los enteros son de precision ilimitada
#===============================================================

y = 500000000000000000000000000000000
print(y)

#===============================================================
# Se pueden delimitar numeros con guion bajo pero no con coma
y = 5_000_000
print(y)

#================================================================
# La notacion cientifica de flotantes utiliza e o E
#================================================================
# 1.2 x 10e^{-9}
#================================================================
y = 1.2E-09
print(y)

#================================================================
# La funcion float() convierte strings y enteros a floats
#================================================================
y = float("14.3")
print(y)

#================================================================
# Los complejos se escriben con la raiz de menos uno
# j siempre con un numero prefijo
# no acepta la j suelta
#================================================================
z = 1+1j
#suma +
#resta -
#multiplicacion *
#divison /
#exponente **
# // funcion piso
#funciones para transformar numero int() float() complex()
#operaciones abs() round() pow()

print(round(3.14159,4))

#==================================================================
# Strings de varias lineas
#==================================================================
parrafo = """ En el bosque de la china
 la chinita se perdio """
print(parrafo)

#==================================================================
# La funcion len() obtiene el tamano del string
#==================================================================
n=len(parrafo)
print(n)

#==================================================================
# Las letras en un string ocupan lugares como en un arreglo
# (tambien de tras para adelante comoenzando en -1 el ultimo)
#==================================================================

palabra = "hola"
print(palabra[0])
print(palabra[-4])


















        

#=========================================================================
# Primera funcion
#=========================================================================
def saludo():
    #=====================================
    # Documentacion rapida para la funcion
    #=====================================
    """Esta funcion saluda"""
    print('quiuboles, como estas')

#=====================
# Llamdo de la funcion
#=====================
saludo()

#================================
# Se ejecuta pero no se asigna
#================================
salida = saludo()

#================================
# Esto no funciona
#================================
print(salida)

#================================
# Mostrar documentacion
#================================
#help(saludo)

#================================
# Funcion con argumento
#================================
def salu2(nombre):
    """Esta funcion te saluda por tu nombre"""
    print("que onda ese",nombre,"!")
salu2("julian")
salu2("Angel")

#==========================================
# Ahorra trabajo de interprete
# nombre:str la varible nombre es un str
#==========================================
def saludos(nombre:str):
    """esta funcion te saluda por tu nombre estrictamente"""
    print("que onda es",nombre,"!")
saludos("Julian")
a = 123
print(type(a))
saludos(a)

#===========================================
# Funcion con muchos argumentos
#===========================================
def saludos_multiples(nombre1,nombre2,nombre3):
    """esta funcion saluda a 3 personas al mimsmo tiempo"""
    print("hola",nombre1,",",nombre2,"y",nombre3)
saludos_multiples("Hugo","Paco","Luis")

#===============================================
# Funcion con cualquier numero de argumentos
#===============================================
def muchos_saludos(*nombres):
    """Esta funcion saluda a toso los que quieras"""
    i = 0
    #===========================================
    # end= es para ponerlo corrido
    #===========================================
    print("Hola ", end="")
    while len(nombres) > i:
        # Ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1
muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Lev","Luis")
def greet(firstname, lastname):
    print('hello', firstname, lastname)
#==========================================================
# llamar la funcion con argumentos en desorden 
#==========================================================
greet(lastname='Jobs', firstname='Steve') #se pueden especificar las variables en desorden

#==========================================================
# Funcion con argumentos escondidos**
#==========================================================
def greet(**person):
    #======================================================
    # persona tiene caracteristicas firstname y lastname
    #======================================================
    print('hello', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) # se pueden pasar mas parametros de los necesarios

#=======================================
# Funcion con valores por defecto
#=======================================
def greet(name = 'Guest'):
    print('hello', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#=======================================
# Funcion con resultado
#=======================================
def suma(a, b):
    return a + b

#=======================================
# Programacion funcional
# Se pueden funciones en funciones
#=======================================
total=suma(5, suma(10, 20))
print(total)

#====================================================
# Calculo lambda
# nombre de la funcion = lambda variable : funcion
#====================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)

#====================================================
# lambda de varias variables
#====================================================
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#====================================================
# Uso de una funcion anonima
# El argumento va afuera entre parentesis
#====================================================
print((lambda x: x*x)(6))  #Funcion anonima

#====================================================
# Funcion con variable global
# Evite el exceso
#====================================================
name = 'Steve'
def greet():
    global name # Para utilizar una varibale global (que viene de fuera del bloque)
    name = 'Bill'
    print('Hello', name)

greet()



















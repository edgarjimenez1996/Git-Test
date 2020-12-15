# Ctrl +B para compilar en SublimeTex
# https://www.youtube.com/watch?v=tmY6FEF8f1o&ab_channel=KeithGalli

import turtle 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart


x = Complex(3.0,-4.5)
print ((x.r , x.i))



##############################################################################


class Poligono:
	def __init__(self, lados, nombre, tamaño, color="black", ancho_de_linea=2):  #cuado le agrefo a un atributo ="" defino un valor por default que puede cambiar en el momento de definir el objeto
	   self.lados = lados
	   self.nombre = nombre
	   self.tamaño = tamaño
	   self.color = color
	   self.ancho_de_linea=ancho_de_linea
	   self.angulos_interiores = (self.lados-2)*180
	   self.angulo= self.angulos_interiores/self.lados
	   
	def dibujar(self):
	    turtle.color(self.color)
	    turtle.pensize(self.ancho_de_linea)
	    for i in range (self.lados):
	         turtle.forward(self.tamaño)
	         turtle.right(180-self.angulo)
	    turtle.done()

             

cuadrado= Poligono(4,"cuadrado" , 100 , color="red")
triangulo = Poligono(3,"triangulo", 100, ancho_de_linea=9)

pentagono = Poligono (5,"pentagono" , 100)
hexagono =Poligono(6, "" , 100 , "blue")

octagono = Poligono(8,"octagono",100,color="green")

print("lados del cuadrado:" ,cuadrado.lados)
print("Atributo nombre del objeto cuadrado:",cuadrado.nombre)

print(hexagono.lados)
print(hexagono.nombre)



#triangulo.dibujar()
#hexagono.dibujar()
#octagono.dibujar()
#cuadrado.dibujar()


#Poligono(4,"cuadrado",100).dibujar( )


# Para entender la funcion de self se define la funcion dibujar 

# def dibujar_como_funcion(lados, ancho_de_linea, tamaño, color):
# 	angulos_interiores = (lados-2)*180
# 	angulo= angulos_interiores/lados
# 	turtle.color(color)
# 	turtle.pensize(ancho_de_linea)
# 	for i in range (lados):
# 		turtle.forward(tamaño)
# 		turtle.right(180-angulo)
# 		turtle.done()


# dibujar_como_funcion(4,2,100,"blue")


class Cuadrado(Poligono):   #Una subclase de Poligono
	def __init__(self, color="black", ancho_de_linea=2):
		super().__init__(4 ,"cuadrado" ,100 , color , ancho_de_linea) #take atributes from Poligon or the super class


cuadrado_2 = Cuadrado()
cuadrado_3 = Cuadrado(ancho_de_linea=100)
cuadrado_4 = Cuadrado(color="#123abc", ancho_de_linea=5)

#Que pasa si quiero re definir los lados de un cuadrado?
#No es parte de los atributos definidos para la clase Cuadrado
#cuadrado_error= Cuadrado(lados=6)  #Genera error 


print("lados cuadrado_2:",cuadrado_2.lados)
print("nombre cuadrado_2:",cuadrado_2.nombre)
print("tamaño cuadrado_2:",cuadrado_2.tamaño)
print("ancho_de_linea de cuadrado_2:",cuadrado_2.ancho_de_linea)
cuadrado_2.dibujar()
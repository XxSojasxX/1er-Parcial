from clase_metodo import Persona
from clase_metodos_str import Pizza
from datos import Datos
if __name__ == "__main__":
    
    
    pizza1 = Pizza ("Pizza hawaiana", "Pina", "Queso", "Familiar")
    
    cliente1 = Persona ("Sebastian", "Vaca", "Quito", "sebas@hotmail.com", 987654321)
    
    
    dato1 = Datos(1, Persona("Sebastian", "Vaca", "Quito", "sebas@hotmail.com", 987654321), Pizza("Pizza hawaiana", "Pina", "Queso", "Familiar"))
#1.-CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__

class Pizza:
    nombre       = str 
    ingrediente1 = str
    ingrediente2 = str
    tamaño       = str
    
    def __init__(self, nombre, ingrediente1, ingrediente2, tamaño):
        self.nombre = nombre
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.tamaño = tamaño

    def __str__(self):
        return f"Su orden es una {self.nombre} con {self.ingrediente1} y {self.ingrediente2} en tamaño {self.tamaño}"

pizza1 = Pizza("Pizza de la casa", "Jamon", "Queso", "Familiar")
print("1.-Clase con metodo Str:")
print(pizza1)

#2.- CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.

class Persona:
    nombre       = str 
    apellido     = str
    ciudad       = str
    correo       = str
    telefono     = str
    
    
    def __init__(self, nombre, apellido, ciudad, correo, telefono):
        self.nombre   = nombre
        self.apellido = apellido
        self.ciudad   = ciudad
        self.correo   = correo
        self.telefono = telefono
    
    def miFuncion(self):
        print("Buenos dias mi nombre es " +self.nombre+" " +self.apellido+" de la ciudad de "+self.ciudad+" deseo hacer un pedido de una pizza.")

cliente1 = Persona("Sebastian", "Vaca", "Quito", "sebas@hotmail.com", 987654321)
print("2.-Clase con metodo:")
cliente1.miFuncion()


#3.- REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
class Pedido:
    nombre       = str 
    apellido     = str
    direccion    = str

    def __init__(self, nombre, apellido,direccion):
        self.nombre     = nombre
        self.apellido   = apellido
        self.direccion  = direccion

class Repartidor(Pedido):
    codigo = int

    def __init__(self, nombre, apellido,direccion, codigo):
        super().__init__(nombre, apellido, direccion)
        self.codigo = codigo
    
    def __str__(self):
        return f"Buenos dias {self.nombre} {self.apellido} con direccion {self.direccion} el codigo de su repartidor es {self.codigo}"

Pedido1 = Repartidor("Sebastian", "Vaca", "Habana y tapi", 38)
print("3.-REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO")
print(Pedido1)
print(vars(Pedido1))

#4.- REALIZAR UNA HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO

from clase_metodo import Persona
from clase_metodos_str import Pizza

class Datos (Persona, Pizza):
     id = int
     Persona = Persona ("", "", "", "", "")
     Pizza = Pizza ("", "", "", "")
    
     def __init__(self, id, Persona, Pizza):
         
         self.id = id
         self.Persona = Persona
         self.Pizza = Pizza
     def __str__(self):
        return f"Buenos dias mi nombre es {self.nombre} {self.apellido} de la ciudad de {self.ciudad} deseo hacer un pedido de una pizza."
     def __str__(self):
        return f"Su orden es una {self.nombre} con {self.ingrediente1} y {self.ingrediente2} en tamaño {self.tamaño}"

cliente2 = Persona ("Jose", "Vega", "Quito", "jose@hotmail.com", 987657821)
pizza2 = Pizza("Pizza Hawaiana", "Pina", "Jamon", "Mediano")
print("4.-")
print(vars(cliente2))
print(cliente2)
print(vars(pizza2))
print(pizza2)   
         
#5.-REALIZAR UNA HERENCIA EN UNA CLASE QUE CONTENGA VARIOS OBJETOS (2) Y OBJETOS DENTRO DE OBJETOS (2)

print("")
print("Objetos en Objetos:")
print(vars(dato1))
print("Cliente")
print(vars(dato1.Persona))
print("Pizza")
print(vars(dato1.Pizza))
print("Pedido")
print(vars(dato1.Pedido))

        

    
    
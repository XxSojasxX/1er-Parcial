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
print("Clase con metodo:")
cliente1.miFuncion()
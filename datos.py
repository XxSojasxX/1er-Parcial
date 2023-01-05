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
        
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
print("Clase con metodo Str:")
print(pizza1)

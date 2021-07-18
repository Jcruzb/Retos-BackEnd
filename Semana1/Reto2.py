
class personas:
    def __init__(self, nombre, dni, fnac):
        self.nombre = nombre
        self.dni = dni
        self.fnac = fnac

asistentes = int(input("Ingrese el número de asistentes"))

for i in asistentes:
    personas[i].nombre = input("ingrese su nombre")

print (personas.nombre)
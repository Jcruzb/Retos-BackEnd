import datetime

hora =datetime.datetime.now()
print(hora.strftime('%H'))

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


if(edad<18):
    if(int(hora.strftime('%H'))<18):
        print("Vaya a hacer la tarea C#%&o!!")
    else:
        print("¡Hora de dormir!")
else:
    print("Haga lo que prefiera")
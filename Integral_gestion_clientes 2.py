# Clase abstracta de servicio 
from abc import ABC, abstractmethod

class servicio (ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_servicio(self):
        pass

# Clase derivadas (Herencia)    

class Sala(servicio):

    def mostrar_servicio(self):
        print(f"Sala: {self.nombre}, Precio: {self.precio}")

        
# Alquiler de equipos         

class equipos(servicio):

    def mostrar_servicio(self):
        print(f"Equipo: {self.nombre}, Precio: {self.precio}")

# Asesoria        

class asesoria(servicio):

    def mostrar_servicio(self):
        print(f"Asesoria: {self.nombre}, Precio: {self.precio}")

# Encapsulamiento: Clase cliente        

class cliente:

    def __init__(self, nombre, identificación):
        self.__nombre = nombre
        self.__identificación = identificación

    def get_nombre(self):
        return self.__nombre

    def get_identificación(self):
        return self.__identificación

# Clase Reserva: 

class reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio

    def mostrar_reserva(self):
        print(
            f"Cliente: {self.cliente.get_nombre()} - " 
            f"Servicio: {self.servicio._mostrar_nombre}"
        )            
# Polimorfismo:

Servicios = [
    Sala("Sala de reuniones", 1.000.000),
    equipos("Portatil", 200.000),
    asesoria("Asesoria de negocios", 700.000)
]        

for servicio in Servicios:
    servicio.mostrar_servicio()

# Excepción personalizada

class ReservaException(Exception):
    pass

try:
    nombre = input("Nombre del cliente: ")

    if nombre == "":
        raise ReservaException("El nombre del cliente no puede estar vacío.")

except ReservaException as e:
    print(f"Error: {e}")

# try/except/else

try:
    opcion = int(input("Seleccione un servicio: "))       

except ValueError:
    print("Error: Debe ingresar un número")

else:
    print("opcion valida")

#try/except/finally    


try:
    archivo = open("datos.txt", "r")

except FileNotFoundError:
    print("Archivo no encontrado")

finally:
    print("Proceso terminado")

# Registro de errores (logs)

import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR
)

try:
    int("abc")

except ValueError as e:
    logging.error(f"Error detectado: {e}")

# Lista para almacenar información:

clientes = []
reservas = []    

cliente1 = Cliente("Juan", "12345")
clientes.append(cliente1)

reserva1 = Reserva(
    cliente1,
    Sala("Sala Principal", 1.000.000)
)

reservas.append(reserva1)



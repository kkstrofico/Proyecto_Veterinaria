from Listas import *
import pandas as pd
class Propietario:
    def __init__(self,id_propietario,nombre_propietario,apellido_propietario,direccion_propietario,telefono_propietario,correo_propietario) -> None:
        self.id_propietario = id_propietario
        self.nombre_propietario = nombre_propietario
        self.apellido_propietario = apellido_propietario
        self.direccion_propietario = direccion_propietario
        self.telefono_propietario = telefono_propietario
        self.correo_propietario = correo_propietario
    def registar(self):#Permite registrar un propietario 
        datos_propietario = {}
        datos_propietario['Id'] = self.id_propietario
        datos_propietario['Nombre'] = self.nombre_propietario
        datos_propietario['Apellido'] = self.apellido_propietario
        datos_propietario['Direccion'] = self.direccion_propietario
        datos_propietario['Telefono'] = self.telefono_propietario
        datos_propietario['Correo'] = self.correo_propietario
        propietarios.append(datos_propietario)
class Mascota:#Clase Mascota - Resive todas las funciones que se le atribullen a la mascota
    def __init__(self,nombre_mascota,color_mascota,especie_mascota,raza_mascota,medico_veterinario = ''):
        self.nombre_mascota = nombre_mascota
        self.color_mascota = color_mascota
        self.especie_mascota = especie_mascota
        self.raza_mascota = raza_mascota
        self.medico_veterinario = medico_veterinario
class Veterinario:
    def __init__(self,id_veterinario,nombre_veterinario,apellidos_veterinario,direccion_veterinario,telefono_veterinario,tarjeta_profesional = {}):
        self.id_veterinario = id_veterinario
        self.nombre_veterinario = nombre_veterinario
        self.apellidos_veterinario = apellidos_veterinario
        self.direccion_veterinario = direccion_veterinario
        self.telefono_veterinario = telefono_veterinario
        self.tarjeta_profesional = tarjeta_profesional
class Visita:
    def __init__(self,temperatura,peso,frecuencia_respiratoria,frecuencian_cardiaca,id_profesional,recomendaciones):
        self.temperatura = temperatura
        self.peso = peso
        self.frecuencia_respiratoria = frecuencia_respiratoria
        self.frecuencia_cardiaca = frecuencian_cardiaca
        self.id_profesional = id_profesional
        self.recomendaciones = recomendaciones
        pass
from Clases import *
while True:
    print('\n\tMENU')
    print('Obciones:\n 1.Ragistrar Propietario')
    opcion = int(input('DIGITA AQUI: '))
    if opcion == 1:
        print('\nIngresa los datos del propietario\n')
        id = input('ID: ')
        nombre = input('NOMBRES: ')
        apellido = input('APELLIDO: ')
        direccion = input('DIRECCION: ')
        telefono = input('TELEFONO: ')
        correo = input('CORREO: ')
        propietario = Propietario(id,nombre,apellido,direccion,telefono,correo)
        propietario.registar()
        print('PROPIETARIO REGISTRADO EXITOSAMENTE')
        print(propietarios)
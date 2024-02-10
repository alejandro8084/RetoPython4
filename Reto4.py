def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_correo(correo):
    return "@" in correo and "." in correo and validar_longitud(correo, 5, 50)

def capturar_usuario(id_counter):
    nombre = input('Ingresa tu nombre: ')
    apellidos = input("Ingresa tus apellidos: ")
    telefono = input("Ingresa tu número de teléfono: ")
    email = input("Ingresa tu correo electrónico: ")

    while not (validar_longitud(nombre, 5, 50) and
               validar_longitud(apellidos, 5, 50) and
               validar_telefono(telefono) and
               validar_correo(email)):
        print("Error: Ingresa datos válidos.")
        nombre = input('Ingresa tu nombre: ')
        apellidos = input("Ingresa tus apellidos: ")
        telefono = input("Ingresa tu número de teléfono: ")
        email = input("Ingresa tu correo electrónico: ")

    id_counter[0] += 1
    return id_counter[0], {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "email": email}

def listar_usuarios(usuarios):
    print("ID de los usuarios registrados:")
    for usuario in usuarios:
        print(usuario[0])

def ver_info_usuario(id_usuario, usuarios):
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            print(f"Información del usuario con ID {id_usuario}:")
            print(f"Nombre: {usuario[1]['nombre']}")
            print(f"Apellidos: {usuario[1]['apellidos']}")
            print(f"Teléfono: {usuario[1]['telefono']}")
            print(f"Correo electrónico: {usuario[1]['email']}")
            return
    print("Usuario no encontrado.")

def editar_usuario(id_usuario, usuarios):
    for i, usuario in enumerate(usuarios):
        if usuario[0] == id_usuario:
            print(f"Editando información del usuario con ID {id_usuario}:")
            nombre = input('Ingresa el nuevo nombre: ')
            apellidos = input("Ingresa los nuevos apellidos: ")
            telefono = input("Ingresa el nuevo número de teléfono: ")
            email = input("Ingresa el nuevo correo electrónico: ")

            while not (validar_longitud(nombre, 5, 50) and
                       validar_longitud(apellidos, 5, 50) and
                       validar_telefono(telefono) and
                       validar_correo(email)):
                print("Error: Ingresa datos válidos.")
                nombre = input('Ingresa el nuevo nombre: ')
                apellidos = input("Ingresa los nuevos apellidos: ")
                telefono = input("Ingresa el nuevo número de teléfono: ")
                email = input("Ingresa el nuevo correo electrónico: ")

            usuarios[i] = (id_usuario, {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "email": email})
            print("Usuario actualizado.")
            return
    print("Usuario no encontrado.")

def menu():
    print("\n*** Menú de opciones ***")
    print("A. Registrar nuevos usuarios")
    print("B. Listar usuarios")
    print("C. Ver información de un usuario")
    print("D. Editar información de un usuario")
    print("E. Salir")

cantidad_usuarios = int(input("Ingresa la cantidad de usuarios a capturar: "))
usuarios = []
id_counter = [0]

for _ in range(cantidad_usuarios):
    usuario = capturar_usuario(id_counter)
    usuarios.append(usuario)

opcion = ""
while opcion != "E":
    menu()
    opcion = input("Elige una opción (A, B, C, D o E): ").upper()

    if opcion == "A":
        usuario = capturar_usuario(id_counter)
        usuarios.append(usuario)
        print("Usuario registrado exitosamente.")
    elif opcion == "B":
        listar_usuarios(usuarios)
    elif opcion == "C":
        id_usuario = int(input("Ingresa el ID del usuario que deseas ver: "))
        ver_info_usuario(id_usuario, usuarios)
    elif opcion == "D":
        id_usuario = int(input("Ingresa el ID del usuario que deseas editar: "))
        editar_usuario(id_usuario, usuarios)
    elif opcion == "E":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

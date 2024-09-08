
#Creamos la variable donde cargaremos a los clientes:
clientes = []

#y la función para cargar a los clientes: 
def registrar_cliente(nombre, apellido, rut):#rut sería el numero de cliente... 
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "rut":rut,
        "mascotas": []
        
    }

    clientes.append(cliente)
    print(f"Cliente {nombre} {apellido} registrado correctamente.")

#Hacemos una función para agregar la mascota(o lo que sea a un cliente, por ejemplo un auto si es un mecánico o una prenda si es un inventario de clientes, etc)...

def agregar_mascota(rut, nombre, tipo):
    for cliente in clientes:
        if cliente["rut"] == rut:
            mascota = {
                "nombre": nombre,
                "tipo": tipo
            }
            cliente["mascotas"].append(mascota)
            return
    print("Cliente no encontrado")    

#Esta sera la funcion para hacer un listado de sus clientes con sus mascotas, respectivamente:
def listar_clientes():
    if not clientes:
        print("No hay clientes registrados")
    else:
        for cliente in clientes:
            print(f"Nombre Cliente: {cliente ["nombre"]} {cliente["apellido"]}\n") 
            n = 1
            for mascota in cliente["mascotas"]:
                print(f"Mascota {n}:")
                print(f"Nombre: {mascota["nombre"]}, Tipo: {mascota["tipo"]}")
                n+=1

#Y esta función será para imprimir el historial de visitas de cada mascota:
def imprimir_historial_visitas(rut):
    for cliente in clientes:
        if cliente['rut'] == rut:
            filename = f"{cliente["nombre"]}_{cliente["apellido"]}_historial.txt"
            with open(filename,'w', encoding='utf-8') as file:
                for mascota in cliente['mascotas']:
                    file.write(f"Visita para {mascota['nombre']} {mascota["tipo"]}:\n")
                    file.write("Fecha: 01/01/2024, Resumen: Visita de control general.\n\n")
                print(f'Historial de visitas guardado en {filename}.')
                return 
            print("Cliente no encontrado")

#Y para finalizar hacemos el menu principal: 
def main():
    while True:
        print("\nOpciones")
        print("1. Registrar cliente")
        print("2. Agregar mascota a cliente")
        print("3. Listar todos los clientes con sus mascotas")
        print("4. Imprimir el historial de visitas")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            rut = input("Ingrese el rut del cliente: ")
            registrar_cliente(nombre, apellido, rut)
        elif opcion == '2':
            rut_cliente = input("Ingrese el rut del cliente: ")
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            tipo_mascota = input("Ingrese el tipo de mascota: ")
            agregar_mascota(rut_cliente, nombre_mascota, tipo_mascota)
        elif opcion == '3':
            listar_clientes()
        elif opcion == '4': 
            rut_cliente = input("Ingrese el rut del cliente: ")
            imprimir_historial_visitas(rut_cliente)
        elif opcion == '5':
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida,por favor seleccione nuevamente.")

main()





'''listar_clientes()
registrar_cliente("Luis", "Cerelli", 123)
agregar_mascota(123,"Bobby", "Perro")
agregar_mascota(123,"Matias","Huron")
registrar_cliente("Andrea", "Di Paolo", 124)
agregar_mascota(124,"Romulo", "Gato")
agregar_mascota(124,"Remo","Gato")
imprimir_historial_visitas(123)
imprimir_historial_visitas(124)
listar_clientes()'''




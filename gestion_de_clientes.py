
#Creamos la variable donde cargaremos a los clientes:
clientes = []

#y la función para cargar a los clientes: 
def registrar_cliente(nombre, apellido, rut):#rut sería el numero de cliente... 
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "mascotas": [],
        "rut":rut
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

print(clientes)
registrar_cliente("Luis", "Cerelli", 123)
agregar_mascota(123,"Bobby", "Perro")
print(clientes)
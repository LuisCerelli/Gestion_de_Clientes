
#Creamos la variable y la funcion para cargar a los clientes: 

clientes = []

def registrar_cliente(nombre, apellido):
    cliente = {
        "nombre": nombre,
        "apellido": apellido
    }

    clientes.append(cliente)

print(clientes)    

registrar_cliente("Luis","Cerelli")

print(clientes)
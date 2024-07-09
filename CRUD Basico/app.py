productos = []

def crearProducto(id, nombre, precio):
    data = {
        'id': id,
        'nombre': nombre,
        'precio': precio
    }
    productos.append(data)
    print('Producto Creado')

def listarProductos():
    for i in productos:
        print(i)

def eliminarProducto(id):
    del productos[id]
    print('Producto Eliminado')

def modificarProducto(id, key, value):
    productos[id][key] = value
    print('Producto Modificado')


crearProducto(1,'Pan', 1000)
crearProducto(2,'Bebida', 990)
listarProductos()
eliminarProducto(1)
listarProductos()
modificarProducto(0,'nombre', 'pan')
listarProductos()



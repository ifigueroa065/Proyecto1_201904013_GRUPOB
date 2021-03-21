class CLIENTE():
    def __init__(self,nombre,nit,direccion,propina):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.propina= propina

class PEDIDO():
    def __init__(self,cantidad,id):
        self.cantidad=cantidad
        self.id=id
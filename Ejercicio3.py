class Producto:
  def __init__(self,precio_bruto_producto):
    self.precio_bruto_producto = 100
  def facturar(self):
    precio_neto_producto = precio_bruto_producto + precio_bruto_producto * IVA
IVA_alimentacion = 0,055
IVA_servicios = 0,20   
class Producto_Servicio:
  def __init__(self, precio_neto_producto):
    precio_neto_producto = precio_bruto_producto + precio_bruto_producto * IVA_servicios
    print(precio_neto_producto)
class Producto_Alimenticio:
    def __init__(self, precio_neto_producto):
    precio_neto_producto = precio_bruto_producto + precio_bruto_producto * IVA_alimentacion
    print(precio_neto_producto)
  




  



# Ejercicios_Estructuras

Este es el enlace de mi repositorio: https://github.com/guerramorantemiguel/Ejercicios_Estructuras.git

# Ejercicio 1
```
class Bloque:
  def __init__(self):
    self.instrucciones = []
  def agregarInstruccion(self, instruccion):
    self.instrucciones.append(instruccion)
class Si:
  def __init__(self, condicion, entonces, si_no):
    self.condicion = condicion
    self.entonces = entonces
    self.si_no = si_no
class MientrasQue:
  def __init__(self, condicion, bloque):
    self.condicion = condicion
    self.bloque = bloque
class Mostrar:
  def __init__(self, mensaje):
    self.mensaje = mensaje

mostrar_ok = Mostrar('"OK"')
mostrar_ko = Mostrar('"KO"')
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa = Bloque()
bloque_alternativa.agregarInstruccion(alternativa)
bucle = MientrasQue(True, bloque_alternativa)
```
# Ejercicio 2
```

```
# Ejercicio 3
```
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
  
```

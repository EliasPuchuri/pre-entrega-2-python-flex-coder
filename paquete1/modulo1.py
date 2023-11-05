from datetime import datetime

class Cliente:
  def __init__(self, nombre, correo, edad):
    self.nombre = nombre
    self.correo = correo
    self.edad = edad
    self.carrito = []
    self.historial = []
    

  def __str__(self):
    return f'Cliente {self.nombre} registrado correctamente'
  
  def agragar_carrito(self, producto, sede, precio, cantidad):
    self.carrito.append({
      'producto': producto, 
      'sede': sede, 
      'precio': int(precio), 
      'cantidad': int(cantidad)
    })
    return 'Producto agregado al carrito'
  
  def comprar(self):
    monto = 0
    for prod in self.carrito:
      monto += prod['precio'] * prod['cantidad']
    
    self.carrito = []
    self.historial.append({'monto': monto, 'fecha': str(datetime.now())})
    return 'Gracias por confiar en nosotros'

  def enviar_boleta(self, monto):
    if len(self.historial) == 0:
      return 'Aún no ha realizado compras con nosotros' 
    
    return f'Se envió el detalle de la compra al correo: {self.correo} por el monto de ${monto:.2f}'
  
  
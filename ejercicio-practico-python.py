# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.
class Usuario:
  def __init__(self, nombre, contraseña):
    self.nombre = nombre
    self.contraseña = contraseña

  def __str__(self):
      return f"Mi nombre es: {self.nombre} y mi contraseña es: {self.contraseña}"
    
usuarioUno = Usuario("Caty", "246CA")
print(usuarioUno)
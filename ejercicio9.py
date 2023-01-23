#Creamos las funciones para dar a conocer la salud, posición, y la salud que le quitamos al enemigo.

class Warrior:
  def __init__(self, tipo):
    self.tipo = tipo
    self.salud = 100

  def block(self, posicion):
    self.posicion = posicion

  def attack(self, enemigo, position):
    if enemigo.posicion != position:
      enemigo.salud -= 10


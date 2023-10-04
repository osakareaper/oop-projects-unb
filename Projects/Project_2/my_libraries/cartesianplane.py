from my_libraries.shapes import *

class Plane():
  
  def __init__(self):
    self.shapes = {}
    print('O Plano Cartesiano foi inicializado! Bem-Vindo!')
    
  def insert(self, shape):
    self.shapes[shape.getType() + str(shape.getId())] = shape
    
  def remove(self, shape):
    del self.shapes[shape.getType() + str(shape.getId())]
    
  def showShapes(self):
    if not self.shapes:
      print('OBJETOS PRESENTES NO PLANO CARTESIANO:')
      print('O Plano cartesiano está vazio, insira alguns objetos!')
    else:
      print('OBJETOS PRESENTES NO PLANO CARTESIANO:')
      for shape in self.shapes.keys():
        print(shape)
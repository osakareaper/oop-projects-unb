from my_libraries.shapes import *
from my_libraries.cartesianplane import *

def workspace():
    
    # Inicialização do plano cartesiano
    print("")
    plane = Plane()
    print("")
    
    # Inicializando as 4 formas presentes
    pt1 = Point(1, 4, -5)
    pt2 = Point(2, 8, -5)
    circ1 = Circle(1, pt1, 3) # Herda 1 ponto como origem do círculo
    sqr1 = Square(1, 8)
    ln1 = Line(1, pt1, pt2) # Herda 2 pontos, o início da linha e o final da linha
    
    # Inserindo as formas no plano cartesiano e printando objetos presentes no plano
    plane.insert(pt1)
    plane.insert(pt2)
    plane.insert(circ1)
    plane.insert(sqr1)
    plane.insert(ln1)
    plane.showShapes()
    print("")
    
    # Removendo as formas do plano e logo após printando objetos presentes no plano
    plane.remove(pt1)
    plane.remove(pt2)
    plane.remove(circ1)
    plane.remove(sqr1)
    plane.remove(ln1)
    plane.showShapes()
    print("")
    
    # Utilizando as funções dos shapes!
    print(pt1.getType() + str(pt1.getId()) + ':')
    pt1.getCoord()
    pt1.moveToOrigin()
    pt1.getCoord()
    pt1.setCoord(19, -5)
    pt1.getCoord()
    pt1.getQuad()
    print("")
    
    print(circ1.getType() + str(circ1.getId()) + ':')
    circ1.getOrigin()
    circ1.setOrigin(28, -5)
    circ1.getOrigin()
    circ1.getRadius()
    circ1.getDiameter()
    circ1.getCircumference()
    circ1.getArea()
    print("")
    
    print(sqr1.getType() + str(sqr1.getId()) + ':')
    sqr1.getSide()
    sqr1.getPerimeter()
    sqr1.getDiagonal()
    sqr1.getArea()
    print("")
    
    print(ln1.getType() + str(ln1.getId()) + ':')
    ln1.getPoints()
    ln1.getLength()
    print("")
    
    
    
    
    

if __name__ == "__main__":
    workspace()
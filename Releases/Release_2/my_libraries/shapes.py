import math

class Point():
    
    def __init__(self, pointId, x, y):
        self._pointId = pointId
        self._x = x
        self._y = y
        
    def getType(self):
        return 'Ponto '
    
    def getId(self):
        return self._pointId
    
            
    def getCoord(self):
        print(f'O {self.getType()}{self._pointId} está localizado nas coordenadas: (x: {self._x}, y: {self._y})')
        
    def setCoord(self, x, y):
        self._x = x
        self._y = y
        print(f'[ATENÇÃO] As coordenadas do {self.getType()}{self._pointId} foram atualizadas!')
        
    def getQuad(self):
        if self._x == 0 and self._y == 0:
            print(f'O {self.getType()}{self._pointId} está na origem do plano.')
        elif self._x > 0:
            if self._y >= 0:
                print(f'O {self.getType()}{self._pointId} está no 1° quadrante.')
            elif self._y < 0:
                print(f'O {self.getType()}{self._pointId} está no 4° quadrante.')
        elif self._x < 0:
            if self._y >= 0:
                print(f'O {self.getType()}{self._pointId} está no 2° quadrante.')
            elif self._y < 0:
                print(f'O {self.getType()}{self._pointId} está no 3° quadrante.')
                
    def moveToOrigin(self):
        self._x = 0
        self._y = 0
        print(f'[ATENÇÃO] O {self.getType()}{self._pointId} foi movido para a origem do plano!')
                
class Circle(Point):
    
    def __init__(self, circleId, originPoint, r):
        self._originPoint = originPoint
        self._circleId = circleId
        self._r = r
        
    def getType(self):
        return 'Círculo '
    
    def getId(self):
        return self._circleId
    
    def getOrigin(self):
        x = self._originPoint._x
        y = self._originPoint._y
        print(f'A origem do {self.getType()}{self._circleId} está localizada nas coordenadas: (x: {x}, y: {y})')
        
    def setOrigin(self, x, y):
        self._originPoint._x = x
        self._originPoint._y = y
        print(f'[ATENÇÃO] As coordenadas da origem do {self.getType()}{self._circleId} foram atualizadas!')
        
    def getRadius(self):
        print(f'O raio do {self.getType()}{self._circleId} é: {self._r:,.2f} cm')
        
    def getDiameter(self):
        diameter = self._r * 2
        print(f'O diametro do {self.getType()}{self._circleId} é: {diameter:,.2f} cm')
        
    def getArea(self):
        area = math.pi * (self._r**2)
        print(f'A área do {self.getType()}{self._circleId} é: {area:,.2f} cm²')
        
    def getCircumference(self):
        circumference = 2*math.pi*self._r
        print(f'A circunferência do {self.getType()}{self._circleId} é: {circumference:,.2f} cm')
        
class Square():
    
    def __init__(self, squareId, side):
        self._squareId = squareId
        self._side = side
        
    def getType(self):
        return 'Quadrado '
    
    def getId(self):
        return self._squareId
    
    def getSide(self):
        print(f'Os lados do {self.getType()}{self._squareId} medem: {self._side:,.2f} cm')
        
    def getArea(self):
        area = self._side**2
        print(f'A área do {self.getType()}{self._squareId} é: {area:,.2f} cm²')
        
    def getPerimeter(self):
        perimeter = self._side * 4
        print(f'O perímetro do {self.getType()}{self._squareId} é: {perimeter:,.2f} cm')
        
    def getDiagonal(self):
        diagonal = self._side * math.sqrt(2)
        print(f'A diagonal do {self.getType()}{self._squareId} mede: {diagonal:,.2f} cm')
        
    
class Line:

    def __init__(self, lineId, startPoint, endPoint):
        self._lineId = lineId
        self._startPoint = startPoint
        self._endPoint = endPoint
        
    def getType(self):
        return 'Linha '
    
    def getId(self):
        return self._lineId
    
    def getPoints(self):
        x1 = self._startPoint._x
        y1 = self._startPoint._y
        x2 = self._endPoint._x
        y2 = self._endPoint._y
        print(f'A {self.getType()}{self._lineId} é formada pelo {self._startPoint.getType()}{self._startPoint.getId()} (x: {x1}, y: {y1}) e {self._endPoint.getType()}{self._endPoint.getId()} (x: {x2}, y: {y2})')
        
    def getLength(self):
        x1 = self._startPoint._x
        y1 = self._startPoint._y
        x2 = self._endPoint._x
        y2 = self._endPoint._y
        length = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(f'A {self.getType()}{self._lineId} mede: {length:,.2f} cm')
        
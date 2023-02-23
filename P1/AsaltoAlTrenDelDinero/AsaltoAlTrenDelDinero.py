from dataclasses import dataclass
from math import sqrt
import matplotlib.pyplot as plt

@dataclass
class Punto:
    def __init__(self, *args):
        self.x, self.y = args[0], args[1]
        self.coord= args
    def __repr__(self):
        s = "Punto("+str(self.x)+","+str(self.y)+")"
        return s
    def distancia(p1, p2):
            x = p1.x - p2.x
            y = p1.y - p2.y
            d = sqrt(x ** 2 + y ** 2)
            return d

@dataclass
class Linea:
    A: float
    B: float
    C: float
    p1: Punto
    p2: Punto
    tipo: str

    def __init__(self, p1, p2):
        mx = p2.x - p1.x
        if mx == 0:
          self.A = -1
          self.B = 0
          self.C = p1.x
        else:
          m = (p2.y - p1.y) / mx
          self.A = m
          self.B = -1
          self.C = m*(-p2.x) + p2.y
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"A:{self.A}, B:{self.B}, C:{self.C}, tipo:{self.tipo}"

#####FUNCTIONS#####
def getIntersectedPoint(p, l):
  x1 = l.p1.x
  y1 = l.p1.y
  x2 = l.p2.x
  y2 = l.p2.y
  x3 = p.x
  y3 = p.y
  dx, dy = x2-x1, y2-y1
  det = dx*dx + dy*dy
  a = (dy*(y3-y1)+dx*(x3-x1))/det
  return(Punto(x1+a*dx, y1+a*dy))

def distanciaSegmentoPunto(p: Punto, l: Linea):
    return abs((l.A*p.x + l.B*p.y + l.C) / sqrt(l.A ** 2 + l.B ** 2))

#####GRAPHICS#####
def acepta_listas(f):
  def inner(parametro, *args, **kwargs):
    if type(parametro) == list:
      for elemento in parametro:
        f(elemento, *args, **kwargs)
    else:
      f(parametro, *args, **kwargs)
  return inner

@acepta_listas
def graficarPunto(p, *args, **kwargs):
  x=p.x
  y=p.y
  plt.scatter(x,y, *args, **kwargs)

def graficarLinea(p1,p2,isTrail):
  if(isTrail):
    plt.plot([p1.x,p2.x],[p1.y,p2.y], color='olive')
  else:
    plt.plot([p1.x,p2.x],[p1.y,p2.y], color='lightseagreen')

#####INPUTS#####
puntos = []
vias = []

with open("1.in", 'r') as f:
    for i, l in enumerate(f):
        if i == 1:
            x = float(l)
        elif i == 2:
            base = Punto(x,float(l))
        elif i == 4:
            numPuntos = float(l)
        elif i > 5:
            if i % 2 == 0:
                x = float(l)
            else:
                puntos.append(Punto(x, float(l)))

#####MAIN#####
for i in range(0, len(puntos)-1):
    graficarLinea(puntos[i], puntos[i+1], 1)
    vias.append(Linea(puntos[i], puntos[i + 1]))

graficarPunto(puntos, color='olive')
graficarPunto(base, 100, color='red', marker='X')

menor = base.distancia(puntos[0])
puntoMenor = puntos[0]
for i in range(1, len(puntos)):
    dist = base.distancia(puntos[i])
    if dist < menor:
        menor = dist
        puntoMenor = puntos[i]

for i in range(len(vias)):
    dist = distanciaSegmentoPunto(base, vias[i])
    if dist < menor:
        tempPunto = getIntersectedPoint(base, vias[i])
        tempX = [vias[i].p1.x, vias[i].p2.x]
        tempY = [vias[i].p1.y, vias[i].p2.y]
        tempX.sort(key=lambda x: x)
        tempY.sort(key=lambda y: y)
        if tempPunto.x >= tempX[0] and tempPunto.x <= tempX[1] and tempPunto.y >= tempY[0] and tempPunto.y <= tempY[1]:
            menor = dist
            puntoMenor = tempPunto

graficarLinea(base, puntoMenor, 0)
graficarPunto(puntoMenor, 120, color='darkorange', marker='*')

font1 = {'family':'serif','color':'olive','size':14}
plt.title("Asalto en el Tren del Dinero\nRosita Aguirre, Lucia Castañeda & Eduardo González", fontdict=font1)
plt.show()
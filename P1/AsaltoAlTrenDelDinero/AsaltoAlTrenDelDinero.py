import sympy as sym
import numpy as np
from collections import deque
import math
import matplotlib.pyplot as plt
eps= 1e-4

class Punto:
    def __init__(self, *args):
        self.x, self.y = args[0], args[1]
        self.coord= args
    def __str__(self):
        s = "Punto("+str(self.x)+","+str(self.y)+")"
        return s
    def __repr__(self):
        s = "Punto("+str(self.x)+","+str(self.y)+")"
        return s
    def __eq__(self, other):
        if len(self.coord)!= len(other.coord):
            raise ArithmeticError
        return all( [abs(x1-x2)<eps for x1,x2 in zip(self.coord, other.coord)] )
    def rotar(self, grados):
        g = np.deg2rad(grados)
        R = np.array([[np.cos(g), -np.sin(g)],[np.sin(g),np.cos(g)]])
        P = np.array([[self.x],[self.y]])
        RP = np.dot(R,P)
        return Punto(RP[0],RP[1])
    def dist(self, other):
        d = np.sqrt((pow((other.y-self.y),2))+(pow((other.x-self.x),2)))
        return d
    # Ordena puntos en ángulo (círculo) Regresa ángulo hacia el orígen
    def angulo(self):
        return math.atan2(-self.y,-self.x)
    def anguloOrigenDif(self, orig):
        return math.atan2(-(self.x+orig.x),self.y+orig.y)
    def vector(self, a, b):
        return (Punto(b.x-a.x,b.y-a.y))


def getM(x1,y1,x2,y2):
    return (y2 -y1) / (x2 -x1)

def getC(p, q, m):
  return (q + (1 / m)*p)
  
def getB(x, y, m):
  return y - m*x


def getDistance(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


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
    plt.plot([p1.x,p2.x],[p1.y,p2.y], color='pink')

# p1 = Punto(1, 4)
# p2 = Punto(3, 5)
# p3 = Punto(4, 7)
# p4 = Punto(6, 4)
# p5 = Punto(9, 3)

# base = Punto(3, 2)

# numPuntos = 5
# puntos = [p1, p2, p3, p4, p5]

puntos = []

with open("1.in", 'r') as f:
    for i, l in enumerate(f):
        if i == 1:
            x = l.split(" ")
        elif i == 2:
            base = Punto(x,l)
        elif i == 4:
            numPuntos = l.split(" ")
        elif i > 5:
            if i % 2 == 0:
                x = l.split(" ")
            else:
                puntos.append(Punto(x, l.split(" ")))

distancias = []
pConDist = []

for i in range(0, len(puntos)-1):
    graficarLinea(puntos[i], puntos[i+1], 1)

for punto in puntos:
    graficarPunto(punto, color='olive')

graficarPunto(base, 100, color='red', marker='X')

for i in range(0, 4):
  x1 = puntos[i].x
  y1 = puntos[i].y

  x2 = puntos[i + 1].x
  y2 = puntos[i + 1].y
  
  m = getM(x1, y1, x2, y2)
  b = getB(x1, y1, m)
  c = getC(base.x, base.y, m)

  x=sym.Symbol('x')
  y=sym.Symbol('y')
  resp=sym.solve([y-(m*x)-b, y+(m*x) - c], dict=True)

  if resp[0][x] < x1 or resp[0][x] < x2 or resp[0][y] < y1 or resp[0][y] < y2:
    break
  else:
    nuevoPunto = Punto(resp[0][x], resp[0][y])
    puntos.append(nuevoPunto)

for punto in puntos:
  #distancias.append(getDistance(punto.x, punto.y, base.x, base.y))
  pConDist.append((punto, getDistance(punto.x, punto.y, base.x, base.y)))
  
pConDist.sort(key = lambda x: x[1])

print(pConDist)
cercanoPunto = pConDist[0][0]

graficarLinea(base, cercanoPunto, 0)
graficarPunto(cercanoPunto, 100, color='darkorange', marker='*')

font1 = {'family':'serif','color':'olive','size':14}
plt.title("Asalto en el Tren del Dinero\nRosita Aguirre, Lucia Castañeda & Eduardo González", fontdict=font1)
plt.show()

"""
lx1 = 0
ly1 = 1

lx2 = 3
ly2 = 4

px = 3
py = 2

m = getM(lx1, ly1, lx2, ly2)
b = getB(lx1, ly1, m)
c = getC(px, py, m)

print(f"Funcion 1: y = {m}x + {b}")
print(f"Funcion 2: y = -{m}x + {c}")
"""

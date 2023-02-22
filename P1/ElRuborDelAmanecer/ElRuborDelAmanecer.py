from dataclasses import dataclass
from math import sqrt
import matplotlib.pyplot as plt

@dataclass
class Punto:
  x: float
  y: float

  def distancia(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    d = sqrt(x**2+y**2)
    return d
  
  def __eq__(self, other):
      epsilon = 10**-3
      dx = abs(self.x - other.x)
      dy = abs(self.y - other.y)
      return dx < epsilon and dy < epsilon

@dataclass
class Linea:
  A: float
  B: float
  C: float
  tipo: str 
  def __init__(self, p1, p2):
    self.A = p1.y - p2.y
    self.B = p2.x - p1.x
    self.C = p2.y * p1.x - p1.y * p2.x

  def __repr__(self):
    return f"A:{self.A}, B:{self.B}, C:{self.C}, tipo:{self.tipo}"

  def __eq__(self, other):
    #Revisar que A no sea igual a 0
    if self.A != 0 and other.A != 0:
      dif = self.A / other.A
    #Si A es igual a 0, usamos B
    else:
      dif = self.B / other.B
    return self.A / dif == other.A and self.B / dif == other.B and self.C / dif == other.C

def acepta_listas(f):
  def inner(parametro, *args, **kwargs):
    if type(parametro) == list:
      for elemento in parametro:
        f(elemento, *args, **kwargs)
    else:
      f(parametro, *args, **kwargs)
  return inner

@acepta_listas
def graficarPunto(p:Punto, *args, **kwargs):
  x=p.x
  y=p.y
  plt.scatter(x,y, *args, **kwargs, color='red', marker='*')

def graficarLinea(p1,p2,isShiny):
  if(isShiny):
    plt.plot([p1.x,p2.x],[p1.y,p2.y], color='orange')
  else:
    plt.plot([p1.x,p2.x],[p1.y,p2.y], color='black')

#####FUNCTIONS#####
def pendiente(x1,x2,y1,y2):
  return (y2-y1)/(x2-x1)

def getX2(x1,y1,y2,m):
  return ((y2-y1)/m)+x1

#####INPUTS#####
pts = []

with open('1.in','r') as file:
    for l in file:
        x, y = l.split(" ")
        pts.append(Punto(int(x),int(y)))

casos = len(pts)
#####SORT LIST#####
pts.sort(key=lambda punto:punto.x)

#####DRAW LINES#####
for i in range(casos-1): graficarLinea(pts[i],pts[i+1],0)

#####DRAW HIGHER POINTS#####
for i in range(1,casos-1, 2): graficarPunto(pts[i])

#####DRAW SUNNY LINES#####
revPts = pts[::-1]

graficarLinea(revPts[0], revPts[1], 1)
m = pendiente(revPts[1].x, revPts[0].x, revPts[1].y, revPts[0].y)
ptAlto = Punto(revPts[1].x, revPts[1].y)

for i in range(1,casos-1):
  if revPts[i].y > ptAlto.y:
    m = pendiente(revPts[i-1].x, revPts[i].x,revPts[i-1].y,revPts[i].y)
    newPt = Punto(getX2(revPts[i].x, revPts[i].y, ptAlto.y, m), ptAlto.y)
    graficarLinea(newPt, revPts[i], 1)
    ptAlto= Punto(revPts[i].x, revPts[i].y)


font1 = {'family':'serif','color':'orange','size':14}
plt.title("El Rubor del Amanecer\nRosita Aguirre, Lucia Castañeda & Eduardo González", fontdict=font1)
plt.grid(axis = 'y')
plt.show()
import numpy as np 
import pylab as pl 
from tools.line_style import Color
from tools.axis import Axis 


class Grad : 
	def __init__(self,col = Color()):
		self._params = {"color" : col.green()}
	def getParam(self):
		return self._params
	def getColor(self):
		return self.getParam().values()

	def setParam(self,p):
		self._params = p
	def plot(self,mod1,xaxis,yaxis):
		xstr = xaxis.getDebut()
		xend = xaxis.getFin()
		xmsh = xaxis.getnbPoint()
		ystr = yaxis.getDebut()
		yend = yaxis.getFin()
		ymsh = yaxis.getnbPoint()
		X, Y = np.mgrid[xstr:xend:xmsh, ystr:yend:ymsh]
		xGrad = mod1.getGrad(X,Y)[0]
		yGrad = mod1.getGrad(X,Y)[1]
		couleur = self.getColor()
		return pl.quiver(X,Y,xGrad,yGrad,color = couleur)

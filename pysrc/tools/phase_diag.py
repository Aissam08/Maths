import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from tools.grad import Grad


class PhaseDiag :
	def __init__(self,title="Portrait des phases",figsize =(10,6)):
		self._title = title
		self._figsize = figsize
	def __str__(self):
		return self._title
# -- Public getters
	def getTitle(self):
		return self._title
	def getFigsize(self):
		return self._figsize
# -- Public setters
	def setTitle(self,t):
		self._title = t

	def setFigsize(self,f):
		self._figsize = f 
# -- Public methods
	def portrait(self,modl,cndszr,xaxis,yaxis,taxis,exprtpng = False ,showfield = True) :
		# -- Preparer graphique
		fig,phases =plt.subplots(figsize = self.getFigsize())

		# -- Parametrage graphique globaux
		plt.xlim(xaxis.getDebut(),xaxis.getFin())
		plt.ylim(yaxis.getDebut(),yaxis.getFin())

		# -- Parametrage repere
		phases.grid(True)
		phases.set_title(self.getTitle())
		phases.set(xlabel=xaxis.getLabel(),
		ylabel=yaxis.getLabel())

		# -- Calcul des trajectoires
		tdisc = np.linspace(taxis.getDebut(),
			taxis.getFin(),
			taxis.getnbPoint())

		cndszero = cndszr.getIni()

		for cnd in cndszero :
			cnd0 = cnd.getCoord()
			trj = odeint(modl.getSystm(),cnd0,tdisc)
			phases.plot(trj[:,0],trj[:,1],cnd.getParam())
		# --
		# -- Champ des gradients
		
		if showfield :
			field = Grad()
			field.plot(modl,xaxis,yaxis)
			#plt.show()

		if exprtpng :
			figname = self.getTitle()+".png"
			figname = figname.replace(" ","_")
			fig.savefig(figname)

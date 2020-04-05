from tools.line_style import *




#======================Classe Initial======================#

class Initial : 
	def __init__(self,c,p):
		self._coord = c
		self._param = p

	def getCoord(self):
		return self._coord
	def getParam(self):
		return self._param

	def setCoord(self,co):
		self._coord = co

	def setParam(self,pa):
		self._param = pa

	def styli(self): 
		for c,f in self.getParam():
			return ""+c+f+""
#==========================Classe Initials=====================#
class Initials :
	def __init__(self):
		self._ini = []
	def getIni(self):
		return self._ini
	def setIni(self,ino):
	 	self._ini = ino

	def genCond(self,Lx,Ly,c):
	 	for i in Lx:
	 		for j in Ly:
	 			self._ini.append(Initial((i,j),c.style()))

	def addCond(self,co,st):
		self._ini.append(Initial(co,st.style()))

##On crée une liste d'instance de Initial vide.
#On crée une instance de Initials contenant cette liste, on y ajoute les éléments I
#Le style est défini ave 'b-' de base
#ini.Initial((0,0),{'b':'-'})]
"""
I = []
L1 = [1,2,3]
L2 = [5,4]
Init = Initials(I)
Init.genCond(L1,L2,blue_solid)
op = (1,0)

for a in Init.getIni():
	print("Coord : "+str(a.getCoord())+" style : "+str(a.getParam()))

Init.addCond(op,black_dash)
Init.addCond((4,3),red_dot)
Init.addCond((2,1),yellow_solid)
print("\nCoord après ajout\n")
for a in Init.getIni():
	print("Coord : "+str(a.getCoord())+" style : "+str(a.getParam()))
"""
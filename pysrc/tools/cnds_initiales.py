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

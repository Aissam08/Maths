import numpy as np 
import matplotlib.pyplot

class Axis:
	# Classe des axes
	def __init__(self,d,f,nbP,l):
		self.__debut = d
		self.__fin = f
		self.__nbPoints = nbP
		self.__label = l
	def setDebut(self,n):
		self.__debut = n
	def setFin(self,n):
		self.__fin = n
	def setnbPoint(self,n):
		self.__nbPoints= n
	def setLabel(self,lb):
		self.__label = lb
	def getDebut(self):
		return self.__debut
	def getFin(self):
		return self.__fin
	def getnbPoint(self):
		return self.__nbPoints
	def getLabel(self):
		return self.__label


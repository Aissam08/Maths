

#===================Déclaration de classe=======================#

#===============FORM=================#

class Form: 
	def __init__(self):
		self._forms = {"line" : '-',
		"tirets" : '--',
		"tiretP" : '-.',
		"points" : ':',
		"rien" : ' '
		}
	def getLine(self):
		return self._forms["line"]
	def getDash(self):
		return self._forms["tirets"]
	def getDdsh(self):
		return self._forms["tiretP"]
	def getDot(self):
		return self._forms["points"]
	def getR(self):
		return self._forms["rien"]

#=============COLOR====================#

class Color:
	def __init__(self):
		self._colors = { "blue" : "b" ,
						"red" : "r" ,
						"black" : "k" ,
						"cyan" : "c" ,
						"green" : "g" ,
						"magenta" : "m" ,
						"yellow" : "y",
						"white" : "w"}
	def blue(self):
		return self._colors["blue"]
	def red(self) :
		return self._colors["red"]
	def black(self):
		return self._colors["black"]
	def cyan(self):
		return self._colors["cyan"]
	def green(self):
		return self._colors["green"]
	def magenta(self):
		return self._colors["magenta"]
	def yellow(self):
		return self._colors["yellow"]
	def white(self):
		return self._colors["white"]

#==================STYLE================#

class LineStyle : 
	def __init__(self,f,c):
		self._form = f
		self._color = c
	def getForm(self):
		return self._form
	def getColor(self):
		return self._color
	def setForm(self,fo):
		self._form = fo
	
	def setColor(self,col):
		self._color=col

	def style(self): 
		return ""+self.getColor()+self.getForm()+""

#=======================Création des instances========================#
"""
black_solid = LineStyle(Color().black(),Form().getLine())
black_dash = LineStyle(Color().black(),Form().getDash())
black_dot = LineStyle(Color().black(),Form().getDot())
black_ddsh = LineStyle(Color().black(),Form().getDdsh())

red_solid = LineStyle(Color().red(),Form().getLine())
red_dash = LineStyle(Color().red(),Form().getDash())
red_dot = LineStyle(Color().red(),Form().getDot())
red_ddsh = LineStyle(Color().red(),Form().getDdsh())


green_solid = LineStyle(Color().green(),Form().getLine())
green_dash = LineStyle(Color().green(),Form().getDash())
green_dot = LineStyle(Color().green(),Form().getDot())
green_ddsh = LineStyle(Color().green(),Form().getDdsh())


cyan_solid = LineStyle(Color().cyan(),Form().getLine())
cyan_dash = LineStyle(Color().cyan(),Form().getDash())
cyan_dot = LineStyle(Color().cyan(),Form().getDot())
cyan_ddsh = LineStyle(Color().cyan(),Form().getDdsh())


yellow_solid = LineStyle(Color().yellow(),Form().getLine())
yellow_dash = LineStyle(Color().yellow(),Form().getDash())
yellow_dot = LineStyle(Color().yellow(),Form().getDot())
yellow_ddsh = LineStyle(Color().yellow(),Form().getDdsh())

magenta_solid = LineStyle(Color().magenta(),Form().getLine())
magenta_dash = LineStyle(Color().magenta(),Form().getDash())
magenta_dot = LineStyle(Color().magenta(),Form().getDot())
magenta_ddsh = LineStyle(Color().magenta(),Form().getDdsh())


blue_solid = LineStyle(Color().blue(),Form().getLine())
blue_dash = LineStyle(Color().blue(),Form().getDash())
blue_dot = LineStyle(Color().blue(),Form().getDot())
blue_ddsh = LineStyle(Color().blue(),Form().getDdsh())
"""
class Cellule:
	def __init__(self, v, s):
		self.valeur = v
		self.suivant = s


class Pile:
	def __init__(self):
		self.sommet = None

	def estVide(self):
		return self.sommet is None

	def empiler(self, v):
		self.sommet = Cellule(v, self.sommet)

	def depiler(self):
		if self.estVide():
			raise ValueError("La pile est vide")
		else:
			v = self.sommet.valeur
			self.sommet = self.sommet.suivant
			return v

	def __repr__(self):
		if self.estVide():
			return "Pile vide"
		else:
			s = "Pile : \n"
			p = self.sommet
			while p is not None:
				s += str(p.valeur) + "\n"
				p = p.suivant
			return s
			

class File:
	def __init__(self):
		self.premier = None

	def estVide(self):
		return self.premier == None

	def defiler(self):
		if self.estVide():
			raise ValueError("La file est vide")
		else:
			v = self.premier.valeur
			self.premier.valeur = self.premier.suivant
			return v
	
	def emfiler(self, v):
		if self.estVide:
			self.premier = Cellule(v, None)
		else:
			premier = self.premier
			while not premier.suivant is None:
				premier = premier.suivant
			premier= Cellule(v, None)

	def __repr__(self):
		if self.estVide():
			return "File Vide"
		else:
			texte = ""
			valeur = self.premier
			while not valeur is None:
				texte = str(valeur.valeur) + "---->" + texte
				valeur = valeur.suivant
			return texte
				
				

a = File()
a.emfiler(4)
a.emfiler(5)
a.emfiler(6)
a.emfiler(7)
a.emfiler(8)
print(a.premier.suivant)


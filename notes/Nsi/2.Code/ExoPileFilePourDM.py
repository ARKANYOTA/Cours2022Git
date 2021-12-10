class Cellule:
    def __init__(self,v,s):
        self.val = v
        self.suiv = s

    '''def __repr__(self):
      txt="|"+str(self.val)+"|"
      if self.suiv is None:
         txt=txt+"X|"      
      else:
         txt=txt+"--> "
      return txt
    '''
#---------  La Pile -----------
class Pile:
    def __init__(self):
       self.sommet = None
       self.taille=0

    def estVide(self):
        return self.sommet is None

    def valeurSommet(self):
        return self.sommet.val

    def empiler(self,x):
        C=Cellule(x,self.sommet)
        self.sommet=C
        

    def depiler(self):
        x=self.sommet.val
        self.sommet=self.sommet.suiv
        return x
   
    def __len__(self):
        return self.taille
    
    def __repr__(self):
        if self.estVide():
          return "Pile vide"
        else:
          S=self.sommet
          txt=""
          while not S is None:
            x=S.val
            txt=txt+"\n"+str(x)
            S=S.suiv
          return txt

#---------  La File -----------
class File:
    def __init__(self):
       self.premier = None
       self.taille=0

    def estVide(self):
        return self.premier is None

    def valeurSommet(self):
        return self.premier.val         

    def enfiler(self,x): # met l'élément au "fond"
        if self.estVide():# si file vide
           self.premier=Cellule(x,None) 
        else:
           cel_active=self.premier
           while not cel_active.suiv is None:
               cel_active=cel_active.suiv
           cel_active.suiv=Cellule(x,None)          

    def defiler(self):
        x=self.premier.val
        self.premier=self.premier.suiv
        return x
   
    def __len__(self):
        return self.taille
 
    def __repr__(self):
        if self.estVide():
            return "File vide"
        else:
            txt=str(self.premier.val)
            reste_file=self.premier.suiv
            while not reste_file is None:
                x=reste_file.val
                txt=str(x)+"-->"+txt
                reste_file=reste_file.suiv
        return txt  



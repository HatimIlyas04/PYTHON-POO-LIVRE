from datetime import datetime , date

class Livre :
    def __init__(self,titre=None , auteur=None ,anneePub=None ,eduteur=None,nombrePage=None,prix=None,fournisseur=None,):
        self.__auteur=auteur        
        self.__titre=titre
        self.__anneePub=anneePub
        self.__eduteur=eduteur
        self.__nombrePage=nombrePage
        self.__prix=prix
        self.__fournisseur=fournisseur
         
    #setter and getter--------------------------------------------------------------------------------------------------
         
    def getTitre(self):
         return self.__titre
    def setTitre(self, value):
        self.__titre=value

    def getAuteur(self):
         return self.__auteur
    def setTitre(self, value):
        self.__auteur=value
        
    def getAnneePub(self):
         return self.__anneePub
    def setTitre(self, value):
        self.__anneePub=value
        
    def getEduteur(self):
         return self.__eduteur
    def setTitre(self, value):
        self.__eduteur=value
        
    def getNombrePage(self):
         return self.__nombrePage
    def setTitre(self, value):
        self.__nombrePage=value  
        
    def getPrix(self):
         return self.__prix
    def setTitre(self, value):
        self.__prix=value 
        
    def getFournisseur(self):
         return self.__fournisseur
    def setTitre(self, value):
        self.__fournisseur=value   
        
    #  methode------------------------------------------------------------------------------------------------------------------------------
    def afficher(self):
        print("L auteur :", self.__auteur) 
        print("Le titre :", self.__titre)
        print ("La date de publication :", self.__anneePub)
        print("Editeur  :", self.__eduteur)
        print ("Le nombre de page :" ,self.__nombrePage)
        print ("Le prix  :" , self.__prix)
        print ("Le fournisseure:",self.__fournisseur)
    
L1 = Livre("the blue bird", "ilyas", 2017-1-2,"toto",177,12000,"ilyas")
L1.afficher()
        
   
                
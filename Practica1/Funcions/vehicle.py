class vehicle:
    def __init__(self,color,marca,model,anyo,velocitat,preu):
        self.color = color
        self.marca = marca
        self.model = model
        self.anyo = anyo
        self.velocitat = velocitat
        self.preu = preu
    #GETTERS I SETTERS
    def getColor(self):
        return self.color
    def setColor(self):
        self.color = color
    def getMarca(self):
        return self.marca
    def setMarca(self):
        self.marca = marca
    def getModel(self):
        return self.model
    def setModel(self):
        self.model = model
    def getAnyo(self):
        return self.anyo
    def steAnyo(self):
        self.anyo = anyo
    def getVelocitat(self):
        return self.velocitat
    def setVelocitat(self):
        self.velocitat = velocitat
    def getPreu(self):
        return self.preu
    def setPreu(self):
        self.preu = preu
    #FI DE GETTERS I SETTERS
    def to_dict(self):
        return {
            "color": self.color,
            "marca": self.marca,
            "model": self.model,
            "anyo": self.anyo,
            "velocitat": self.velocitat,
            "preu": self.preu
        }
    def parts(self):
        print(f"El meu color es el {self.color}, la meva marca es {self.marca}, el meu model es {self.model}, soc del {self.anyo}, la meva velocitat es de {self.velocitat} i costo {self.preu}")
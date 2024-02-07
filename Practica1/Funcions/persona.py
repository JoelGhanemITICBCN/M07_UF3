class persona:
    def __init__(self,edat,altura,pes,iq,origen,color_ulls):
        self.edat = edat
        self.altura = altura
        self.pes = pes
        self.iq = iq
        self.origen = origen
        self.color_ulls = color_ulls
    #GETTERS I SETTERS#
    def getEdat(self):
        return self.edat
    def setEdat(self):
        self.edat = edat
    def getAltura(self):
        return self.altura
    def setAltura(self):
        self.altura = altura
    def getPes(self):
        return self.pes
    def setPes(self):
        self.pes = pes
    def getIq(self):
        return self.iq
    def setIq(self):
        self.iq = iq
    def getOrigen(self):
        return self.origen
    def setOrigen(self):
        self.origen = origen
    def getColor(self):
        return self.color_ulls
    def setColor(self):
        self.color_ulls = color_ulls
    #FI DELS GETTERS I SETTERS
    def nomSalutacio(self):
        print(f"Tinc {self.edat}, soc de {self.origen}, la meva altura es {self.altura}, peso {self.pes}, el meu IQ es de {self.iq} i el color dels meus ulls es el {self.color_ulls}")
    def to_dict(self):
        return {
            "edat": self.edat,
            "altura": self.altura,
            "pes": self.pes,
            "iq": self.iq,
            "origen": self.origen,
            "color_ulls": self.color_ulls
        }
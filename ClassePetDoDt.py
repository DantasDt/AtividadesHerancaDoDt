import os
os.system("cls")
class Pet:
    def __init__(self, nome, humor):
        self._nome = nome
        self._humor = humor
    
    def mostrarStatus(self):
        print("Nome do Pet", self._nome)
        print(self._nome, "está com o humor: ", self._humor)
    
    def brincar(self):
        self._humor += 1
        return self._humor
    
class Dragao(Pet):
    def __init__(self, nome, humor, nivelFogo):
        super().__init__(nome, humor)
        self.__nivelFogo = nivelFogo

    def SoltarFogo(self):
        self.__nivelFogo += 1
        self._humor -= 1
        return self.__nivelFogo and self._humor
    
    def mostrarStatusDragao(self):
        super().mostrarStatus()
        print("Nível de Fogo de", self._nome, self.__nivelFogo)
    
class CaoRobo(Pet):
    def __init__(self, nome, humor, CargaBateria):
        super().__init__(nome, humor)
        self.__CargaBateria = CargaBateria
    
    def Recarregar(self, valor):
        if valor != 100:
            self.__CargaBateria = 100
            return self.__CargaBateria
        
    def mostrarStatusCaoRobo(self):
        super().mostrarStatus()
        print("Nível da bateria de", self._nome, self.__CargaBateria)

import os
os.system("cls")
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo
    
    def deposita(self, valor):
        self._saldo += valor
        return self._saldo
    
    def saca(self, valor):
        if self._saldo > valor:
            self._saldo -= valor
        else:
            print("Valor inválido para depósito!")
        return self._saldo
    
class Poupanca(Conta):
    def __init__(self, saldo, taxaRend):
        super().__init__(saldo)
        self.__taxaRend = taxaRend
        
    def Render(self):
        self._saldo += (self._saldo * self.__taxaRend)
        return self._saldo

class ContaEspecial(Conta):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.__limite = limite

    def sacar(self, valor):
        if self._saldo < valor:
            x = valor - self._saldo
            self._saldo = 0
            self.__limite -= x
        else:
            self._saldo -= valor
        return self._saldo and self.__limite
    
    def limite(self):
        return self.__limite

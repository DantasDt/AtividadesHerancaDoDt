import os
from ClasseConta import ContaEspecial, Poupanca
obj = Poupanca
obj2 = ContaEspecial
while True:
    x = str(input("Oque deseja fazer? "))
    x = x.lower()
    if x == "acessar":
        os.system("cls")
        y = str(input("Informe o seu tipo de conta: "))
        y = y.lower()
        if y == "conta especial":
            saldo = float(input("Informe seu saldo: "))
            limite = float(input("Informe seu limite: "))
            obj2 = ContaEspecial(saldo, limite)

        elif y == "poupanca":
            saldo = float(input("Informe seu saldo: "))
            taxaRend = float(input("Informe a taxa de rendimento: "))
            obj = Poupanca(saldo, taxaRend)
    elif x == "sacar":
        if y == "conta especial":
            valor = float(input("Informe o valor: "))
            obj2.sacar(valor)
            
        elif y == "poupanca":
            valor = float(input("Informe o valor: "))
            obj.saca(valor)
    elif x == "render":
        obj.Render()
# Ainda não finalizado!

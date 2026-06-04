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
            os.system("cls")
            saldo = float(input("Informe seu saldo: "))
            limite = float(input("Informe seu limite: "))
            obj2 = ContaEspecial(saldo, limite)

        elif y == "poupanca":
            os.system("cls")
            saldo = float(input("Informe seu saldo: "))
            taxaRend = float(input("Informe a taxa de rendimento: "))
            obj = Poupanca(saldo, taxaRend)
    elif x == "sacar":
        if y == "conta especial":
            os.system("cls")
            valor = float(input("Informe o valor: "))
            print("Tentativa de saque efetuado!")
            print("Seu novo saldo é de: ", obj2.sacar(valor))
            print("Seu limite agora é de: ", obj2.limite())
        else:
            os.system("cls")
            valor = float(input("Informe o valor: "))
            print("Tentativa de saque efetuado!")
            print("Seu novo saldo é de: ", obj.saca(valor))
    elif x == "render":
        os.system("cls")
        print("Rendimento mensal adicionado ao seu saldo!")
        print("Novo saldo: ", obj.Render())
# Finalizado

import os 
os.system("cls")
from ClassePetdoDt import Dragao, CaoRobo
obj = CaoRobo
obj2 = Dragao
while True:
    x = str(input("Oque deseja fazer? "))
    x = x.lower()
    if x == "cadastrar":
        os.system("cls")
        y = str(input("Informe o tipo do pet: "))
        y = y.lower()
        if y == "dragao":
                nome = str(input("Informe o nome do pet: "))
                humor = int(input("Informe o humor do pet: "))
                nivelFogo = int(input("Informe o nivel de fogo do pet: "))
                obj2 = Dragao(nome, humor, nivelFogo)
        elif y == "caorobo":
                nome = str(input("Informe o nome do pet: "))
                humor = int(input("Informe o humor do pet: "))
                nivelBateria = int(input("Informe o nivel da bateria do pet: "))
                obj = CaoRobo(nome, humor, nivelBateria)
    elif x == "brincar":
        os.system("cls")
        if y == "dragao":
            obj2.brincar()
        elif y == "caorobo":
              obj.brincar()
        print("O pet brincou e seus humor melhorou!")
    
    elif x == "mostrar":
            os.system("cls")
            if y == "dragao":
                  obj2.mostrarStatusDragao()
            else:
                  obj.mostrarStatusCaoRobo()
    
    elif x == "soltar fogo":
          os.system("cls")
          obj2.SoltarFogo()
    
    elif x == "recarregar":
          os.system("cls")
          bateria = int(input("Informe a Bateria do Cão Robo: "))
          obj.Recarregar(bateria)
    else: 
        if x == "sair":
            break

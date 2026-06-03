import os 
os.system("cls")
from p import Pet, Dragao, CaoRobo
obj = Pet
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
                obj = Dragao(nome, humor, nivelFogo)
        elif y == "caorobo":
                nome = str(input("Informe o nome do pet: "))
                humor = int(input("Informe o humor do pet: "))
                nivelBateria = int(input("Informe o nivel da bateria do pet: "))
                obj = CaoRobo(nome, humor, nivelBateria)
    elif x == "brincar":
        os.system("cls")
        obj.brincar()
        print("Os pets brincaram e seus humores melhoraram!")
    
    elif x == "mostrar":
            os.system("cls")
            if y == "dragao":
                  obj.mostrarStatusDragao()
            else:
                  obj.mostrarStatusCaoRobo()
    
    elif x == "soltar fogo":
          os.system("cls")
          obj.SoltarFogo()
    
    elif x == "recarregar":
          os.system("cls")
          bateria = int(input("Informe a Bateria do Cão Robo: "))
          obj.Recarregar(bateria)
    else: 
        if x == "sair":
            break

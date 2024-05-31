
print("CLASSIFICADOR DE NÍVEL DE HERÓI")
print("Por RafaelPinhoDev")
print("--------------------------------")


Nome_Heroi = input("Digite o nome do Heroi:") 
XP = int(input("Digite a quantidade de XP de " + Nome_Heroi + ": "))

if XP < 1000:
    Nivel_Heroi = "Ferro"
elif XP >= 1001 and XP <= 2000:
    Nivel_Heroi = "Bronze"
elif XP >= 2001 and XP <= 5000:
    Nivel_Heroi = "Prata" 
elif XP >= 5001 and XP <= 7000:
    Nivel_Heroi = "Ouro"
elif XP >= 7001 and XP <= 8000:
    Nivel_Heroi = "Platina"
elif XP >=  8001 and XP <= 9000:
    Nivel_Heroi = "Anscendente"
elif XP >= 9001 and XP <= 10000:
    Nivel_Heroi = "Imortal"
else:
    Nivel_Heroi = "Radiante"
    
print("O Heroí ", Nome_Heroi , "está no nível ", Nivel_Heroi)
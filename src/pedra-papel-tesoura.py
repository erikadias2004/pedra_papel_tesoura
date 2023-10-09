import random

print ("╔╦══ ⋆ ⋆ ✦ ⋅ ✩ ⋅ ✦ ⋆ ⋆ ══╦╗")
print ("         𝔹𝕖𝕞-𝕧𝕚𝕟𝕕𝕠!")
print ("╚╩══⋆ ⋆ ✦ ⋅ ✩ ⋅ ✦ ⋆ ⋆  ══╩╝")
escolha = input('''Opções disponíveis:
[0] Pedra
[1] Papel
[2] Tesoura
Escolha um para jogar: ''')
computador = random.randint(0,2)

##while escolha != 0 or escolha != 1 or escolha != 2:
##    print ('''Valor inválido! Opções disponíveis:
##[0] Pedra
##[1] Papel
##[2] Tesoura''')
##    escolha = input("Tente novamente: ")

if computador == 0:
    print ("Computador escolheu pedra!")
    if escolha == 0:
        print ("Houve um empate!")
    elif escolha == 1:
        print ("Parábens, você ganhou!")
    else:
        print ("O computador ganhou")

if computador == 1:
    print ("Computador escolheu papel!")
    if escolha == 1:
        print ("Houve um empate!")
    elif escolha == 2:
        print ("Parábens, você ganhou!")
    else:
        print ("O computador ganhou")

if computador == 2:
    print ("Computador escolheu tesoura!")
    if escolha == 2:
        print ("Houve um empate!")
    elif escolha == 0:
        print ("Parábens, você ganhou!")
    else:
        print ("O computador ganhou")
        

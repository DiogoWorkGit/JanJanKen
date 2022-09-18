import random
import time

def scisor():    
    print("   _    _")
    print("  (_)  / )")
    print("    | (_/")
    print("   _+/")
    print("  //|\\")
    print(" // ||")
    print("(/  |/")

def rock():
    print("   ____")
    print(" _/  _ \\")
    print("/ _ - _ \\")
    print("\\_______/")

def paper():
    print("    _____")
    print("   O_____O")
    print("  /     /")
    print(" /____ /") 
    print("O_____O")

def showScore(placar):
    print(f"\nVitórias: {placar[0]}\nDerrotas: {placar[1]}\nEmpates: {placar[2]}")

def numRandom():
    maquina = random.randrange(0,3)
    return maquina

def showGame(player, maquina):
    time.sleep(1)
    print("\n\nVocê: ")
    time.sleep(0.5)
    if player == 0:
        rock()
    
    elif player == 1:
        paper()
    
    else:
        scisor()
    
    time.sleep(1)
    print("\nMáquina: ")
    time.sleep(0.5)
    if maquina == 0:
        rock()
    
    elif maquina == 1:
        paper()
    
    else:
        scisor()

def jokenpo(player, maquina, placar):
    # Empates
    time.sleep(1)
    if player == 0 and maquina == 0:
        print("\nMaquina:\nDroga, empatamos 😠 (1+ Empate)")
        placar[2] = placar[2]+1
    elif player == 1 and maquina == 1:
        print("\nMaquina:\nDroga, empatamos 😠")
        placar[2] = placar[2]+1
    elif player == 2 and maquina == 2:
        print("\nMaquina:\nDroga, empatamos 😠")
        placar[2] = placar[2]+1
    
    # Vitórias
    elif player == 0 and maquina == 2:
        print("\nMaquina:\nMaldição, como é possível você ter ganhado, isso não faz sentido 😡 (1+ Vitória)")
        placar[0] = placar[0] + 1
    elif player == 1 and maquina == 0:
        print("\nMaquina:\nMaldição, como é possível você ter ganhado, isso não faz sentido 😡 (1+ Vitória)")
        placar[0] = placar[0] + 1
    elif player == 2 and maquina == 1:
        print("\nMaquina:\nMaldição, como é possível você ter ganhado, isso não faz sentido 😡 (1+ Vitória)")
        placar[0] = placar[0] + 1
        
    # Derrotas
    elif player == 0 and maquina == 1:
        print("\nMaquina:\nHA HA, Como você consegue ser tão ruim assim, meu deus, desinstala esse jogo logo 😂 (1+ Derrota)")
        placar[1] = placar[1] + 1
    elif player == 1 and maquina == 2:
        print("\nMaquina:\nHA HA, Como você consegue ser tão ruim assim, meu deus, desinstala esse jogo logo 😂 (1+ Derrota)")
        placar[1] = placar[1] + 1
    elif player == 2 and maquina == 0:
        print("\nMaquina:\nHA HA, Como você consegue ser tão ruim assim, meu deus, desinstala esse jogo logo 😂 (1+ Derrota)")
        placar[1] = placar[1] + 1

def introGame():
    print("\nMaquina:\nFique sabendo que você está interessado em jogar")
    time.sleep(3)
    print("\nMaquina:\nMas você não parece alguém que vai conseguir me ganhar mesmo se eu estiver brincando 😂 ")
    time.sleep(2)
    print ("\nMaquina:\nEntão você acha que consegue me derrotar em um jogo de Pedra, Papel e Tesoura?")
    time.sleep(2) 
    loop="on"
    while loop == "on":
        try:
            jogar = int(input("\n1. Claro que sim seu panaca, eu vou colocar teu orgulho no chão 😡 \n2. Acho que você é muito forte para ser derrotado...\n    Insira o número da alternativa: "))    
        except:
            print("\nDigite um número!!!!")
            time.sleep(1)
            continue
        time.sleep(1)
        if jogar == 1:
            print("\nMaquina:\nSe você acha que consegue, então vai ter que arcar com as consequências")
            start = "sim"
            loop = "off"
        
        elif jogar  == 2:
            print("\nMaquina:\nEntão já vai de base, perdedor 😂")
            time.sleep(1)
            exit()
            
        else:
            print("\nMaquina:\nOque você disse??? 😕 ")
            time.sleep(2)
            continue
    return start

def repitir(placar):
    print("\nQuer tentar a sua sorte denovo?")
    looop="on"
    while looop == "on":
        time.sleep(1)
        try:
            continuar = int(input("\n1. Sim\n2. Não\n    Insira o número da alternativa: "))
            time.sleep(1)
        except:
            print("\nDigite um número!!!!")
            time.sleep(1)
            continue
        if continuar == 1:
            print("\nEsse é o espirito, vamos recomeçar")
            recomeca = "sim"
            time.sleep(1)
            looop = "off"
        elif continuar == 2:
            print("\nAté mais noob")
            time.sleep(1)
            print(f"\nVitórias: {placar[0]}\nDerrotas: {placar[1]}\nEmpates: {placar[2]}")
            time.sleep(4)
            exit()
        else:
            print("Digite uma alternativa valida")
            time.sleep(1)
            continue
    return recomeca

# Vitórias = placar[0], Derrotas = placar[1], Empates = placar[2]
placar = [0,0,0]
ligado = "sim"
start = introGame()
if start == "sim":
    while ligado.lower() == "sim":
            print("\nVamos começar")
            time.sleep(2)
            print("\nJo")
            time.sleep(0.5)
            print("Ken")
            time.sleep(0.5)
            print("Po")
            time.sleep(1)

            looop="on"
            while looop == "on":
                try:
                    jogada = int(input("\n1. Pedra\n2. Papel\n3. Tesoura\n    Insira o número da alternativa: "))
                except:
                    print("\nDigite um número!!!!")
                    time.sleep(1)
                    continue
                jogada = jogada - 1
                if jogada >=0 and jogada <=2:
                    maquina = numRandom()
                    showGame(jogada, maquina)
                    jokenpo(jogada, maquina, placar)
                    showScore(placar)
                    looop="off"
                else:
                    print("Digite uma alternativa valida")
                    time.sleep(1)
                    continue
            recomecar = repitir(placar)
            if recomecar == "sim":
                continue
            
        
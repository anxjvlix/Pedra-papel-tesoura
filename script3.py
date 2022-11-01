import random

def play():
    user = input("Escolha um: P para pedra, Pa para papel e T para tesoura\n")
    computer = random.choice(['P', 'Pa', 'T'])

    if user == computer:
        return 'Foi um empate'

# P>T, T>Pa, Pa>P 

    if is_win(user, computer):
        return 'Você Ganhou!'

       
    return 'Você perdeu!'

def is_win( jogador, oponente):
    #return true if jogador wins 
    # P>T, T>Pa, Pa>P 
    if (jogador == 'P' and oponente == 'T') or (jogador == 'T' and oponente == 'Pa') or (jogador == 'Pa' and oponente == 'P'):
        return True 

print(play())
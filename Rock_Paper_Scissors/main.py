from random import choice

# Clássico jogo: pedra, papel e tesoura

computer = choice([1, 2, 3])
def play(opponent):
    # O parâmetro de player recebe o argumento (computer)

    user = int(input("[1]Pedra\n[2]Papel\n[3]Tesoura\nEscolha(1, 2 ou 3): "))
    
    if user == opponent:
        return "É um empate."

    if is_win(user, opponent):
        return "Você ganhou!"

    return "Você perdeu!"

        
def is_win(player, opponent):
    # Lógica que retornará "True" caso o player sempre vença

    if (player == 1 and opponent == 3) or (player == 3 and opponent == 2)\
        or (player == 2 and opponent == 1):
        return True


def message(opponent):
    # O parâmetro de message recebe o argumento (computer)
    # A função irá retornar formatado o argumento recebido

    if opponent == 1:
        return f"O computador escolheu: Pedra"
    
    elif opponent == 2:
        return f"O computador escolheu: Papel"
    
    elif opponent == 3:
        return f"O computador escolheu: Tesoura"
        

print(play(computer))
print(message(computer))

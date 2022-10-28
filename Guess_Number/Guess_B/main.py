from random import randint

# O parâmetro da função "computer_guess" recebe o argumento (10)
# O computador deve acertar o número escolhido pelo usuário, sabendo que o limite está no argumento (10)


def computer_guess(value):
    low = 1
    high = value
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = randint(low, high)
        else:
            guess = low  # Evitar o erro, caso low e high sejam o mesmo número

        feedback = input(f"É {guess} muito alto (H), muito baixo (L), ou correto (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Uau! O computador adivinhou seu número, {guess}, corretamente!")


computer_guess(10)

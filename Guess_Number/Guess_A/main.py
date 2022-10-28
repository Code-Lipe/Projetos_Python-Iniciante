from random import randint

# O parâmetro da função "guess" recebe o argumento (10)
# O usuário deve acertar o número recebido pelo computador (1 a 10)

def guess(value):
    random_number = randint(1, value)
    user_guess = 0

    while user_guess != random_number:
        user_guess = int(input(f"Adivinhe um número entre 1 e {value}: "))

        if user_guess < random_number:
            print("Desculpe, tente novamente. Muito baixo.")
        elif user_guess > random_number:
            print("Desculpe, tente novamente. Muito alto.")

    print(f"Uau, parabéns. Você adivinhou o número {random_number} corretamente!")


guess(10)

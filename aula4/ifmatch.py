# Pedir um número e associar esse número a um dia da semana => se digitar 1 = domingo, 2 = segunda ...
num = int(input("Digite um número de 1 a 7: "))
#
# if num == 1:
#     print("Domingo")
# elif num == 2:
#     print("Segunda-feira")
# elif num == 3:
#     print("Terça-feira")
# elif num == 4:
#     print("Quarta-feira")
# elif num == 5:
#     print("Quinta-feira")
# elif num == 6:
#     print("Sexta-feira")
# elif num == 7:
#     print("Sábado")
# else:
#     print("Não é um número de 1 a 7")
# ==========================================
# match/case
#
match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Dia inválido")


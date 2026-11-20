# 1. Vários valores no mesmo case com | (lê-se "ou")
# dia = int(input("Digite um dia da semana (1 a 7): ")) 
# #
# match dia:
#     case 1 | 7:
#         print("Fim de semana")
#     case 2 | 3 | 4 | 5 | 6:
#         print("Dia útil")
#     case _:
#         print("Dia inválido")
#======================================================
# 2. Match com texto - Calculadora
operacao = input("Operação (+, -, *, /, %): ")
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
#
match operacao:
    case "+":
        print(f"Resultado: {a + b}")
    case "-":
        print(f"Resultado: {a - b}")
    case "*":
        print(f"Resultado: {a * b}")
    case "/":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Não é possível dividir por zero!")
    case "%":
        print(f"Resultado: {(a / 100) * b}")
    case _:
        print("Operação inválida")
#-------------- Quando usar match/case ou if/elif/else? ---------------
# match/case: Comparar UMA variável com VÁRIOS valores fixos. (menu, códigos, dias, meses)
# if/elif/else: faixas e condições (média >= 7, idade <18, estudante ou não)
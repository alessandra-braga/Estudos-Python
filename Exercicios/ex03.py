#Diversas brincadeiras indígenas tradicionais são realizadas em ambientes específicos, 
# como a água, o campo aberto ou em rodas organizadas em salas fechadas. 
# A escolha correta do ambiente é fundamental para preservar o significado cultural 
# da brincadeira e garantir a segurança dos participantes.

'''Escreva um programa que:

    Leia um número: 1,2 ou 3
    Caso o número lido seja 1, imprima “ÁGUA”
    Caso o número lido seja 2, imprima “CAMPO”
    Caso o número lido seja 3, imprima “SALA”
    Caso o número lido seja diferente de 1, 2 ou 3, imprima “aAMBIENTE INVÁLIDO”

ENTRADAS:
    Um número inteiro que representa o ambiente no qual a brincadeira será realizada

SAÍDAS:
    Se o valor for 1, imprima: “ÁGUA"
    Se o valor for 2, imprima: “CAMPO”
    Se o valor for 3, imprima: “SALA”
    Para qualquer outro valor, imprima: “AMBIENTE INVÁLIDO”'''

ambiente = int(input("Digite um número: "))
if ambiente == 1:
    print("ÁGUA")
elif ambiente == 2:
    print("CAMPO")
elif ambiente == 3:
    print("SALA")
else:
    print("AMBINETE INVÁLIDO")
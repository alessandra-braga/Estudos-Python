#Na cultura Dagomba, grupo étnico da África Ocidental, os griots são responsáveis por
#preservar histórias e ensinamentos transmitidos oralmente de geração em geração. 
#Em algumas comunidades, apenas pessoas que atingem uma idade mínima podem atuar como guardiões da memória.

"""
Escreva um programa que verifique se um griot está apto a assumir essa função.

Entradas:
    Dois valores inteiros:
        Idade do griot.
        Idade mínima exigida pela comunidade.

SaídaS:
    Exibir "GRIOT APTO" se a idade do griot for maior ou igual à idade mínima.
    Exibir "GRIOT NÃO APTO" caso contrário."""

idade_griot = int(input("Digite a idade do griot: "))
idade_minima = int(input("Informe a idade mínima exigida: "))
diferenca = idade_griot - idade_minima

if diferenca >= 0:
    print("GRIOT APTO")
else:
    print("GRIOT NÃO APTO")
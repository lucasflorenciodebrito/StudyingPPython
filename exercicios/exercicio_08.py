"""
Faça um programa que receba a data de nascimento (15/07/87) e imprima

Você nasceu em <dia> de <mês> de <ano>

"""


resposta = input('Qual sua data de nascimento?  ')
# 06/03/1993

dia, mes, ano = resposta.split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}')
"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre do mais barato.
"""
preco1 = float(input("Preço 1: "))
preco2 = float(input("Preço 2: "))
preco3 = float(input("Preço 3: "))

if preco1 > preco2 and preco2 > preco3:
	print("Compre o produto 3")
elif preco2 > preco1 and preco1 < preco3:
	print("Compre o produto 1")
elif preco3 > preco1 and preco1 > preco2:
	print("Compre o produto 2")







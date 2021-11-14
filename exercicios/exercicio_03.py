#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total
print ("Olá, posso calcular quanto de tinta você precisará para a reforma?")
area = int (input("Para isso me diga o tamanho da area em m² que você quer pintar: "))
litros = (area / 3)
if(litros%18) == 0:
    lata = (litros/18)
else:
    lata = ((litros//18) + 1)
valor_total = (lata*80)
print (f"vai ser necessário {lata} lata(s) de tinta, que custará {valor_total} reais")
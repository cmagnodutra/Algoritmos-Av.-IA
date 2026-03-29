# Dado um array onde cada posição representa o preço de uma ação em um dia, encontre o maior lucro possível comprando em um dia e vendendo em outro posterior. 
# Se não for possível obter lucro, retorne 0.

print("\033[96m=== Best Time to Buy and Sell Stock ===\033[0m")
print("Dado um array de preços, retorna o maior lucro possível comprando e vendendo uma vez.")
print()

entrada = input("Digite os preços separados por espaço: ")
prices = list(map(int, entrada.split()))

min_preco = float('inf')
max_lucro = 0

for preco in prices:
    if preco < min_preco:
        min_preco = preco
    elif preco - min_preco > max_lucro:
        max_lucro = preco - min_preco

print(f"\nPreços: {prices}")
print(f"Menor preço para comprar: {min_preco}")
print(f"Maior lucro possível: {max_lucro}")
# Dado um array de temperaturas diárias, retorne um array onde cada posição indica quantos dias você precisa esperar até uma temperatura mais alta.
# Se não houver, coloque 0.

print("\033[96m=== Daily Temperatures ===\033[0m")
print("Para cada dia, quantos dias até a próxima temperatura mais alta?")
print()

entrada = input("Digite as temperaturas separadas por espaço: ")
temps = list(map(int, entrada.split()))

resultado = [0] * len(temps)
pilha = []

for i, temp in enumerate(temps):
    while pilha and temps[pilha[-1]] < temp:
        idx = pilha.pop()
        resultado[idx] = i - idx
    pilha.append(i)

print(f"\nTemperaturas: {temps}")
print(f"Dias de espera: {resultado}")
print()
for i in range(len(temps)):
    if resultado[i] == 0:
        print(f"  Dia {i+1} ({temps[i]}°): sem dia mais quente depois")
    else:
        print(f"  Dia {i+1} ({temps[i]}°): espera {resultado[i]} dia(s) → dia {i+1+resultado[i]} ({temps[i+resultado[i]]}°)")
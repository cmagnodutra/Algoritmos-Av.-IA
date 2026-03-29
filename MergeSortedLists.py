# Dadas duas listas encadeadas ordenadas, combine-as em uma única lista também ordenada.
# Torne a cabeça da nova lista.

print("\033[96m=== Merge Two Sorted Lists ===\033[0m")
print("Une duas listas ordenadas em uma só, mantendo a ordem.")
print()

entrada1 = input("Digite a primeira lista ordenada (ex: 1 3 5): ")
entrada2 = input("Digite a segunda lista ordenada (ex: 2 4 6): ")

lista1 = list(map(int, entrada1.split()))
lista2 = list(map(int, entrada2.split()))

resultado = []
i, j = 0, 0

while i < len(lista1) and j < len(lista2):
    if lista1[i] <= lista2[j]:
        resultado.append(lista1[i])
        i += 1
    else:
        resultado.append(lista2[j])
        j += 1

resultado += lista1[i:]
resultado += lista2[j:]

print(f"\nLista 1: {' -> '.join(map(str, lista1))} -> None")
print(f"Lista 2: {' -> '.join(map(str, lista2))} -> None")
print(f"Resultado: {' -> '.join(map(str, resultado))} -> None")
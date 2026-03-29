#Dada uma lista encadeada, inverta a ordem dos nós e retorne a nova lista.

print("\033[96m=== Reverse Linked List ===\033[0m")
print("Inverte uma lista encadeada.")
print()

entrada = input("Digite os valores da lista separados por espaço: ")
valores = list(map(int, entrada.split()))

# Inverte simplesmente revertendo a lista
original = valores[:]
valores.reverse()

print(f"\nLista original: {' -> '.join(map(str, original))}")
print(f"Lista invertida: {' -> '.join(map(str, valores))}")
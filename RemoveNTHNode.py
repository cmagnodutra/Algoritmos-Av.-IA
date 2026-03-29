#Dada uma lista encadeada, remova o n-ésimo nó a partir do final da lista e retorne a cabeça da lista atualizada.

print("\033[96m=== Remove Nth Node From End ===\033[0m")
print("Remove o N-ésimo nó a partir do final da lista.")
print()

entrada = input("Digite os valores da lista separados por espaço: ")
valores = list(map(int, entrada.split()))
n = int(input(f"Qual posição remover pelo final? (1 = último, máx {len(valores)}): "))

if n < 1 or n > len(valores):
    print("Posição inválida.")
else:
    indice = len(valores) - n
    removido = valores[indice]
    resultado = valores[:indice] + valores[indice+1:]

    print(f"\nLista original: {' -> '.join(map(str, valores))} -> None")
    print(f"\033[91mRemovendo posição {n} pelo final: valor {removido}\033[0m")
    print(f"\033[92mResultado: {' -> '.join(map(str, resultado))} -> None\033[0m")
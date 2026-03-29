#  Dada a cabeça de uma lista encadeada, determine se existe um ciclo nela.
# Um ciclo ocorre quando um nó aponta novamente para algum nó anterior.

print("\033[96m=== Linked List Cycle ===\033[0m")
print("Verifica se uma lista encadeada tem ciclo (usando fast/slow pointer).")
print()

entrada = input("Digite os valores da lista separados por espaço: ")
valores = list(map(int, entrada.split()))

tem_ciclo = input("Quer simular um ciclo? (s/n): ").strip().lower() == 's'
indice_ciclo = None

if tem_ciclo:
    indice_ciclo = int(input(f"Qual índice a cauda conecta? (0 a {len(valores)-1}): "))

# Monta a lista encadeada
class No:
    def __init__(self, val):
        self.val = val
        self.next = None

nos = [No(v) for v in valores]
for i in range(len(nos) - 1):
    nos[i].next = nos[i + 1]

if tem_ciclo and 0 <= indice_ciclo < len(nos):
    nos[-1].next = nos[indice_ciclo]

# Algoritmo de Floyd
lento = nos[0]
rapido = nos[0]
ciclo_detectado = False

for _ in range(10000):
    if not rapido or not rapido.next:
        break
    lento = lento.next
    rapido = rapido.next.next
    if lento == rapido:
        ciclo_detectado = True
        break

print(f"\nLista: {' -> '.join(map(str, valores))}")
if tem_ciclo:
    print(f"Ciclo criado: cauda conecta ao índice {indice_ciclo} (valor {valores[indice_ciclo]})")
print(f"Resultado: {'\033[92mTem ciclo!\033[0m' if ciclo_detectado else '\033[91mNão tem ciclo.\033[0m'}")
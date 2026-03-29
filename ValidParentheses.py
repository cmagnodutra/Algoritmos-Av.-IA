print("\033[96m=== Valid Parentheses ===\033[0m")
print("Verifica se os parênteses, colchetes e chaves estão balanceados.")
print()

s = input("Digite a sequência de parênteses (ex: ({[]})): ").strip()

pilha = []
pares = {')': '(', ']': '[', '}': '{'}
valido = True

for char in s:
    if char in '([{':
        pilha.append(char)
    elif char in ')]}':
        if not pilha or pilha[-1] != pares[char]:
            valido = False
            break
        pilha.pop()

if pilha:
    valido = False

print(f"\nSequência: {s}")
print(f"Resultado: {'\033[92mVálida!\033[0m' if valido else '\033[91mInválida!\033[0m'}")
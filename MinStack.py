#Implemente uma pilha que, além das operações normais (push, pop, top), também consiga retornar o menor elemento da pilha em tempo constante.

print("\033[96m=== Min Stack ===\033[0m")
print("Pilha que suporta push, pop, top e getMin em O(1).")
print()

pilha = []
pilha_min = []

def push(val):
    pilha.append(val)
    minimo = val if not pilha_min else min(val, pilha_min[-1])
    pilha_min.append(minimo)

def pop():
    if pilha:
        pilha.pop()
        pilha_min.pop()

def top():
    return pilha[-1] if pilha else None

def get_min():
    return pilha_min[-1] if pilha_min else None

def mostrar():
    print(f"  Pilha: {pilha}  |  Topo: {top()}  |  Mínimo: {get_min()}")

print("Comandos: push <numero> | pop | top | min | sair")
print()

while True:
    comando = input("> ").strip().lower()

    if comando.startswith("push"):
        partes = comando.split()
        if len(partes) == 2:
            push(int(partes[1]))
            mostrar()
        else:
            print("  Use: push <numero>")
    elif comando == "pop":
        pop()
        mostrar()
    elif comando == "top":
        print(f"  Topo: {top()}")
    elif comando == "min":
        print(f"  Mínimo: {get_min()}")
    elif comando == "sair":
        break
    else:
        print("\033[91m  Comando não reconhecido.\033[0m")
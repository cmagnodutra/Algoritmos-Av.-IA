#Dado um array de inteiros, retorne um novo array onde cada posição contém o produto de todos os elementos do array original, exceto o elemento da posição atual.
#Não utilize divisão e faça em tempo linear.

print("\033[96m=== Product of Array Except Self ===\033[0m")
print("Retorna um array onde cada posição é o produto de todos os outros elementos.")
print()

entrada = input("Digite os números separados por espaço: ")
nums = list(map(int, entrada.split()))
n = len(nums)

resultado = [1] * n

prefix = 1
for i in range(n):
    resultado[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n - 1, -1, -1):
    resultado[i] *= suffix
    suffix *= nums[i]

print(f"\nArray original: {nums}")
print(f"Resultado:      {resultado}")
print()
for i in range(n):
    outros = nums[:i] + nums[i+1:]
    print(f"\033[92m  posição {i}: {' × '.join(map(str, outros))} = {resultado[i]}\033[0m")
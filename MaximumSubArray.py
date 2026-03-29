# Dado um array de inteiros (positivos e negativos), encontre a subarray contínua com a maior soma possível e retorne essa soma.

print("\033[96m=== Maximum Subarray ===\033[0m")
print("Encontra o subarray contíguo com a maior soma (Algoritmo de Kadane).")
print()

entrada = input("Digite os números separados por espaço: ")
nums = list(map(int, entrada.split()))

max_soma = nums[0]
soma_atual = nums[0]
inicio = 0
melhor_inicio = 0
melhor_fim = 0

for i in range(1, len(nums)):
    if nums[i] > soma_atual + nums[i]:
        soma_atual = nums[i]
        inicio = i
    else:
        soma_atual += nums[i]

    if soma_atual > max_soma:
        max_soma = soma_atual
        melhor_inicio = inicio
        melhor_fim = i

subarray = nums[melhor_inicio:melhor_fim + 1]

print(f"\nArray original: {nums}")
print(f"Melhor subarray: {subarray}")
print(f"Soma máxima: {max_soma}")
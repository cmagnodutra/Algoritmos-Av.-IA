#Dado um array de inteiros, encontre todos os trios únicos de números que somam zero.
#A solução não deve conter trios repetidos.

print("\033[96m=== Three Sum ===\033[0m")
print("Encontra todas as triplas no array que somam zero.")
print()

entrada = input("Digite os números separados por espaço: ")
nums = list(map(int, entrada.split()))

nums.sort()
resultado = []

for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    esq, dir = i + 1, len(nums) - 1

    while esq < dir:
        total = nums[i] + nums[esq] + nums[dir]
        if total == 0:
            resultado.append([nums[i], nums[esq], nums[dir]])
            while esq < dir and nums[esq] == nums[esq + 1]:
                esq += 1
            while esq < dir and nums[dir] == nums[dir - 1]:
                dir -= 1
            esq += 1
            dir -= 1
        elif total < 0:
            esq += 1
        else:
            dir -= 1

print(f"\nArray: {nums}")
if resultado:
    print(f"Triplas que somam zero:")
    for t in resultado:
        print(f"  {t[0]} + {t[1]} + {t[2]} = 0")
else:
    print("Nenhuma tripla encontrada.")
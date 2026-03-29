#Dado um array de inteiros e um valor alvo (target), encontre dois índices de elementos cuja soma seja igual ao alvo.
#Você não pode usar o mesmo elemento duas vezes e pode retornar a resposta em qualquer ordem.

print("\033[96m=== Two Sum ===\033[0m")
print("Dado um array e um target, retorna os índices de dois números que somam o target.")
print()
 
entrada = input("Digite os números separados por espaço: ")
nums = list(map(int, entrada.split()))
target = int(input("Digite o target: "))
 
seen = {}
resultado = None
 
for i, num in enumerate(nums):
    complemento = target - num
    if complemento in seen:
        resultado = [seen[complemento], i]
        break
    seen[num] = i
 
if resultado:
    print(f"\nResposta: índices {resultado}")
    print(f"  {nums[resultado[0]]} + {nums[resultado[1]]} = {target}")
else:
    print("\nNenhuma solução encontrada.")
 
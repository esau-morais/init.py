# criar uma função rápida para um título
def lin():
    print("-=" * 18)


lin()
print(" == LISTA ORDENADA SEM REPETIÇÕES == ")
lin()

# criar lista
nums = []

# criar repetição de 5 números
for n in range(0,5):
    num = int(input("Digite um número: "))
    if n == 0 or num > nums[-1]:
        nums.append(num)
        print("Número adicionado à lista.")
    else:
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos,num)
                print(f"Adicionado à posição {pos + 1}")
                break
            pos += 1
lin()
print(f"Os valores digitados foram: {nums}")    

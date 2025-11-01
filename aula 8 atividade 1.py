# ===============================
# EXERCÍCIOS - AULA 8 (Condicionais)
# ===============================

# 1️⃣ Verificar se o número é positivo, negativo ou zero
num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# ------------------------------------------

# 2️⃣ Verificar se a pessoa pode votar com base na idade
idade = int(input("\nDigite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")

# ------------------------------------------

# 3️⃣ Verificar se um número é par ou ímpar
numero = int(input("\nDigite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# ------------------------------------------

# 4️⃣ Verificar o tipo de triângulo (equilátero, isósceles, escaleno)
print("\nDigite o valor dos três lados do triângulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")

# ------------------------------------------

# 5️⃣ Verificar se um número é múltiplo de 5 e 7
num_multi = int(input("\nDigite um número: "))

if num_multi % 5 == 0 and num_multi % 7 == 0:
    print("O número é múltiplo de 5 e 7.")
else:
    print("O número NÃO é múltiplo de 5 e 7.")

# ------------------------------------------

# 6️⃣ Verificar se um número é positivo e maior que 10
num_check = float(input("\nDigite um número: "))

if num_check > 0 and num_check > 10:
    print("O número é positivo e maior que 10.")
elif num_check > 0 and num_check <= 10:
    print("O número é positivo, mas não é maior que 10.")
else:
    print("O número não é positivo.")

# ------------------------------------------

# 7️⃣ Verificar se um número é divisível por 3 ou 5
num_div = int(input("\nDigite um número: "))

if num_div % 3 == 0 or num_div % 5 == 0:
    print("O número é divisível por 3 ou por 5.")
else:
    print("O número não é divisível por 3 nem por 5.")

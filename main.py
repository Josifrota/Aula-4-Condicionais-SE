#Condição SE - Idade

idade = int(input("Olá, Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18 and idade < 65:
    print("Você é um adulto!")
else :
    print("Você é um idoso!")

print('\n')
print("-----------------------")

#Condição Nota - Aprovado / Reprovado / Recuperação

nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2
print(media)

if media >= 6.0 :
  print("Aprovado")
  
else media < 6.0 :
  print("Aluno em recuperação")
    
nota3 = float(input("Digite a nota da recuperação "))

media2 = (nota1 + nota2 + nota3) / 3
print("Média Final: ", media2)

if media2 >= 6.0 :
  print("Aprovado")
  
else  :
  print("Aluno reprovado")


print('\n')
print("-----------------------")

n1 = int(input("Digite um número: "))

if n1% 2 == 0 :
    print("O número", n1, " é par.")
else :
    print("O número", n1, " é ímpar.") 

print('\n')
print("---------------------")

n1 = float(input("Digite um número: "))
operador = input("Digite o operador (+, -, *, /): ")
n2 = float(input("Digite outro número: "))  
if operador == "+" :
    print("O resultado dessa operação é: ", n1 + n2)
elif operador == "-" :
    print("O resultado dessa operação é: ", n1 - n2)
elif operador == "*" :
    print("O resultado dessa operação é: ", n1 * n2)
elif operador == "/" :
    print("O resultado dessa operação é: ", n1 / n2)
else :
    print("Operador inválido")  


print('\n')
print("---------------------")


"""
#A função recebe 5 numeros armazena em uma lista e depois os imprime
num = []
for n in range(0,5):
    num.append(int(input(f"Digite um numero {n}: ")))

print(f"{num}")
"""

"""
#Recebe 10 numeros e imprime a lista ao contrario
num = []
for n in range(0,10):
    num.append(float(input("Digite um numero real: ")))
tam = 10

print(f"{num[::-1]}")
"""
"""
#leia 4 nota e faça a media
soma = 0

for n in range(0,4):
    n = float(input("Digite a nota: "))
    soma += n
media = soma / 4

print(f"A media eh {media}")
"""
"""
texto = []
cont = 0
for n in range(0, 10):
    texto.append(str(input("Digite um caracter: ")))

if 'a' in texto:
    texto.remove('a')
if 'e' in texto:
    texto.remove('e')
if 'i' in texto:
    texto.remove('i')
if 'o' in texto:
    texto.remove('o')
if 'u' in texto:
    texto.remove('u')

print(f"{texto}")
print(f"{len(texto)}")
"""
"""
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
par = []
impar = []

for n in range(0,20):
    numeros.append(int(input("Digite numero: ")))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f"{numeros}")
print(f"{par}")
print(f"{impar}")
"""
"""
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.


recebe = []

for j in range(1,11):
    notas = []
    media1 = 0
    for i in range(0,4):
        notas.append(float(input(f"Digite as notas do aluno {j}: ")))
        media1 += notas[i]

    media1 = media1 / 4
    print("\n")
    if media1 >= 7.0:
        recebe.append(media1)

print(f"{recebe}")
"""

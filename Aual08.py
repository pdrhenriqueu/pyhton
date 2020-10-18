import math

# desafio16
# num = float(input("Digite um numero: "))
# print("Parte inteira: {}".format(math.floor(num)))

# desafio17
#ca = float(input("Digite o CA: "))
#co = float(input("Digite o CO: "))
#print("A hipotenusa eh: {:.2f}".format(math.hypot(ca, co)))

#desafio18
#angulo = float(input("Digite um angulo: "))
#angulo = math.radians(angulo)
#print("cos {:.2f} e sen {:.2f}".format(math.cos(angulo), math.sin(angulo)))

#desafio19
import random
#a1 = (input("Digite o nome do aluno 1: "))
#a2 = (input("Digite o nome do aluno 2: "))
#a3 = (input("Digite o nome do aluno 3: "))
#a4 = (input("Digite o nome do aluno 4: "))
#lista = [a1, a2, a3, a4]
#sorteia = random.choice(lista)
#print("O escolhido foi o: {}".format(sorteia))

#desafio20
#a1 = (input("Digite o nome do aluno 1: "))
#a2 = (input("Digite o nome do aluno 2: "))
#a3 = (input("Digite o nome do aluno 3: "))
#a4 = (input("Digite o nome do aluno 4: "))
#lista = [a1, a2, a3, a4]
#random.shuffle(lista)
#print("A ordem eh: {}".format(lista))

#aula09
#desafio22
#nome = str(input("Nome:")).strip()
#print("Maisculo: {}".format(nome.upper()))
#print("Minusculo: {}".format(nome.lower()))
#print("Letras do nome: {}".format(len(nome) - nome.count(" ")))
#print("Letras Primeiro Nome: {}".format(nome.find(' ')))


#desafio23
#numero = int(input("Digite NUM: "))
#print("Unidade: {}".format(numero // 1 % 10))
#print("Dezena: {}".format(numero // 10 % 10))
#print("Centena: {}".format(numero // 100 % 10))
#print("Milhar: {}".format(numero // 1000 % 10))

#desafio24
#cidade = str(input("Digite o nome da sua cidade: ")).upper().strip()
#print(cidade[:5] == 'SANTO')

#desafio25
#nome = str(input("Digite o nome: ")).upper().strip()
#print("Tem silva no Nome? {}".format("SILVA" in nome))


#desafio 26
#frase = str(input("Digite uma frase: ")).strip().upper()
#print("Qunt de a: {}".format(frase.count('A')))
#print("o Primeiro A: {}".format(frase.find("A")+1))
#print("o Primeiro A: {}".format(frase.rfind("A")+1))

#desadio 27
nome = str(input("Digite seu nome: ")).strip()
n = nome.split()
print("Primeiro nome: {}".format(n[0]))
print("Ultimo nome: {}".format(n[len(n)-1]))

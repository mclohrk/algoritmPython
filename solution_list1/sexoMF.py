######################
# created by McloHrk #
# github.com/mclohrk #
# mclohrk.github.io  #
######################

# Code: 
# Name: sexoMF
# Version:v1
# Description:
# Programa:  Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e aofinal 
# informe total de homens e de mulheres


from tokenize import String
import sys

def repeatNumber():
	x = int(input("qual é a quantidade de pessoas? "))
	return x

def addSexOfPeople(x,vetorSexo):
	
	for n in range(x):
		try:
			char_ = str(input("Infome o sexo da pessoa [M/F]: "))
			assert char_ in ('M', 'F')
			vetorSexo.append(char_)  
		except ValueError:
			print("Oops!  Invalid Input.  Try again...")
			
	return vetorSexo

def printMessage(obj):
	print(obj)			


def main():
	
	vetorSexo = []	
	numRepeat = repeatNumber()
	addSexOfPeople(numRepeat,vetorSexo)
	
	qtdM = vetorSexo.count("M")
	qtdF = vetorSexo.count("F")

	print("Quantidade Homens: ",qtdM)
	print("Quantidade Mulheres: ",qtdF)	

main()

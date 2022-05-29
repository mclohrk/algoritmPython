'''
4. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no
semestre. No final informar o nome do aluno e a sua média (aritmética) e se o mesmo obteve
aprovação, foi reprovado ou irá fazer prova final. A média para aprovação é 7,0. Alunos que tirem
notas menores que 7,0 mas maiores ou igual a 3,0 podem fazer prova final.
'''
def main():
    print("Prorama ssoma notas e aprova aluno ")
    nome = input("infome o nome do aluno >> ")
    nota_1 = float(input("Infome a nota 1 >>"))
    nota_2 = float(input("Infome a nota 2 >>"))
    nota_3 = float(input("Infome a nota 3 >>"))
    media = (nota_1 + nota_2 + nota_3 ) / 3

    if media >= 7:
        print("Aluno aprovado,  com media  ", media)

    elif (media < 7) & (media >= 3):
        print("Aluno em prova final,  com media  ", media)
    else:
        print("Aluno reprovado, com media  ", media)

main()
aluno = {}

aluno["nome"] = input("Qual o seu nome: ")
aluno["Nota 1"] = float(input("Digite sua nota 1: "))
aluno["Nota 2"] = float(input("Digite sua nota 2: "))

imc = aluno["Nota 1"] / (aluno["Nota 2"] ** 2)

aluno["imc"] = imc

print("/n Dados")
print("Nome: ", aluno["nome"])
print("Nota 1: ", aluno["Nota 1"])
print("Nota 2: ", aluno["Nota 2"])


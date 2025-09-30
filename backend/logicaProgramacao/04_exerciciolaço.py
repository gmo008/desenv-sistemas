
senhacorreta = input("digite a senha correta")
senha = input("digite a senha")
nome = input("digite o seu nome")
salario = float(input("digite seu salario"))

while senha!= senhacorreta:
    print("senha incorreta")
    senha = input("digite a senha novamente")

    print("Bem-vindo", nome)

    salarioanual = salario * 12

    if(salarioanual > 100000):
        print("rico")
    else:
        print("faz o l")
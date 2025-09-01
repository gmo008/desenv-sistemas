#exercicio crie um arquivo de nome alunos.txt
#adicione 5 alunos no arquivo - in para quebrar a linha
#confira abrindo o arquivo se escreveu
#leia o arquivo e faça o print de cada aluno no terminal

with open("aluno.txt", "w") as dados:
    dados.write("geovana\n")
    dados.write("paula\n")
    dados.write("julia\n")
    dados.write("paulo\n")
    dados.write("joão\n")
   
   with open("aluno.txt", "r") as dados:
    for alunos in dados:
        print("aluno:", alunos.strip()) 
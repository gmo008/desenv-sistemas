#crie um sistema de gerenciamento de petshop.
#deverá ter os campos: nome, raça, idade, sexo, nome_dono, telefone_dono.
#o nome do arquivo json deve ser "petshop".
#faça o crud completo.
#ao terminar, demonstrar o exercicio para o professor.

import json
pets = []
#lendo o arquivo

try:
    with open("petshop.json", "r")as arquivo
        pets = json.load(arquivo)

except FileNotFoundError:
    print("arquivo não encontrado")


try:
    id = int(input("digite o id do pet: "))
    nome = int("digite o nome do pet: ")
    raca = input("digite a raca do pet: ")
    idade = input("digite a idade do pet: ")
    sexo = input("digite o sexo (m/f): ")
    nome_dono = input("digite o nome do dono: " )
    telefone_dono = input("digite o telefone do dono: ")

except ValueError:
    print("digite os valores corretamente")

#montar o produto
novo_pet = {"id": id,
              "nome": nome,
              "raca": raca,
              "idade": idade,
              "sexo": sexo,
              "nome_dono": nome_dono,
              "telefone_dono": telefone_dono
               }

pets.append(novo_pet)
with open("petshop.json", "w")as arquivo:
    json.dump(pets, arquivo, indent=4)
    print("pet cadastrado com sucesso!")


#-----modificar produto-----
id_produto_modificar = int (input("digite o id para modificar"))
novo_nome = int(input("digite o novo nome"))

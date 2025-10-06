#{} - chaves: definir um objeto- ficha de cadastro 
#[] - colchete: definir uma lista 
#chave/valor: chave descreve o valor    chave=telefone   valor="4499999-9999"


#sempre importar o json
import json
inventario = []
#lendo o arquivo
try:
    with open("loja.json", "r")as arquivo:
      inventario = json.load(arquivo)

except FileNotFoundError:
    print("arquivo nao encontrado")


try:
    id= int(input("digite o id do produto"))
    nome = input("digite o nome do produto: ")
    quantidade = int(input("digite a quantidade: "))
    preco = float(input("digite o preco: "))

except ValueError:
    ptint("digite o valor corretamente")


#montar o objeto
novo_produto= {"id": id,
              "nome": nome,
              "quantidade": quantidade,
              "preco": preco,
               "em_estoque": quantidade > 0 #expressao verdadeiro ou falso
               }


#escrever o objeto no arquivo
 
inventario.append(novo_produto)
with open("loja.json", "w")as arquivo:
    json.dump(inventario, arquivo, indent=4)
    #indent - formatar o arquivo json
    print("produto cadastrado com sucesso")


#-----modificar produto-----
id_produto_modificar = int (input("digite o id para modificar"))
nova_quantidade = int(input("digite a nova quantidade"))

try:
    with open("loja.json", "r" as arquivo:)
    inventario = json.load(arquivo)
except FileNotFoundError:
    print("arquivo não encontrado")

produto_encontrado = False

for produto in inventario:
    if produto['id'] == id_produto_modificar:
    #colocamos a nova quantidade 
        produto['quantidade'] = nova_quantidade
        produto['em_estoque'] = nova_quantidade > 0
        produto_encontrado = True
        break;

if not produto_encontrado:
    print("o produto com o id informado não foi encontrado")

else:
    with open("loja.json", "w")as arquivo:
        json.dump(inventario,arquivo,indent=4)
    print("o arquivo foi alterado com sucesso!!")















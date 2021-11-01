#VERSÃO 3 DA APS

#importar bliblioteca
import cryptocode

#Menu de escolha de função do codigo
menu = input("Digite o que você deseja fazer: \n 1- criptografar \n 2- descriptografar \n 9- Informaçoes sobre o programa \n opção:")

#Opção 1 com o objetivo de criptografar
if menu == '1':
    valor = input("Digite a chave que você deseja criptografar: ")
    valor = cryptocode.encrypt(valor, 'wow')
    print (valor)

#Opção 2 com o objetivo de descriptografar
elif menu == '2':
    valor2 = input("Digite a chave que você deseja descriptografar: ")
    valor2 = cryptocode.decrypt(valor2, "wow")
    print (valor2)

#Opção 9 com o objetivo de mostrar as informações do codigo
elif menu == '9':
        print ("\n O codigo foi desenvolvido em Python, Pelos alunos do grupo Erro 404! \n" +
        "Tem como função a criptografia e descriptografia de dados de entrada atraves do input \n" +
        "Biblioteca utilizada foi a cryptocode, que utilizada o metodo SHA de criptografia.")

#Caso a opção escolhida seja diferente do menu
else:
    print("opção invalida")
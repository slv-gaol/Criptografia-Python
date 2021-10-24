#VERSÃO 2 DA APS
#importar bliblioteca
import cryptocode

#Menu de escolha de função do codigo
menu = input("Digite o que você deseja fazer: 1 para criptografar ou 2 para descriptografar: ")

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

#Caso a opção escolhida seja diferente do menu
else:
    print("opção invalida")
#importar bliblioteca para criptografar
from simplecrypt import encrypt, decrypt
import PySimpleGUI as sg    
import tk  

passkey = 'wow'
str1 = input('Digite o que você deseja criptografar: ')
cipher = encrypt(passkey, str1)
print(cipher)

menu2 = input('Deseja descriptografar (sim ou nao): ')
if menu2 == 'sim':
    print(decrypt('wow', cipher))
else:
    print ('até mais')
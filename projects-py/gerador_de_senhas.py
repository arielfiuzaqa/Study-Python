# Pense em como desenvolver um de forma bem tranquila do zero.
'''Senhas com:
    letras maiusculas e minusculas
    simbolos e espaços
    palavras chaves que pode criar algo criativo'''

# Inserindo a chaver - Forma diferente
palavra_chave = input("Digite a base da senha: ")

senha = ""
for letra in palavra_chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Gg":
        senha = senha + "#"
    elif letra in "Rr":
        senha = senha + "$"
    else:
        senha = senha + letra
        continue
print(senha)








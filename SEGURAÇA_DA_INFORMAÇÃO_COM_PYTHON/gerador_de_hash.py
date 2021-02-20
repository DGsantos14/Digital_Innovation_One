import hashlib

print("\n################################@DGSANTOSFKZ#################################")
print("############################## GERADOR DE HASH ##############################")

string = input("Digite o texto a ser gerado a hash: \n")

menu = int(input('''### MENU - ESCOLHA O TIPO DA HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
Digite o número do hash a se gerado: \n'''))


if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("A hash  MD da string \n", string, "é: \n", resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("A hash  SHA1 da string \n", string, "é: \n", resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("A hash  SHA256 da string \n", string, "é: \n", resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("A hash  SHA512 da string \n", string, "é: \n", resultado.hexdigest())

else:
    print("Algo de errado não deu certo, tente novamente!")

print("\n################## OBRIGADO POR USAR NOSSO GERADOR DE HASH ##################")
print("###################################FKZ TEC###################################")
print("\n###################################THE AND###################################")
print("################################@DGSANTOSFKZ#################################")
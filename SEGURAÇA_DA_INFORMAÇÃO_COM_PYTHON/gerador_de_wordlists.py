import itertools

print("\n################################@DGSANTOSFKZ#################################")
print("#############################GERADOR DE WORDLISTS#############################")

string = input("Informe a String a ser permutada: \n")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))

print("\n################OBRIGADO POR USAR NOSSO GERADOR DE WORDLISTS#################")
print("###################################FKZ TEC###################################")
print("\n###################################THE AND###################################")
print("################################@DGSANTOSFKZ#################################")
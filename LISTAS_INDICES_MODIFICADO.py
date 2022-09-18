#BUSCA DE DADOS LISTA
equipamentos=[]
valores =[]
seriais =[]
departamentos =[]
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
#concatenação de Variaveis tipo int e string
    seriais.append(int and str(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\"para continuar: ").upper()
#BUSCA DADO LISTA
busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
# SE BUSCA FOR IGUAL EQUIPAMENTOS FAÇA
       if busca ==equipamentos[indice]:
           print("Valor..: ", valores[indice])
           print("Serial.:", seriais[indice])


nomes = ["Joaquim ", "Maria " , "Ana"]

print(nomes[0])     # Joaquim
print(nomes[1])
print(nomes[2])

nomes [0] = "Joao" #estava Joaquim

print(nomes[0]) # alterado para Joao
print(nomes[1])
print(nomes[2])

nomes.append ("Joao")
nomes.append("Joana")

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])
print(nomes[5])

nomes.insert(1,"fernanda") # insere "Fernanda" na posicao 1
print("Apos insert:", nomes)

# modificando elementos
nom[2] = "Paulo" #modificao no indice 2
print ("Apos modificacao" ,nomes)

# removendo elemento
del nomes [3] # remove o elemento no indice 3
print ("Apos del: , nomes" )

nomes.remove ("Maria") # remove a primeira ocorrencia de"Maria"
print ("Apos remover:, nomes" )

removido = nomes.pop (2) # Remove e retorna o elememnto no indice 2
print(f"Apos pop (removido '[removido]'):",nomes)

nomes.clear() #esvazia a lista 
print("Apos clear:", nomes)
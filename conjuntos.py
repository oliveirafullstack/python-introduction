# Criando um conjunto
conjunto  = {1,2,3,4}
# Adciona um valor (sem duplicar)
conjunto.add(4) # Não sera adicionado novamente 

# Verifica qse um valor está presente 
print(2 in conjunto) #Saida: True

#Criar dois conjuntos e encontrar a interseção entre eles

set1 = {1,2,3,4}
set2 = {3,4,5,6}

intersecao  =  set1 & set2
print(intersecao) # Saida: {3,4}
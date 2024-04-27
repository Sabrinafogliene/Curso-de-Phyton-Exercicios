frutas = ["laranja", "maca", "uva"]
print (frutas)
print (frutas[0])
print (frutas[-1])

frutas = []
print (frutas)

letras = list("python") #armazena letra por letra
print (letras)

numeros = list(range(10)) #armazena números de 0 a 9
print (numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print (carro)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] #[1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

lista = ["p", "y", "t", "h", "o", "n"]
lista[2:] # ["t", "h", "o", "n"] (inicial - da posição 2 em diante)
lista[:2] # ["p", "y"] (final - da posição 0 até a 2, mas a 2 não retorna)
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"] (inicial, final e o step(andando, nesse caso, de 2 em 2))
lista[::] # ["p", "y", "t", "h", "o", "n"] (cópia exata da sequência)
lista[::-1] # ["n", "o", "h", "t", "y", "p"] (espelha a declaração de uma lista)

# Iterar lista pelo comando for

carros = ["gol", "celta", "palio"]

for carro in carros: #carro é cada item que declarei dentro da lista carros
    print (carro)

for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")


#Filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero)

#Filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

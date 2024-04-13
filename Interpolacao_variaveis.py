# %s tipo string; %d tipo inteiro; %f flutuante

nome = "Sabrina"
idade = 32
profissão = "Estudante de Programação"
linguagem = "Phyton" 

dados = {"nome": "Sabrina", "idade": 32}

print("Nome: %s Idade: %d" % (nome,idade))

print("Nome: {} Idade: {}".format(nome,idade))

print("Nome: {0} Idade: {1} Nome: {0} {0}".format(nome,idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
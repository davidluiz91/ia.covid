from sklearn.naive_bayes import GaussianNB

import atv

# treino
modelo = GaussianNB()
modelo.fit(atv.atributos, atv.resultados)

# entrada
febre = int(input("Apresenta febre? "))
cansaco = int(input("Apresenta Cansaço? "))
tosse = int(input("Apresenta tosse seca? "))
espirro = int(input("Apresenta Espirro? "))
corpo = int(input("Apresenta dor no corpo?"))
coriza = int(input("Apresenta coriza? "))
garganta = int(input("Está com dor de garganta? "))
diarreia = int(input("Apresenta diarreia? "))
cabeca = int(input("Apresenta dor de cabeça? "))
ar = int(input("Apresenta falta de ar? "))

# resultado
resultado = modelo.predict(
    [[febre, cansaco, tosse, espirro, corpo, coriza, garganta, diarreia, cabeca, ar]])

if (resultado==1):
    print('Recomenda-se fazer o teste de corona virus')
if (resultado==0):
    print('Paciente não apresenta sintomas de corna virus')
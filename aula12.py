nome = 'João Pedro'
altura = 1.96
peso = 88
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)

testando_fstrings = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}.'

print(testando_fstrings)
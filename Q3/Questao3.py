from array import array
from cgi import print_form
import json
import sys
import statistics


with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

max = {
    "dia": sys.maxsize * -1,
    "valor": sys.maxsize * -1
}

min = {
    "dia": sys.maxsize,
    "valor":sys.maxsize
}

print(max, min)
print("-" * 30)
for dia in dados:
    if dia['valor'] > max['valor']:
        max['valor'] = dia['valor']
        max['dia'] = dia['dia']
    if dia['valor'] < min['valor']:
        min['valor'] = dia['valor']
        min['dia'] = dia['dia']

print("O valor máximo foi", max['valor'])
print("O valor minimo foi de", min['valor'])

total = sum(it['valor'] for it in dados)

for dia in dados:
    if dia['valor'] > 0:
        media = statistics.mean(it['valor'] for it in dados)

contar = 0


for dia in dados:
    if dia['valor'] > media:
        contar = contar +1

print("O número de dias em que o valor foi maior que a média foram" ,contar , "dias.")

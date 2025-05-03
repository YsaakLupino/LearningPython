'''
🔸 Criar um script que:
Pega vários filmes da API - filtro ano
Salva os dados em .csv
Lê esse .csv com pandas
Cria gráficos com matplotlib ou seaborn (ex: quantidade de filmes por idioma, nota média por diretor etc.)
'''
import requests

f'http://www.omdbapi.com/?y=2020&apikey=b20caf44'

r = requests.get('http://www.omdbapi.com/?apikey=b20caf44&i=tt1285016')
print(r.json())
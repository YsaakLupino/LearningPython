import requests
from bs4 import BeautifulSoup
from time import time
import pandas

books = {}
n = 0

tempoI = time()
for page in range(1, 51):
    link = f'https://books.toscrape.com/catalogue/page-{page}.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
    html = requests.get(link, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    book_table = soup.find('ol').find_all('li')
    for book in book_table:
        n+=1
        books[f'Livro {n}'] ={
                            'Título': book.find('h3').a['title'],
                            'Preço': book.find('div', class_ = 'product_price').p.text,
                            'Nota': book.find('p')['class'][1]
                            }
tempoF = time()
exec_time = tempoF - tempoI

# print(books)
print(f'TEMPO DE EXECUÇÃO DA RASPAGEM: {exec_time}')


df = pandas.DataFrame(books)
df = df.transpose()
print(df.axes[0][3] + df.axes[1][2])

n= 0
for nota in df['Nota']:
    if nota == 'One':
        df[df.axes[1][2]][df.axes[0][n]] = 'Um'
    if nota == 'Two':
        df[df.axes[1][2]][df.axes[0][n]] = 'Dois'        
    if nota == 'Three':
        df[df.axes[1][2]][df.axes[0][n]] = 'Três'
    if nota == 'Four':
        df[df.axes[1][2]][df.axes[0][n]] = 'Quatro'
    if nota == 'Five':
        df[df.axes[1][2]][df.axes[0][n]] = 'Cinco'
    n+= 1 

print(df)

df.to_excel('Livros do site.xlsx')
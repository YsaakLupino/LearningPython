Desafio: Rastrear preços de livros

Objetivo:
    Criar um script Python que: 
        1 - Acesse o site de livros (exemplo: https://books.toscrape.com).
        2 - Extraia o título do livro,  o preço e a nota (rating).
        3 - Salve tudo em um arquivo CSV.

Regras e dicas:
    1.Use apenas requests e BeautifulSoup (sem Selenium).
    2. Extraia todos os livros da primeira página.
    3. Organize o resultado em um DataFrame (pandas) antes de salvar.

**O CSV deve conter colunas:["titulo", "preco", "nota"]**

Como bônus:
    1 - Faça o script percorrer todas as páginas do site (há 50 no total).
    2 - Calcule o preço médio dos livros com nota “Five”.
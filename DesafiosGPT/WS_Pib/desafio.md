Desafio: Raspagem de tabela de países e PIB

Criar um script Python que: 
    - Acesse a página da Wikipédia
         - https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_PIB_nominal

    - Extraia a primeira tabela que contém:

    - Nome do país,

    - PIB nominal (em dólares),

    - Ano da estimativa (se houver).

    - Organize os dados em um DataFrame pandas.

    - Salve o resultado em pib_paises.csv.

🧰 Regras e dicas
    - Use requests e BeautifulSoup 
    - O DataFrame deve conter:
        1- ["País", "PIB (US$ bilhões)", "Ano"]
    - Converta os valores de PIB para float (ex: remover vírgulas, espaços e símbolos).

💡 Bônus (opcional)

 - Ordene o DataFrame pelo PIB (do maior para o menor).
 - Calcule o PIB total e o PIB médio.
 - Gere uma pequena visualização (ex: top 10 países com maior PIB) usando matplotlib.
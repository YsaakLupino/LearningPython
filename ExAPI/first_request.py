import requests

#título ano tempo diretor linguagem e premios

amarelo = '\033[33m'
reset = '\033[0m'
lista_filmes = []

class filme_buscado():
    def __init__(self,titulo,diretor,premios,lingua,tempo, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.premios = premios
        self.lingua = lingua
        self.tempo = tempo
        self.ano = ano

while True:
    busca = str(input('Qual filme ou série deseja buscar?'))
    link_api = f'http://www.omdbapi.com/?t={busca}&apikey=b20caf44'
    r = requests.get(link_api)
    r_json = r.json()
    try:
        filme  = filme_buscado(r_json['Title'], r_json['Director'], r_json['Awards'],
                            r_json['Language'], r_json['Runtime'], r_json['Year']
                            )
        lista_filmes.append(filme)
    except:
        print('Filme não encontrado!!')
        pass
    while True:
        loop = str(input('Deseja procurar por outro filme?[S/N]')).upper().strip()[0]
        if loop in ['S','N']:
            break
        print('Por favor insira sim ou não para sua resposta!')
    if loop == 'S':
        continue
    print('\n',f'{amarelo}\bAqui estão os filmes que você buscou:','\n')
    for filme in lista_filmes:
            print(
                f"{amarelo}{'Título:'.ljust(14)}{reset}{filme.titulo}\n"
                f"{amarelo}{'Diretor:'.ljust(14)}{reset}{filme.diretor}\n"
                f"{amarelo}{'Premios:'.ljust(14)}{reset}{filme.premios}\n"
                f"{amarelo}{'Lingua:'.ljust(14)}{reset}{filme.lingua}\n"
                f"{amarelo}{'Tempo:'.ljust(14)}{reset}{filme.tempo}\n"
                f"{amarelo}{'Ano:'.ljust(14)}{reset}{filme.ano}\n"
                + '_' * 30 + '\n'
            )
    break

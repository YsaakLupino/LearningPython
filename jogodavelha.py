from random import randrange
from time import sleep
# board = [['X','X','X'],['X','X','X'],['X','X','X']]
board = [[1,2,3],[4,5,6],[7,8,9]]
def display_board(board):
    '''A função aceita um parâmetro contendo o status atual do tabuleiro
     e o imprime no console'''
    print('+-------+-------+-------+\n'+
    '|       |       |       |\n'+
    f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n'+
    '|       |       |       |\n'+
    '+-------+-------+-------+\n'+
    '|       |       |       |\n'+
    f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n'+
    '|       |       |       |\n'+
    '+-------+-------+-------+\n'+
    '|       |       |       |\n'+
    f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n'+
    '|       |       |       |\n'+
    '+-------+-------+-------+')

def enter_move(board):
    '''A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada,
    verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.'''

    free_fields = make_list_of_free_fields(board)

    #verifica de há campos para jogar
    if free_fields.__len__() == 0:
        print('Não há mais movimentos possíveis!')
        return 'Velha'

    while True: 
        try:
            player_play = int(input('Em qual numero você deseja jogar?'))
            valid_play = False
            for row in board:
                for field in row:
                    if player_play == field:
                        valid_play = True
            if not valid_play:
                raise ValueError
            break
        except ValueError:
            print('Você deve inserir um valor presente no tabuleiro!')
    for row, row_value in enumerate(board,0):
        for column, value  in enumerate(row_value,0):
            if value == player_play:
                board[row][column] = 'X'

    return True

 
def make_list_of_free_fields(board):
    '''A função navega pelo tabuleiro e constrói uma lista de todas as casas livres;
     a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.'''
    free_fields = []
    for row,field_row in enumerate(board,0):
        for column, field_column in enumerate(field_row,0):
            if isinstance(field_column,int):
                free_fields.append((row,column))
    return free_fields


def victory_for(board, sign):
    '''A função analisa o estado do tabuleiro a fim de verificar se
    o jogador usando 'O's ou 'X's ganhou o jogo'''

    #verificação de linha
    for row in board:
        if row == [sign, sign, sign]:
            return sign
                
    #verificação de coluna
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return sign
    
    # Verifica diagonais
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return sign
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return sign

        
 
def draw_move(board):
    '''A função desenha o movimento do computador e atualiza o tabuleiro.'''
    #verificar se este é primeiro movimento, caso sim, o computador começa jogando no meio
    start = True
    for row in board:
        if not start:
            break
        for field in row:
            if isinstance(field, str):
                start = False
    if start:
        board[1][1] = 'O'
        return True

    free_fields = make_list_of_free_fields(board)

    #verifica de há campos para jogar
    if free_fields.__len__() == 0:
        print('Não há mais movimentos possíveis!')
        return 'Velha'
    
    rand_cpu_play = free_fields[randrange(0,free_fields.__len__())]
    board[rand_cpu_play[0]][rand_cpu_play[1]] = 'O'
    return True

def loading():
    print('Carregando',end='',flush=True)
    sleep(0.3)
    string = '....'
    for letra in string:
        print(letra,end='', flush=True)
        sleep(0.3)
    print()

def main():
    print('O jogo vai começar, o PC começa jogando no meio!')
    loading()
    draw_move(board)

    while True:
        display_board(board)

        if victory_for(board, 'O') == 'O':
            print('\nO computador venceu!')
            break

        if not enter_move(board):
            print('\nEmpate!')
            break

        if victory_for(board, 'X') == 'X':
            display_board(board)
            print('\nVocê venceu!')
            break

        # 👇 Adiciona verificação de empate aqui, após o jogador jogar
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print('\nEmpate!')
            break

        if not draw_move(board):
            display_board(board)
            print('\nEmpate!')
            break

        loading()

main()
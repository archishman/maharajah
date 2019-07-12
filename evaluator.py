import chess as c
import chess.pgn
import os
import random
import numpy as np

fens = []
vectorized = []

def read(pgn):
    games = []
    with open(pgn,'r+') as g:
        for i in range(1000):
            gm = c.pgn.read_game(g)
            games.append(gm)
    return games
def pick_positions(games):
    for game in games:
            

def preprocess(pgn):
    count = 0    
        gm = c.pgn.read_game(g)
        while(bool(gm) and count < 10000):
            count+=1
            board = gm.board()
            for mv in gm.mainline_moves():
                board.push(mv)
                fens.append(tensorize(board))
            gm = c.pgn.read_game(g)

    return fens

def tensorize(b):
    t = np.zeros((16, 8,8))
    temp = np.asarray(list(map(list, str(b).replace(' ','').split('\n'))))
    pieces = list('KQRBNP.kqrbnp')
    for i in range(len(pieces)):
        piece = pieces[i]
        is_piece = temp == [piece] * 8
        t[i] = np.asarray(is_piece)

    return t

a = preprocess('./2013-01-games.pgn')


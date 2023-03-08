import jjcli
import os
import chess

PATH = 'lichess_db_puzzle.csv'

with open(PATH,'r') as f:
    line = f.readline()

print(line)

# PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl,OpeningFamily,OpeningVariation
id,fen,moves,rating,_,_,_,theme,url,*_ = line.split(',')

print(fen,moves,rating)



def makeBoard(fen:str, orientation:str, moves:list):
    out = jjcli.qxlines('ls puzzles/ ')
    n = len(out)
    path = os.path.join('puzzles',str(n))
    os.mkdir(path)

    for jogada in moves:
        out = jjcli.qxlines(f'ls {path}')
        n = len(out)
        pathpng = os.path.join(path, str(n)+ '.png')

        board = chess.Board(fen)
        board.push_san(jogada)
        fen = board.fen()

            
        auxpath = os.path.join("puzzles",'_.png')

        pgnmaker = f"""
var ChessImageGenerator = require('chess-image-generator');

var imageGenerator = new ChessImageGenerator({{
    size: 720,
    light: 'rgb(245, 245, 220)',
    dark: 'rgb(150, 33, 24)',
    style: 'merida',
    flipped: {orientation}
}});
imageGenerator.loadFEN("{fen}");
imageGenerator.generatePNG("{path}/{n}.png");
"""

        with open('pngmaker.js','w') as png:
            png.write(pgnmaker)

        os.system(f'node pngmaker.js')

        os.system(f'mv {pathpng} {auxpath}')
        
        os.system(f'convert -append assets/banner.png {auxpath} assets/banner.png {pathpng}')

 
    os.system(f'rm {auxpath}')
makeBoard(fen,'true',moves.split())

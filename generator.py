import jjcli
import os
import chess

def makeBoard(fen:str, orientation:str, moves:list):
    out = jjcli.qxlines('ls puzzles/ ')
    n = len(out)
    path = os.path.join('puzzles',str(n))
    os.mkdir(path)

    primeira = True
    for jogada in moves:
        out = jjcli.qxlines(f'ls {path}')
        n = len(out)
        pathpng = os.path.join(path, str(n)+ '.png')

        board = chess.Board(fen)
        board.push_san(jogada)
        fen = board.fen()

        auxpath = os.path.join("puzzles",'_.png')

        pgnmaker = f"""
//var ChessImageGenerator = require('chess-image-generator/');

const ChessImageGenerator = require(".");
var imageGenerator = new ChessImageGenerator({{
    size: 720,
    light: 'rgb(245, 245, 220)',
    dark: 'rgb(150, 33, 24)',
    style: 'merida',
    flipped: {orientation}
}});
imageGenerator.highlightSquares(["{jogada[:2]}", "{jogada[2:4]}"])
imageGenerator.loadFEN("{fen}");
imageGenerator.generatePNG("/home/jotaalvim/Documents/projetos/instagram-puzzles-generator/{path}/{n}.png");
"""

        with open('/home/jotaalvim/chess-image-generator/pngmaker.js','w') as png:
            png.write(pgnmaker)

        os.system(f'node /home/jotaalvim/chess-image-generator/pngmaker.js')
        os.system(f'mv {pathpng} {auxpath}')

        if primeira:
            if orientation == 'false':
                bt = "assets/bannertw.png"
            else:
                bt = "assets/bannertb.png"
        else:
            bt = "assets/bannert.png"

        os.system(f'convert -append {bt} {auxpath} assets/bannerb.png {pathpng}')
        primeira = False
    os.system(f'rm {auxpath}')


#PATH = 'lichess_db_puzzle.csv'
#PATH = 'lichess_db_puzzle2000.csv'
PATH = 'lichess_db_puzzle2100.csv'

with open(PATH,'r') as f:
    while True:
        line = f.readline()

# PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl,OpeningFamily,OpeningVariation
        id,fen,moves,rating,_,_,_,theme,url,*_ = line.split(',')
        print(fen,moves,rating)

        _,who,*_ = fen.split()
        if who == 'b':
            orientation = 'false'
        else :
            orientation = 'true'

        makeBoard(fen,orientation,moves.split())



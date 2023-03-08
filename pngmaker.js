
var ChessImageGenerator = require('chess-image-generator');

var imageGenerator = new ChessImageGenerator({
    size: 720,
    light: 'rgb(245, 245, 220)',
    dark: 'rgb(150, 33, 24)',
    style: 'merida',
    flipped: true
});
imageGenerator.loadFEN("r6k/pp2R2p/5p2/3p4/8/3P2b1/P1P3PP/2Q4K b - - 0 27");
imageGenerator.generatePNG("puzzles/0/5.png");

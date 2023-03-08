# instagram-puzzles-generator
instagram chess puzzle generater for my chess club's instagram

```mermaid
flowchart TD
    A(Lichess Puzzles Open Database) -->|parsing | B(fen & moves)
    B -->|chess-image-generator| C(group of images)
    C -->|ImageMagick| D[Final 4:3 Instagram Pictures]
```

## Dependecies
* jjcli
* chess 
* https://github.com/andyruwruw/chess-image-generator
* ImageMagick

# instagram-puzzles-generator
I made this project in order to automate a puzzles collection to publish and advertisement chess
in my Universities chess club instagram.

Project flow
```mermaid
flowchart TD
    A(Lichess Puzzles Open Database) -->| parsing | B(fen & moves)
    B -->| filtering by Difficulty level | C(filtered fen & moves)
    C -->|chess-image-generator| D(cluster of images)
    D -->|ImageMagick| E[Instagram Pictures]
```

Generated content:




## Dependecies
* jjcli
* chess 
* https://github.com/andyruwruw/chess-image-generator
* ImageMagick

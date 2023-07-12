# instagram-puzzles-generator
I made this project in order to automate a puzzle collection to publish and advertise chess on my University chess club's Instagram.am.

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

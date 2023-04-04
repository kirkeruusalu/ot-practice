--- 
Monopoly
---
```mermaid
  classDiagram
      Game "1" -- "1" Board
      Game "1" -- "2" Dice
      Game "1" -- "2-8" Player
      Board "1" -- "40" Tile
      class Tile{
        next
      }
      Piece "0-8" -- "1" Tile
      Player "1" -- "1" Piece
```

```mermaid
---
title: Monopoly updated
---
classDiagram
      Game "1" -- "1" Board
      class Game{
          start_square,
          prison_square
      }
      Game "1" -- "2" Dice
      Game "1" -- "2-8" Player
      class Player{
          money
      }
      Board "1" -- "40" Tile
      class Tile{
        next
        function()
      }
      Tile "1" -- "1" Prison
      class Prison{
        location
        function()
      }
      Tile "1" -- "1" Start
      class Start{
        location
        function()
      }
      Tile "3" -- "1" Community
      class Community{
         card
         function()
      }
      Tile "3" -- "1" Chance
      
        

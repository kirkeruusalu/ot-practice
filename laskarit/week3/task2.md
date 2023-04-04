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
      Prison "1" -- "1" Game
      Start "1" -- "1" Game
      Tile "1" -- "1" Start
      class Start{
        location
        function()
      }
      Tile "1" -- "1" Community
      class Community{
         card
         function()
      }
      Tile "1" -- "1" Chance
      class Chance{
         card 
         function()
      }
      Chance "1" -- "16" Chance_card
      class Chance_card{
            function()
      }
      Community "1" -- "16" Community_card
      class Community_card{
            function()
      }
      Normal "1" -- "1" Tile
      class Normal{
            name
            function()
      }
      Normal "1" -- "0-4" House
      Normal "1" -- "0-1" Hotel
      Railroad "1" -- "1" Normal
      class Railroad{
            function()
      }
      Utility "1" -- "1" Normal
      class Utility{
            function()
      }
            
      
        

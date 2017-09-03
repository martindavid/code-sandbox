--  File     : Proj1.hs
--  Author   : Martin Valentino
--  Purpose  : Entry point to the main program
--             This file contain two main function
--             that will be called by the test script

module Proj1 (initialGuess, nextGuess, GameState) where

import           Combination
import           Helper
import           Scoring

type GameState = [[String]]

-- random index for next guess selection.
-- I found out that 4 give best average
-- result from several trial
indexForGuess = 4
-- List of possible notes
notes = ["A","B","C","D","E","F","G"]
-- List of possible octave
octaves = ["1","2","3"]

-- Don't know what's the best way to come up with initial guess other than hardcode it
trialGuess = ["A2","B2","G3"]

initialGuess :: ([String], GameState)
initialGuess = (trialGuess, guessCombination notes octaves )

nextGuess :: ([String], GameState) -> (Int, Int, Int) -> ([String], GameState)
nextGuess (target, gameState) (x,y,z) = (newGuess, newState)
  where newGuess  = sortedList !! index
        newState = filterGuessList gameState target [x,y,z]
        index = length  newState `quot` indexForGuess
        sortedList = quicksort newState


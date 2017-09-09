--  File     : Scoring.hs
--  Author   : Martin Valentino
--  Purpose  : Functions that is use for compute score
--             and generate next guess

module Scoring where

import           Data.List
import           Helper

notePosition = 0 -- Note is in first position in the pitch
octavePosition = 1 -- Octave is in second position in the pitch
pitch = 0
note = 1
octave = 2

-- Compute next guess based on current score we got from previous answer
filterGuessList :: [[String]] -> [String] -> [Int] -> [[String]]
filterGuessList [] _ _ = []
filterGuessList (x:xs) list2 scores
  | scores == computedScore  = x : filterGuessList xs list2 scores
  | otherwise                       = filterGuessList xs list2 scores
  where computedScore = getScore x list2


-- Intermediate function to compute next guess score
getScore :: [String] -> [String] -> [Int]
getScore list1 list2 = [a, b, c]
  where a = correctScore pitch list1 list2
        b = correctScore note list1 list2
        c = correctScore octave list1 list2

-- count correct answer score from the guess we put
-- by pitch, note and octave
correctScore :: Int -> [String] -> [String] -> Int
correctScore part list1 list2
  | part == pitch = p
  | part == note = n
  | part == octave = o
  where p = length $ filterSimilar newList1 list2
        t = length newList1
        n = t - ln - p
        o = t - lo - p
        newList1 = removeDuplicates list1
        ln = length(deleteFirstsBy(eqNthElem 0)newList1 list2)
        lo = length(deleteFirstsBy(eqNthElem 1)newList1 list2)

--  File     : Combination.hs
--  Author   : Martin Valentino
--  Purpose  : Functions use to generate a combination

module Combination where

combinations :: Int -> [a] -> [[a]]
combinations 0 _      = [[]]
combinations _ []     = []
combinations n (x:xs) = map (x :) (combinations (n-1) xs) ++ combinations n xs

combinations' a b = [ x ++ y | x <- a, y <- b]

guessCombination a b = combinations 3 (combinations' a b)

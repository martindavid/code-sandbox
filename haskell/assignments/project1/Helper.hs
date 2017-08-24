--  File     : Helper.hs
--  Author   : Martin Valentino
--  Purpose  : A helper function use for list operations

module Helper where

-- Sort list in descending order
quicksort :: Ord t => [t] -> [t]
quicksort [] = []
quicksort (x:xs) = quicksort large ++ (x : quicksort small)
   where small = [y | y <- xs, y <= x]
         large = [y | y <- xs, y > x]

-- remove duplicate element from two list of type a
removeDuplicates :: Eq a => [a] -> [a]
removeDuplicates []     = []
removeDuplicates (x:xs) = x : removeDuplicates (filter (/= x) xs)

-- check whether element in position n
-- is similar in both list of type a
eqNthElem :: Eq a => Int -> [a] -> [a] -> Bool
eqNthElem n l1 l2 = (l1 !! n) == (l2 !! n)

-- Return similar element from two list of type t
filterSimilar :: Eq t => [t] -> [t] -> [t]
filterSimilar xs ys = [ x | x <- xs , y <- ys, x == y]

factorial :: Int -> Int
factorial 1 = 1
factorial n = n * factorial (n - 1)

------------------------------------

myElem :: Eq a => a -> [a] -> Bool
myElem a [] = False
myElem a (x: xs)
  | a == x = True
  | otherwise = myElem a xs

-------------------------------------

longestPrefix :: Eq a => [a] -> [a] -> [a]
longestPrefix _ [] = []
longestPrefix (x:xs) (y:ys)
  | x == y = x : longestPrefix xs ys
  | otherwise = []


-------------------------------------
prevCFunc :: Int -> Int

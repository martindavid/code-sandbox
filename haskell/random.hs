{-# LANGUAGE TemplateHaskell #-}

allPos []     = True
allPos (x:xs) = x > 0 && allPos xs

doubleSmallNumber x = if x > 10
                         then x
                         else x*2

doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

-- Take two lists of any type and pairs them up
pair :: [a] -> [b] -> [(a,b)]
pair l1 l2 = [(x,y) | x <- l1, y <- l2]

sumTorial :: Integer -> Integer
sumTorial 0 = 0
sumTorial n = n + sumTorial (n - 1)

hailStone :: Integer -> Integer
hailStone n
 | n `mod` 2 == 0 = n `div` 2
 | otherwise      = 3*n + 1

foo :: Integer -> Integer
foo 0 = 16
foo 1
  | "Haskell" > "C++" = 3
  | otherwise         = 4
foo n
  | n < 0 = 0
  | n `mod` 17 == 2 = -43
  | otherwise = n + 3

zero = len []
one
 = len
      []
two = len [1,2]
three = len [1,2,3]
four = len [1,
     2,3,
         4]
len []     = 0
len (x:xs) = 1 + len xs

myXor :: Bool -> Bool -> Bool
myXor a b = a || b

pairList :: [Int] -> [Int] -> [Int]
pairList [] [] = []
pairList a b   = a ++ b

reverse' :: [Int] -> [Int]
reverse' []     = []
reverse' (x:xs) = reverse xs ++ [x]

getNthElem :: Int -> [Int] -> Int
getNthElem a b = b!!a

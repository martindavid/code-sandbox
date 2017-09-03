import           Data.Foldable

main = print "Hello World"


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

sumPair :: (Int, Int) -> Int
sumPair (x, y) = x + y

-- generate a hailstone iterations from a starting number
hailstoneSeq :: Integer -> [Integer]
hailstoneSeq 1 = [1]
hailstoneSeq n = n : hailstoneSeq (hailStone n)

-- Compute the length of the list of integer
intListLength :: [Integer] -> Integer
intListLength []     = 0
intListLength (x:xs) = 1 + intListLength xs
-- in above code, since we're not using x it can be replaced with intListLength (_:xs) = 1 + intListLength xs

-- Sum every pair element in a list
sumEveryTwo :: [Integer] -> [Integer]
sumEveryTwo []         = [] -- do nothing with an empty list
sumEveryTwo (x:[])     = [x] -- do nothing to a list with just one element
sumEveryTwo (x:(y:zs)) = (x + y) : sumEveryTwo zs

double nums =
  if null nums
  then []
  else 2 * head nums : double (tail nums)

removeOdd nums =
  if null nums
     then []
  else
    if mod (head nums) 2 == 0
       then head nums : removeOdd (tail nums)
    else removeOdd (tail nums)

data FailableDouble = Failure | Ok Double
  deriving Show

data Thing = Shoe
           | Ship
           | SealingWax
           | Cabbage
           | King
  deriving Show

data Person = Person String Int Thing
  deriving Show

brent :: Person
brent = Person "Brent" 31 SealingWax

stan :: Person
stan = Person "Stan" 94 Cabbage

getAge :: Person -> Int
getAge (Person _ a _) = a

maybeHead :: [a] -> Maybe a
maybeHead []     = Nothing
maybeHead (x:xs) = Just x

const :: a -> b -> a
const a _ = a

length = foldr ((+) . const 1) 0

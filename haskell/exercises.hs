myMultiply :: Int -> Int -> Int -> Int -> Int
myMultiply w x y z = w * x * y * z

myList :: [Int]
myList = [1,2,3]

-- a can be any type
myHead :: [a] -> a
myHead (x:xs) = x

headItem = myHead [1,2,3]

-- myLength is a function that can accept list of any type and return its length as Int
myLength :: [a] -> Int
myLength []     = 0
myLength (x:xs) = 1 + myLength xs


myMap :: (a -> b) -> [a] -> [b]
myMap f []     = []
myMap f (x:xs) = f x : myMap f xs

myFloat :: Double
myFloat = 1.1

data SomeJunk = Rubbish String | Trashpile String Int Bool
  deriving Show
discards :: SomeJunk
discards = Trashpile "JunkYard" 42 True

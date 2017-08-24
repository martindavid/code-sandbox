-- main = print "hello, world"

data Thing = Shoe
           | Ship
           | SealingWax
           | Cabbage
           | King
  deriving Show

shoe :: Thing
shoe = Shoe

data FailableDouble = Failure
                    | OK Double
  deriving Show

ex01 = Failure
ex02 = OK 3.4

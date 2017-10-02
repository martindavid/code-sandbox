module Lab1 (subst, interleave, unroll) where

-- Question 1
-- subst takes two values and a list, and replaces every occurrence
-- of the first value with the second in the list
subst :: (Eq t) => t -> t -> [t] -> [t]
subst _ _ [] = []
subst a b (x:xs)
  | a == x = b : subst a b xs
  | otherwise = x : subst a b xs

-- Question 2
-- interleave takes two lists and returns the interleaving of the two arguments. That, the
-- result is a list in which the first, third, fifth . . . elements come fromt the first argument
-- and the second, fourth, sixth . . . come from second. If either argument is shorter than
-- the other, the excess elements of the longer comprise the end of the resulting list
interleave :: [t] -> [t] -> [t]
interleave a []          = a
interleave [] b          = b
interleave (x:xs) (y:ys) = x : y : interleave xs ys


-- Question 3
-- unroll takes a list and an integer and constructs a list of the specified length made up
-- by “unrolling” the input list as many times as needed to construct a list of that length.
-- That is, the output consists of the input list repeated as many times as necessary to
-- have the specified length
unroll :: Int -> [a] -> [a]
unroll _ [] = []
unroll n a
  | n <= 0 = []
  | n > length a = a ++ unroll (n - length a) a
unroll n (x:xs) = x : unroll (n - 1) xs

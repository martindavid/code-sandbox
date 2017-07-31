main = do 
  putStrLn "What is your name?"
  name <- getLine
  putStrLn $ name ++ "! this is a very nice name"
  putStrLn "Where are you come from?"
  city <- getLine
  putStrLn $ "Hey I love " ++ city ++ "!"

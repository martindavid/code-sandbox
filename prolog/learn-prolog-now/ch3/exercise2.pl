definitely_greater(succ(X), X).
greater_than(X, Y) :- definitely_greater(X,Y).
greater_than(X, Y) :- definitely_greater(X,Z), greater_than(Z, Y).

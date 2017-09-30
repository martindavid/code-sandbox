directIn(katarina, olga).
directIn(olga, natsha).
directIn(natsha, irina).

in(X,Y) :- directIn(X,Y).
in(X,Y) :- directIn(X,Z), in(Z, Y).

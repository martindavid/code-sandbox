% Q2
borders(spain,X),borders(france,X).

% Q3
borders(spain,X),borders(france,X),country(X,_,_,_,_,_,_,_,_).

% Q4
country(C) :- country(X,_,_,_,_,_,_,_,_).
borders(spain,X),borders(france,X),country(X).

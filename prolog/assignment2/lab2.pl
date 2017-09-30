% Author:   Martin Valentino
% Purpose:  Solution for assignment 2, COMP90048 - Declarative Programming
% 
% This program contain solutions to three problem case in Lab2 assignment


% a predicate that holds when in one place where list L1 has the value E1, L2 has E2.
% construct: correspond(E1, L1, E2, L2)

correspond(E1,[E1|_T1],E2,[E2|_T2]).
correspond(E1,[_H1|T1],E2,[_H2|T2]) :-
    correspond(E1,T1,E2,T2).


% a predicate that holds when Ls is a list of lists, and L is a list of all the elements
% of all the lists in Ls, interleaved.
% The case where the first argument consists of non-empty lists    
interleave([[Head|Tail]|X], [Head|Y]):-
    append(X, [Tail], X2),
    interleave(X2, Y).

% Base case in which first argument is a list of empty lists
interleave([], []).
interleave([[]|T], []) :-
    interleave(T, []).



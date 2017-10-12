% Question 1
list_of(_, []).
list_of(Elt, [Elt|Tail]) :-
  list_of(Elt, Tail).


% Question 2
all_same([Head|Tail]) :- list_of(Head, Tail).

% Question 3
adjacent(E1, E2, List) :- 
  append(_, [E1,E2|_], List).

% Question 4
adjacent(E1, E2, [E1,E2|_]).
adjacent(E1, E2, [Head|Tail]) :- 
  adjacent(E1,E2, Tail).


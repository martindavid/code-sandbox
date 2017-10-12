:- use_module(library(clpfd)).

unique([X]).
unique([X,X1|Tail]).

list_sum([X], X).
list_sum([X,Y | Tail], Result) :-
  Head is X+Y,
  list_sum([Head | Tail], Result).

list_product([X], X).
list_product([X, Y | Tail], Result) :-
  Head is X*Y,
  list_product([Head | Tail], Result).


solver(Rows, Sol) :-
  append(Rows, Vs), Vs ins 1..9,
  maplist(all_distinct,Rows),
  transpose(Rows, Columns),
  maplist(all_distinct,Columns),
  maplist(label, Rows).


valid(L) :- L ins 1..9, all_distinct(L).

foo(X) :- X in 1..3.
foo(X) :- X in 5..7.
foo(X) :- X in 8..12.


%% Code from this tutorial http://www.pathwayslms.com/swipltuts/clpfd/clpfd.html

puzzle([S,E,N,D] + [M,O,R,E] = [M,O,N,E,Y]) :-
  Vars = [S,E,N,D,M,O,R,Y],
  Vars ins 0..9,
  all_different(Vars),
  S*1000 + E*100 + N*10 + D +
  M*1000 + O*100 + R*10 + E #=
  M*10000 + O*1000 + N*100 + E*10 + Y,
  M #\= 0, S#\=0,
  label(Vars).

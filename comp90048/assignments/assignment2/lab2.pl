% Author:   Martin Valentino
% Purpose:  Solution for assignment 2, COMP90048 - Declarative Programming
% 
% This program contain solutions to three problem case in Lab2 assignment


% a predicate that holds when in one place where list L1 has the value E1, L2 has E2.
% construct: correspond(E1, L1, E2, L2)

correspond(E1,[E1|_],E2,[E2|_]).
correspond(E1,[_|T1],E2,[_|T2]) :-
    correspond(E1,T1,E2,T2).


% a predicate that holds when Ls is a list of lists, and L is a list of all the elements
% of all the lists in Ls, interleaved.
interleave([], []).
interleave([[]|T], []) :- interleave(T, []).
interleave([[Head|Tail]|X], [Head|Y]):-
    append(X, [Tail], X2),
    interleave(X2, Y).



partial_eval(Expr0, Var, Val, Expr) :-
   evaluate(Expr0,[Var:Val],Expr).

evaluate(Exp, ListExpr, Val) :-
   parse(ListExpr, Exp, ParsedExpr),
   Val is ParsedExpr.

parse(ListExpr, Term, R) :-
   functor(Term, Term, 0), !,
   ( member(Term : V, ListExpr) ->  R = V ; R = Term ).

parse(ListExpr, Term, V) :-
   functor(Term, Name, _),
   Term =.. [Name | Args],
   maplist(parse(ListExpr), Args, Args2),
   V =.. [Name| Args2].

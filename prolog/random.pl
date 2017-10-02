
partial_eval(X,X,Y,Y) :- atom(X).

compose(Expr, V) :- evaluate(Expr, V).
evaluate(Expr, R) :-
  Term =.. [Expr].


test(X) :-

  (   atom(X) ; number(X)

  -> print(is_true)

  ;   print(is_false)

  ).


partial_eval(Expr0, Var, Val, Expr) :-
  Expr = Expr0.


eval2(E, R) :-
   isexpr(E),
   R is E.

isexpr(BinOp) :-
   BinOp =.. [F,L,R],
   admissibleop(F),
   isexpr(L),
   isexpr(R).
isexpr(N) :-
   number(N).

admissibleop(*).
admissibleop(+).
% admissibleop(/).
admissibleop(-).




exp_symbols(Symbols, Expr, WithSym) :-
    Expr =.. [F|Args],
    ( memberchk(F:V, Symbols) -> G = V ; G = F ),
    maplist(exp_symbols(Symbols), Args, ArgsSWithSym),
    WithSym =.. [G|ArgsSWithSym].

evaluate(Exp, LstVars, Val) :-
    exp_symbols(LstVars, Exp, NewExp),
    (Val is NewExp ; Val = NewExp).


expression_result(n(N), _, _, n(N)).
expression_result(a(A), A, N, n(N)).
expression_result(a(A), Var, _, a(A)) :-
        dif(A, Var).
expression_result(X+Y, Var, Val, R) :-
        expression_result(X, Var, Val, RX),
        expression_result(Y, Var, Val, RY),
        addition(RX, RY, R).
expression_result(X*Y, Var, Val, R) :-
        expression_result(X, Var, Val, RX),
        expression_result(Y, Var, Val, RY),
        product(RX, RY, R).

addition(n(X), n(Y), n(Z)) :- Z = X + Y.
addition(a(X), Y, a(X)+Y).
addition(X, a(Y), X+a(Y)).

product(n(X), n(Y), n(Z)) :- Z = X * Y.
addition(a(X), Y, a(X)*Y).
addition(X, a(Y), X*a(Y)).

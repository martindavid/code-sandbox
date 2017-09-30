:- ensure_loaded(borders).
:- ensure_loaded(cities).
:- ensure_loaded(countries).
:- ensure_loaded(rivers).

country(C) :- country(C,_,_,_,_,_,_,_).

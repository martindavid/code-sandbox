:- ensure_loaded(borders).
:- ensure_loaded(cities).
:- ensure_loaded(countries).
:- ensure_loaded(rivers).


% Workshop 07
%
% Question 2
% borders(spain, X), borders(france, X).


% Question 3
% borders(spain,X),borders(france,X),country(X,_,_,_,_,_,_,_).

% Question 4
country(C) :- country(C,_,_,_,_,_,_,_).

% Question 5
larger(Country1, Country2) :-
  country(Country1,_,_,_,Area1,_,_,_),
  country(Country2,_,_,_,Area2,_,_,_),
  Area1 > Area2.


% Question 6
river_country(River, Country) :-
  river(River, X),
  member(Country, X).


country_region(Country, Region) :-
  country(Country,Region,_,_,_,_,_,_).

% 

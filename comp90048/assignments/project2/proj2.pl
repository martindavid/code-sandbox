% COMP90048 Declarative Programming
% Martin Valentino 


% Math Puzzles
% To solve small mathematical number puzzles. The number puzzle can be described as a grid of 
% squares, each to be filled with a single digit 1-9 satisfying the following constraints:
%     -Each row & each column have no repeated digits
%     -all squares on the diagonal line form the upper left to lower right contain the same values
%     -The heading of each row and column hold either the sum or the product of all the 
%           digits in that row or column

% An Example puzzle              The Puzzle solved  

%     14 | 10 | 35                  | 14 |10 | 35
% 14 |   |    |                  14 | 7  | 2 | 1
% 15 |   |    |                  15 | 3  | 7 | 5
% 28 |   |    |                  28 | 4  | 1 | 7

% Note: the row and column headings are given and do not have any constraints.

% The program was to be able 2x2,3x3,4x4 puzzles.

:- use_module(library(clpfd)).


% Pattern matching for 2*2 puzzle
puzzle_solution([_,C1,C2], [H1| H1Tail],[H2 | H2Tail]).



% Pattern matching for 3*3 puzzle
puzzle_solution([_,C1,C2,C3],[H1 | H1Tail],[H2 | H2Tail],[H3 | H3Tail]).

% Pattern matching for 4*4 puzzle
puzzle_solution([_,C1,C2,C3,C4], [H1 | H1Tail],[H2 | H2Tail],[H3 | H3Tail], [H4 | H4Tail]).

is_sum(X, List, Sol) :-
  List ins 1..9,
  sum(List, #=, X),
  Sol = List.

is_product(X, List, Sol) :-
  List ins 1..9,
  label(List),
  list_product(List,Y),
  X #= Y.

list_product([X], X).
list_product([X, Y | Tail], Result) :-
  Head is X*Y,
  list_product([Head | Tail], Result).

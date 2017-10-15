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


% The program was to be able 2x2,3x3,4x4 puzzles.

:- use_module(library(clpfd)).

% The predicate to find a solution to a math puzzle that
% fulfil the constraints :
%     -Each row & each column have no repeated digits
%     -all squares on the diagonal line form the upper left to lower right contain the same values
%     -The heading of each row and column hold either the sum or the product of all the 
%           digits in that row or column
%
% All the predicate below in sequence:
% - first check that the diagonal element is valid
% - second check that the rows element is either product/sum of the head of list
% - third transpose the rows and check it against product/sum rules
% - lastly, label the list with the value
puzzle_solution([Head|Tail]) :-
  is_valid_diagonal(Tail, 1, _),
  is_valid_row(Tail),
  transpose([Head|Tail], [_|TransposeTail]),
  is_valid_row(TransposeTail),
  maplist(label, [Head|Tail]).


% Validate that all of diagonal element in matrix (except header) is similar
% recursively match the element in the list using nth0 predicate start from
% index 1
is_valid_diagonal([], _,_).
is_valid_diagonal( [Head|Tail] , N, Elem):-
    nth0(N, Head , Elem),
    N0 #= N+1,
    is_valid_diagonal(Tail, N0, Elem).


% Check whether row element meets the constraint:
% - all distinct
% - fulfil the constraint in compute_row predicate
is_valid_row([]).
is_valid_row([Head|Tail]) :-
  compute_row(Head),
  all_distinct(Head),
  is_valid_row(Tail).


% Compute variable in List so it meets with the constraint:
% - the sum of all Tail element in List equal to element in Head, or
% - the product of all Tail element in List equal to element in Head
compute_row([Head|Tail]) :-
  is_sum(Tail, Head);
  is_product(Tail, Head).

% Check if sum of all element in List equal to Total
% Put a constraint for a variable so it will only fit in
% digit 1 to 9
is_sum(List, Total) :-
  List ins 1..9,
  sum(List, #=, Total).

% Check if product of all element in List equal to Total
% Put a constraint for a variable so it will only fit in
% digit 1 to 9
is_product(List, Total) :-
  List ins 1..9,
  label(List),
  product(List,Y),
  Total #= Y.

% Generate a product result of all element in List
product([X], X).
product([X, Y | Tail], Result) :-
  Head #= X*Y,
  product([Head | Tail], Result).

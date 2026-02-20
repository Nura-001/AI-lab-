% ---------------------------
% Male and Female facts
% ---------------------------

male(nazmul).
male(karim).
male(jakir).
male(akib).

female(aliya).
female(salma).
female(nasrin).
female(mitu).

% ---------------------------
% Parent facts
% ---------------------------

father(nazmul, jakir).
mother(aliya, jakir).

father(nazmul, nasrin).
mother(aliya, nasrin).

father(jakir, akib).

mother(nasrin, mitu).
father(karim, mitu).
mother(salma, mitu).

% ---------------------------
% Rules
% ---------------------------

% Parent rule
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Sibling rule
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% ---------------------------
% Likes / Dislikes
% ---------------------------

likes(nazmul, tea).
likes(nazmul, football).
likes(karim, coffee).

dislikes(nazmul, smoking).
dislikes(karim, tea).

% Friend rule
friend(X, Y) :-
    likes(X, Z),
    likes(Y, Z),
    X \= Y.

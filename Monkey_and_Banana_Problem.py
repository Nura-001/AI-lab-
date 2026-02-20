% ---------------------------
% Move the monkey from one place to another
% ---------------------------
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)) :- !.
% '!' stops Prolog from backtracking over other move options once this rule succeeds

% ---------------------------
% Climb onto the box if at the box location
% ---------------------------
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)) :- !.
% Once the monkey climbs, no need to try another 'climb' for same state

% ---------------------------
% Grab the bananas if on the box and at banana's location
% ---------------------------
move(state(P, onbox, P, hasnot), grasp, state(P, onbox, P, has)) :- !.
% When monkey grabs bananas, commit to this move

% ---------------------------
% Goal test: monkey has the bananas
% ---------------------------
canget(state(_, _, _, has)) :- !.
% Cut here ensures Prolog stops searching once goal is reached

% ---------------------------
% Recursive planning: try moves until goal is reached
% ---------------------------
canget(State1) :-
    move(State1, Action, State2),
    writeln(Action),  % Print the move
    canget(State2).

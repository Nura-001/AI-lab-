% Base case: Move a single disk
move(1, Source, Target, _) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    writeln(Target).

% Recursive case: Move N disks
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,

    % Step 1: Move N-1 disks to Auxiliary
    move(M, Source, Auxiliary, Target),

    % Step 2: Move largest disk to Target
    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    writeln(Target),

    % Step 3: Move N-1 disks from Auxiliary to Target
    move(M, Auxiliary, Target, Source).

sum(N,R) :- sum(N,0,R).

sum(0,R,R).

sum(N,T,R) :-
 N>0,
 T1 is T+N,
 N1 is N-1,
 sum(N1,T1,R)
.

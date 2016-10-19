factorial(N,F) :- N>0, N1 is N-1,
factorial(N1,F1), F is N * F1.

fibonacci(A,B) :-  
           A > 1,
           C is A-1,
           E is A-2,	
           fibonacci(C,D1),
           fibonacci(E,D2),
           B is D1+D2.

fib_sequence(A,B,[H|T]) :-
    A =< B                   /* Make sure A is less than or equal to B */
,   fib(A, H)                /* Produce the head value from fib(A,...) */
,   AA is A + 1              /* Produce A+1 */
,   fib_sequence(AA, B, T).  /* Produce the rest of the list */

mother(lila,mona).
alive(lila,mona).
parent(X,Y) :- mother(X,Y).
older(X,Y):-parent(X,Y),alive(X).
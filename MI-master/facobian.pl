factorial(N,F) :- N>0, N1 is N-1,
factorial(N1,F1), F is N * F1.

fibonacci(A,B) :-  
           A > 1,
           C is A-1,
           E is A-2,	
           fibonacci(C,D1),
           fibonacci(E,D2),
           B is D1+D2.

           
(define (problem manytireworldprob)
                   (:domain manytireworld)
                   (:objects l-1-1 l-1-2 l-1-3 l-1-4 l-1-5 l-1-6 l-1-7 l-2-1 l-2-2 l-2-3 l-2-4 l-2-5 l-2-6 l-2-7 l-3-1 l-3-2 l-3-3 l-3-4 l-3-5 l-3-6 l-3-7 l-4-1 l-4-2 l-4-3 l-4-4 l-4-5 l-4-6 l-4-7 l-5-1 l-5-2 l-5-3 l-5-4 l-5-5 l-5-6 l-5-7 l-6-1 l-6-2 l-6-3 l-6-4 l-6-5 l-6-6 l-6-7 l-7-1 l-7-2 l-7-3 l-7-4 l-7-5 l-7-6 l-7-7 - location)
                   (:init (vehicle-at l-1-1)(road l-1-1 l-1-2)(road l-1-2 l-1-3)(road l-1-3 l-1-4)(road l-1-4 l-1-5)(road l-1-5 l-1-6)(road l-1-6 l-1-7)(road l-1-1 l-2-1)(road l-1-2 l-2-2)(road l-1-3 l-2-3)(road l-1-4 l-2-4)(road l-1-5 l-2-5)(road l-1-6 l-2-6)(road l-2-1 l-1-2)(road l-2-2 l-1-3)(road l-2-3 l-1-4)(road l-2-4 l-1-5)(road l-2-5 l-1-6)(road l-2-6 l-1-7)(spare-in l-2-1)(spare-in l-2-2)(spare-in l-2-3)(spare-in l-2-4)(spare-in l-2-5)(spare-in l-2-6)(road l-3-1 l-3-2)(road l-3-2 l-3-3)(road l-3-3 l-3-4)(road l-3-4 l-3-5)(road l-2-1 l-3-1)(road l-2-3 l-3-3)(road l-2-5 l-3-5)(road l-3-1 l-2-2)(road l-3-3 l-2-4)(road l-3-5 l-2-6)(spare-in l-3-1)(spare-in l-3-5)(road l-3-1 l-4-1)(road l-3-2 l-4-2)(road l-3-3 l-4-3)(road l-3-4 l-4-4)(road l-4-1 l-3-2)(road l-4-2 l-3-3)(road l-4-3 l-3-4)(road l-4-4 l-3-5)(spare-in l-4-1)(spare-in l-4-2)(spare-in l-4-3)(spare-in l-4-4)(road l-5-1 l-5-2)(road l-5-2 l-5-3)(road l-4-1 l-5-1)(road l-4-3 l-5-3)(road l-5-1 l-4-2)(road l-5-3 l-4-4)(spare-in l-5-1)(spare-in l-5-3)(road l-5-1 l-6-1)(road l-5-2 l-6-2)(road l-6-1 l-5-2)(road l-6-2 l-5-3)(spare-in l-6-1)(spare-in l-6-2)(road l-6-1 l-7-1)(road l-7-1 l-6-2)(spare-in l-7-1)(spare-in l-7-1)(not-flattire))
                   (:goal (and (vehicle-at l-4-4))))
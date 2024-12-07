(define (problem doors) 
    (:domain doors)


    (:objects
	key-1 - key
	key-2 - key
	key-3 - key
	key-4 - key
	key-5 - key
	key-6 - key
	key-7 - key
	key-8 - key
	key-9 - key
	loc-0-0 - location
	loc-0-1 - location
	loc-0-2 - location
	loc-0-3 - location
	loc-0-4 - location
	loc-0-5 - location
	loc-0-6 - location
	loc-0-7 - location
	loc-1-0 - location
	loc-1-1 - location
	loc-1-2 - location
	loc-1-3 - location
	loc-1-4 - location
	loc-1-5 - location
	loc-1-6 - location
	loc-1-7 - location
	loc-2-0 - location
	loc-2-1 - location
	loc-2-2 - location
	loc-2-3 - location
	loc-2-4 - location
	loc-2-5 - location
	loc-2-6 - location
	loc-2-7 - location
	loc-3-0 - location
	loc-3-1 - location
	loc-3-2 - location
	loc-3-3 - location
	loc-3-4 - location
	loc-3-5 - location
	loc-3-6 - location
	loc-3-7 - location
	loc-4-0 - location
	loc-4-1 - location
	loc-4-2 - location
	loc-4-3 - location
	loc-4-4 - location
	loc-4-5 - location
	loc-4-6 - location
	loc-4-7 - location
	loc-5-0 - location
	loc-5-1 - location
	loc-5-2 - location
	loc-5-3 - location
	loc-5-4 - location
	loc-5-5 - location
	loc-5-6 - location
	loc-5-7 - location
	loc-6-0 - location
	loc-6-1 - location
	loc-6-2 - location
	loc-6-3 - location
	loc-6-4 - location
	loc-6-5 - location
	loc-6-6 - location
	loc-6-7 - location
	loc-7-0 - location
	loc-7-1 - location
	loc-7-2 - location
	loc-7-3 - location
	loc-7-4 - location
	loc-7-5 - location
	loc-7-6 - location
	loc-7-7 - location
	
	room-0 - room
	room-1 - room
	room-2 - room
	room-3 - room
	room-4 - room
	room-5 - room
	room-6 - room
	room-7 - room
	room-8 - room
	room-9 - room
	room-10 - room
	person-1 - person
	fire-1 - fire
	fire-2 - fire
	fire-3 - fire
	fire-4 - fire
	fire-5 - fire
	fire-6 - fire
	fire-7 - fire
	fire-8 - fire
	wall-1 - wall
	wall-2 - wall
	wall-3 - wall
	wall-4 - wall
	wall-5 - wall
	wall-6 - wall
	wall-7 - wall
	wall-8 - wall
	wall-9 - wall
	wall-10 - wall
	wall-11 - wall
	wall-12 - wall
	wall-13 - wall
	wall-14 - wall

    )

    (:init
    (at loc-0-0)
	(adjacent loc-0-0 loc-0-1)
	(adjacent loc-0-0 loc-1-0)
	(adjacent loc-0-1 loc-0-0)
	(adjacent loc-0-1 loc-0-2)
	(adjacent loc-0-1 loc-1-1)
	(adjacent loc-0-2 loc-0-1)
	(adjacent loc-0-2 loc-0-3)
	(adjacent loc-0-2 loc-1-2)
	(adjacent loc-0-3 loc-0-2)
	(adjacent loc-0-3 loc-0-4)
	(adjacent loc-0-3 loc-1-3)
	(adjacent loc-0-4 loc-0-3)
	(adjacent loc-0-4 loc-0-5)
	(adjacent loc-0-4 loc-1-4)
	(adjacent loc-0-5 loc-0-4)
	(adjacent loc-0-5 loc-0-6)
	(adjacent loc-0-5 loc-1-5)
	(adjacent loc-0-6 loc-0-5)
	(adjacent loc-0-6 loc-0-7)
	(adjacent loc-0-6 loc-1-6)
	(adjacent loc-0-7 loc-0-6)
	(adjacent loc-0-7 loc-1-7)
	(adjacent loc-1-0 loc-0-0)
	(adjacent loc-1-0 loc-1-1)
	(adjacent loc-1-0 loc-2-0)
	(adjacent loc-1-1 loc-0-1)
	(adjacent loc-1-1 loc-1-0)
	(adjacent loc-1-1 loc-1-2)
	(adjacent loc-1-1 loc-2-1)
	(adjacent loc-1-2 loc-0-2)
	(adjacent loc-1-2 loc-1-1)
	(adjacent loc-1-2 loc-1-3)
	(adjacent loc-1-2 loc-2-2)
	(adjacent loc-1-3 loc-0-3)
	(adjacent loc-1-3 loc-1-2)
	(adjacent loc-1-3 loc-1-4)
	(adjacent loc-1-3 loc-2-3)
	(adjacent loc-1-4 loc-0-4)
	(adjacent loc-1-4 loc-1-3)
	(adjacent loc-1-4 loc-1-5)
	(adjacent loc-1-4 loc-2-4)
	(adjacent loc-1-5 loc-0-5)
	(adjacent loc-1-5 loc-1-4)
	(adjacent loc-1-5 loc-1-6)
	(adjacent loc-1-5 loc-2-5)
	(adjacent loc-1-6 loc-0-6)
	(adjacent loc-1-6 loc-1-5)
	(adjacent loc-1-6 loc-1-7)
	(adjacent loc-1-6 loc-2-6)
	(adjacent loc-1-7 loc-0-7)
	(adjacent loc-1-7 loc-1-6)
	(adjacent loc-1-7 loc-2-7)
	(adjacent loc-2-0 loc-1-0)
	(adjacent loc-2-0 loc-2-1)
	(adjacent loc-2-0 loc-3-0)
	(adjacent loc-2-1 loc-1-1)
	(adjacent loc-2-1 loc-2-0)
	(adjacent loc-2-1 loc-2-2)
	(adjacent loc-2-1 loc-3-1)
	(adjacent loc-2-2 loc-1-2)
	(adjacent loc-2-2 loc-2-1)
	(adjacent loc-2-2 loc-2-3)
	(adjacent loc-2-2 loc-3-2)
	(adjacent loc-2-3 loc-1-3)
	(adjacent loc-2-3 loc-2-2)
	(adjacent loc-2-3 loc-2-4)
	(adjacent loc-2-3 loc-3-3)
	(adjacent loc-2-4 loc-1-4)
	(adjacent loc-2-4 loc-2-3)
	(adjacent loc-2-4 loc-2-5)
	(adjacent loc-2-4 loc-3-4)
	(adjacent loc-2-5 loc-1-5)
	(adjacent loc-2-5 loc-2-4)
	(adjacent loc-2-5 loc-2-6)
	(adjacent loc-2-5 loc-3-5)
	(adjacent loc-2-6 loc-1-6)
	(adjacent loc-2-6 loc-2-5)
	(adjacent loc-2-6 loc-2-7)
	(adjacent loc-2-6 loc-3-6)
	(adjacent loc-2-7 loc-1-7)
	(adjacent loc-2-7 loc-2-6)
	(adjacent loc-2-7 loc-3-7)
	(adjacent loc-3-0 loc-2-0)
	(adjacent loc-3-0 loc-3-1)
	(adjacent loc-3-0 loc-4-0)
	(adjacent loc-3-1 loc-2-1)
	(adjacent loc-3-1 loc-3-0)
	(adjacent loc-3-1 loc-3-2)
	(adjacent loc-3-1 loc-4-1)
	(adjacent loc-3-2 loc-2-2)
	(adjacent loc-3-2 loc-3-1)
	(adjacent loc-3-2 loc-3-3)
	(adjacent loc-3-2 loc-4-2)
	(adjacent loc-3-3 loc-2-3)
	(adjacent loc-3-3 loc-3-2)
	(adjacent loc-3-3 loc-3-4)
	(adjacent loc-3-3 loc-4-3)
	(adjacent loc-3-4 loc-2-4)
	(adjacent loc-3-4 loc-3-3)
	(adjacent loc-3-4 loc-3-5)
	(adjacent loc-3-4 loc-4-4)
	(adjacent loc-3-5 loc-2-5)
	(adjacent loc-3-5 loc-3-4)
	(adjacent loc-3-5 loc-3-6)
	(adjacent loc-3-5 loc-4-5)
	(adjacent loc-3-6 loc-2-6)
	(adjacent loc-3-6 loc-3-5)
	(adjacent loc-3-6 loc-3-7)
	(adjacent loc-3-6 loc-4-6)
	(adjacent loc-3-7 loc-2-7)
	(adjacent loc-3-7 loc-3-6)
	(adjacent loc-3-7 loc-4-7)
	(adjacent loc-4-0 loc-3-0)
	(adjacent loc-4-0 loc-4-1)
	(adjacent loc-4-0 loc-5-0)
	(adjacent loc-4-1 loc-3-1)
	(adjacent loc-4-1 loc-4-0)
	(adjacent loc-4-1 loc-4-2)
	(adjacent loc-4-1 loc-5-1)
	(adjacent loc-4-2 loc-3-2)
	(adjacent loc-4-2 loc-4-1)
	(adjacent loc-4-2 loc-4-3)
	(adjacent loc-4-2 loc-5-2)
	(adjacent loc-4-3 loc-3-3)
	(adjacent loc-4-3 loc-4-2)
	(adjacent loc-4-3 loc-4-4)
	(adjacent loc-4-3 loc-5-3)
	(adjacent loc-4-4 loc-3-4)
	(adjacent loc-4-4 loc-4-3)
	(adjacent loc-4-4 loc-4-5)
	(adjacent loc-4-4 loc-5-4)
	(adjacent loc-4-5 loc-3-5)
	(adjacent loc-4-5 loc-4-4)
	(adjacent loc-4-5 loc-4-6)
	(adjacent loc-4-5 loc-5-5)
	(adjacent loc-4-6 loc-3-6)
	(adjacent loc-4-6 loc-4-5)
	(adjacent loc-4-6 loc-4-7)
	(adjacent loc-4-6 loc-5-6)
	(adjacent loc-4-7 loc-3-7)
	(adjacent loc-4-7 loc-4-6)
	(adjacent loc-4-7 loc-5-7)
	(adjacent loc-5-0 loc-4-0)
	(adjacent loc-5-0 loc-5-1)
	(adjacent loc-5-0 loc-6-0)
	(adjacent loc-5-1 loc-4-1)
	(adjacent loc-5-1 loc-5-0)
	(adjacent loc-5-1 loc-5-2)
	(adjacent loc-5-1 loc-6-1)
	(adjacent loc-5-2 loc-4-2)
	(adjacent loc-5-2 loc-5-1)
	(adjacent loc-5-2 loc-5-3)
	(adjacent loc-5-2 loc-6-2)
	(adjacent loc-5-3 loc-4-3)
	(adjacent loc-5-3 loc-5-2)
	(adjacent loc-5-3 loc-5-4)
	(adjacent loc-5-3 loc-6-3)
	(adjacent loc-5-4 loc-4-4)
	(adjacent loc-5-4 loc-5-3)
	(adjacent loc-5-4 loc-5-5)
	(adjacent loc-5-4 loc-6-4)
	(adjacent loc-5-5 loc-4-5)
	(adjacent loc-5-5 loc-5-4)
	(adjacent loc-5-5 loc-5-6)
	(adjacent loc-5-5 loc-6-5)
	(adjacent loc-5-6 loc-4-6)
	(adjacent loc-5-6 loc-5-5)
	(adjacent loc-5-6 loc-5-7)
	(adjacent loc-5-6 loc-6-6)
	(adjacent loc-5-7 loc-4-7)
	(adjacent loc-5-7 loc-5-6)
	(adjacent loc-5-7 loc-6-7)
	(adjacent loc-6-0 loc-5-0)
	(adjacent loc-6-0 loc-6-1)
	(adjacent loc-6-0 loc-7-0)
	(adjacent loc-6-1 loc-5-1)
	(adjacent loc-6-1 loc-6-0)
	(adjacent loc-6-1 loc-6-2)
	(adjacent loc-6-1 loc-7-1)
	(adjacent loc-6-2 loc-5-2)
	(adjacent loc-6-2 loc-6-1)
	(adjacent loc-6-2 loc-6-3)
	(adjacent loc-6-2 loc-7-2)
	(adjacent loc-6-3 loc-5-3)
	(adjacent loc-6-3 loc-6-2)
	(adjacent loc-6-3 loc-6-4)
	(adjacent loc-6-3 loc-7-3)
	(adjacent loc-6-4 loc-5-4)
	(adjacent loc-6-4 loc-6-3)
	(adjacent loc-6-4 loc-6-5)
	(adjacent loc-6-4 loc-7-4)
	(adjacent loc-6-5 loc-5-5)
	(adjacent loc-6-5 loc-6-4)
	(adjacent loc-6-5 loc-6-6)
	(adjacent loc-6-5 loc-7-5)
	(adjacent loc-6-6 loc-5-6)
	(adjacent loc-6-6 loc-6-5)
	(adjacent loc-6-6 loc-6-7)
	(adjacent loc-6-6 loc-7-6)
	(adjacent loc-6-7 loc-5-7)
	(adjacent loc-6-7 loc-6-6)
	(adjacent loc-6-7 loc-7-7)
	(adjacent loc-7-0 loc-7-1)
	(adjacent loc-7-0 loc-6-0)
	(adjacent loc-7-1 loc-6-1)
	(adjacent loc-7-1 loc-7-0)
	(adjacent loc-7-1 loc-7-2)
	(adjacent loc-7-2 loc-6-2)
	(adjacent loc-7-2 loc-7-1)
	(adjacent loc-7-2 loc-7-3)
	(adjacent loc-7-3 loc-6-3)
	(adjacent loc-7-3 loc-7-2)
	(adjacent loc-7-3 loc-7-4)
	(adjacent loc-7-4 loc-6-4)
	(adjacent loc-7-4 loc-7-3)
	(adjacent loc-7-4 loc-7-5)
	(adjacent loc-7-5 loc-6-5)
	(adjacent loc-7-5 loc-7-4)
	(adjacent loc-7-5 loc-7-6)
	(adjacent loc-7-6 loc-6-6)
	(adjacent loc-7-6 loc-7-5)
	(adjacent loc-7-6 loc-7-7)
	(adjacent loc-7-7 loc-6-7)
	(adjacent loc-7-7 loc-7-6)
	(unlocked room-0)
	
	(unlocked room-3)
	(unlocked room-4)
	(unlocked room-5)
	(locinroom loc-0-0 room-0)
	(moveto loc-0-0)
	(locinroom loc-0-1 room-0)
	(moveto loc-0-1)
	(locinroom loc-0-2 room-0)
	(moveto loc-0-2)
	(locinroom loc-0-3 room-0)
	(moveto loc-0-3)
	(locinroom loc-0-4 room-0)
	(moveto loc-0-4)
	(locinroom loc-0-5 room-0)
	(moveto loc-0-5)
	(locinroom loc-0-6 room-0)
	(moveto loc-0-6)
	(locinroom loc-0-7 room-0)
	(moveto loc-0-7)
	(locinroom loc-1-0 room-0)
	(moveto loc-1-0)
	(locinroom loc-1-1 room-0)
	(moveto loc-1-1)
	(locinroom loc-1-2 room-0)
	(moveto loc-1-2)
	(locinroom loc-1-3 room-0)
	(moveto loc-1-3)
	(locinroom loc-1-4 room-0)
	(moveto loc-1-4)
	(locinroom loc-1-5 room-0)
	(moveto loc-1-5)
	(locinroom loc-1-6 room-0)
	(moveto loc-1-6)
	(locinroom loc-1-7 room-0)
	(moveto loc-1-7)
	(locinroom loc-2-0 room-0)
	(moveto loc-2-0)
	(locinroom loc-2-1 room-0)
	(moveto loc-2-1)
	(locinroom loc-2-2 room-0)
	(moveto loc-2-2)
	(locinroom loc-2-3 room-0)
	(moveto loc-2-3)
	(locinroom loc-2-4 room-0)
	(moveto loc-2-4)
	(locinroom loc-2-5 room-0)
	(moveto loc-2-5)
	(locinroom loc-2-6 room-0)
	(moveto loc-2-6)
	(locinroom loc-2-7 room-0)
	(moveto loc-2-7)
	(locinroom loc-3-0 room-0)
	(moveto loc-3-0)
	(locinroom loc-3-1 room-0)
	(moveto loc-3-1)
	(locinroom loc-3-2 room-0)
	(moveto loc-3-2)
	(locinroom loc-3-3 room-0)
	(moveto loc-3-3)
	(locinroom loc-3-4 room-0)
	(moveto loc-3-4)
	(locinroom loc-3-5 room-0)
	(moveto loc-3-5)
	(locinroom loc-3-6 room-0)
	(moveto loc-3-6)
	(locinroom loc-3-7 room-0)
	(moveto loc-3-7)
	(locinroom loc-4-0 room-0)
	(moveto loc-4-0)
	(locinroom loc-4-1 room-0)
	(moveto loc-4-1)
	(locinroom loc-4-2 room-0)
	(moveto loc-4-2)
	(locinroom loc-4-3 room-0)
	(moveto loc-4-3)
	(locinroom loc-4-4 room-1)
	(moveto loc-4-4)
	(locinroom loc-4-5 room-0)
	(moveto loc-4-5)
	(locinroom loc-4-6 room-0)
	(moveto loc-4-6)
	(locinroom loc-4-7 room-0)
	(moveto loc-4-7)
    (locinroom loc-5-0 room-0)
	(moveto loc-5-0)
	(locinroom loc-5-1 room-0)
	(moveto loc-5-1)
	(locinroom loc-5-2 room-0)
	(moveto loc-5-2)
	(locinroom loc-5-3 room-0)
	(moveto loc-5-3)
	(locinroom loc-5-4 room-0)
	(moveto loc-5-4)
	(locinroom loc-5-5 room-2)
	(moveto loc-5-5)
	(locinroom loc-5-6 room-0)
	(moveto loc-5-6)
	(locinroom loc-5-7 room-0)
	(moveto loc-5-7)
	(locinroom loc-6-0 room-0)
	(moveto loc-6-0)
	(locinroom loc-6-1 room-0)
	(moveto loc-6-1)
	(locinroom loc-6-2 room-0)
	(moveto loc-6-2)
	(locinroom loc-6-3 room-0)
	(moveto loc-6-3)
	(locinroom loc-6-4 room-0)
	(moveto loc-6-4)
	(locinroom loc-6-5 room-0)
	(moveto loc-6-5)
	(locinroom loc-6-6 room-0)
	(moveto loc-6-6)
	(locinroom loc-6-7 room-0)
	(moveto loc-6-7)
	(locinroom loc-7-0 room-0)
	(moveto loc-7-0)
	(locinroom loc-7-1 room-0)
	(moveto loc-7-1)
	(locinroom loc-7-2 room-0)
	(moveto loc-7-2)
	(locinroom loc-7-3 room-0)
	(moveto loc-7-3)
	(locinroom loc-7-4 room-0)
	(moveto loc-7-4)
	(locinroom loc-7-5 room-0)
	(moveto loc-7-5)
	(locinroom loc-7-6 room-0)
	(moveto loc-7-6)
	(locinroom loc-7-7 room-0)
	(moveto loc-7-7)
	(free loc-0-1)
	(free loc-0-2)
	(free loc-0-3)
	(free loc-0-4)
	(free loc-0-5)
	(free loc-0-6)
	;		fire at 0-7, 1-0
	(free loc-1-1)
	(free loc-1-2)
	;        wall at 1-3
	; 		 wall at 1-4
	;		 wall at 1-5
	; 		 wall at 1-6
	(free loc-1-7)
	(free loc-2-0)
	(free loc-2-1)
	(free loc-2-2)
	(free loc-2-3)
	;			fire at 2-4
	(free loc-2-5)
	; 		wall at 2-6
	(free loc-2-7)
	(free loc-3-0)
	;     wall at 3-1
	(free loc-3-2)
	(free loc-3-3)
	(free loc-3-4)
	(free loc-3-5)
	;	   wall at 3-6
	(free loc-3-7)
	(free loc-4-0)
	;     wall at 4-1
	(free loc-4-2)
	(free loc-4-3)
	(free loc-4-4)
	(free loc-4-5)
	; 	    wall at 4-6
	(free loc-4-7)
	;		fire at 5-0
	;     wall at 5-1
	;		fire at 5-2, 5-3
	(free loc-5-4)
	(free loc-5-5)
	(free loc-5-6)
	(free loc-5-7)
	(free loc-6-0)
	;      wall at 6-1
	;      wall at 6-2
	;      wall at 6-3
	;      wall at 6-4
	(free loc-6-5)
	(free loc-6-6)
	(free loc-6-7)
	(free loc-7-0)
	;		fire at 7-1
	(free loc-7-2)
	(free loc-7-3)
	(free loc-7-4)
	(free loc-7-5)
	;		fire at 7-6
	(free loc-7-7)
	(keyforroom key-1 room-1)
	(keyat key-1 loc-3-3)
	(pick key-1)
	(keyforroom key-2 room-2)
	(keyat key-2 loc-4-4)
	(pick key-2)
	(personat person-1 loc-6-6)
	(fireat fire-1 loc-0-7)
	(fireat fire-2 loc-1-0)
	(fireat fire-3 loc-2-4)
	(fireat fire-4 loc-5-0)
	(fireat fire-5 loc-5-2)
	(fireat fire-6 loc-5-3)
	(fireat fire-7 loc-7-1)
	(fireat fire-8 loc-7-6)
    (wallat wall-1 loc-3-1)
	(wallat wall-2 loc-4-1)
	(wallat wall-3 loc-5-1)
	(wallat wall-4 loc-6-1)
	(wallat wall-5 loc-6-2)
	(wallat wall-6 loc-6-3)
	(wallat wall-7 loc-6-4)
	(wallat wall-8 loc-1-3)
	(wallat wall-9 loc-1-4)
	(wallat wall-10 loc-1-5)
	(wallat wall-11 loc-1-6)
	(wallat wall-12 loc-2-6)
	(wallat wall-13 loc-3-6)
	(wallat wall-14 loc-4-6)

	)

    (:goal (and (at loc-6-6)))
)
    
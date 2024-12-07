(define (problem doors) 
    (:domain doors)

    (:objects
    key-1 - key
	loc-0-0 - location
	loc-0-1 - location
	loc-0-2 - location
	loc-0-3 - location
	loc-1-0 - location
	loc-1-1 - location
	loc-1-2 - location
	loc-1-3 - location
	loc-2-0 - location
	loc-2-1 - location
	loc-2-2 - location
	loc-2-3 - location
    loc-3-0 - location
	loc-3-1 - location
	loc-3-2 - location
	loc-3-3 - location
	room-0 - room
	room-1 - room
	room-2 - room
    )

    (:init
    (at loc-0-0)
	(unlocked room-0)
	(locinroom loc-0-0 room-0)
	(moveto loc-0-0)
	(locinroom loc-0-1 room-0)
	(moveto loc-0-1)
	(locinroom loc-0-2 room-0)
	(moveto loc-0-2)
	(locinroom loc-0-3 room-0)
	(moveto loc-0-3)
	(locinroom loc-1-0 room-0)
	(moveto loc-1-0)
	(locinroom loc-1-1 room-0)
	(moveto loc-1-1)
	(locinroom loc-1-2 room-0)
	(moveto loc-1-2)
	(locinroom loc-1-3 room-0)
	(moveto loc-1-3)
    (locinroom loc-2-0 room-0)
	(moveto loc-2-0)
	(locinroom loc-2-1 room-2)
	(moveto loc-2-1)
	(locinroom loc-2-2 room-0)
	(moveto loc-2-2)
	(locinroom loc-2-3 room-0)
	(moveto loc-2-3)
	(locinroom loc-3-0 room-0)
	(moveto loc-3-0)
	(locinroom loc-3-1 room-0)
	(moveto loc-3-1)
	(locinroom loc-3-2 room-1)
	(moveto loc-3-2)
	(locinroom loc-3-3 room-1)
	(moveto loc-3-3)
    (keyforroom key-1 room-1)
	(keyat key-1 loc-2-3)
	(pick key-1)
    )

    (:goal (and (at loc-3-3)))
)
    
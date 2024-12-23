(define (domain doors)
  (:requirements :strips :typing)
  (:types location room key wall fire person)
  (:predicates
     (at ?loc - location)
     (unlocked ?room - room)
     (locinroom ?loc - location ?room - room)
     (keyat ?key - key ?loc - location)
     (personat ?person - person ?loc - location)
     (wallat ?wall - wall ?loc - location)
     (fireat ?fi - fire ?loc - location)
     (keyforroom ?key - key ?room - room)
     (moveto ?loc - location)
     (free ?loc - location)
     (pick ?key - key)
  )

  ; (:actions moveto pick)

  (:action moveto
    :parameters (?sloc - location ?eloc - location ?eroom - room)
    :precondition (and (moveto ?eloc)
                       (free ?eloc)
                       (at ?sloc)
                       (unlocked ?eroom)
                       (locinroom ?eloc ?eroom)
                  )
    :effect (and (not (at ?sloc))
                 (at ?eloc)
                 (not (free ?eloc))
			           (free ?sloc)
            )
  )

  (:action pick
    :parameters (?loc - location ?key - key ?room - room)
    :precondition (and (pick ?key)
                       (at ?loc)
                       (keyat ?key ?loc)
                       (keyforroom ?key ?room)
                  )
    :effect (and (not (keyat ?key ?loc))
                 (unlocked ?room)
            )
  )

)
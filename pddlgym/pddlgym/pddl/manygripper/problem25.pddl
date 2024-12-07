
(define (problem manygripper) (:domain gripper-strips)
  (:objects
        ball0
	ball1
	ball10
	ball11
	ball12
	ball13
	ball14
	ball15
	ball16
	ball17
	ball18
	ball19
	ball2
	ball20
	ball21
	ball22
	ball23
	ball24
	ball3
	ball4
	ball5
	ball6
	ball7
	ball8
	ball9
	gripper0
	gripper1
	room0
	room1
	room10
	room11
	room12
	room13
	room14
	room15
	room16
	room17
	room18
	room19
	room2
	room3
	room4
	room5
	room6
	room7
	room8
	room9
  )
  (:init 
	(at ball0 room16)
	(at ball10 room4)
	(at ball11 room18)
	(at ball12 room18)
	(at ball13 room10)
	(at ball14 room11)
	(at ball15 room14)
	(at ball16 room19)
	(at ball17 room16)
	(at ball18 room1)
	(at ball19 room8)
	(at ball1 room17)
	(at ball20 room7)
	(at ball21 room5)
	(at ball22 room15)
	(at ball23 room9)
	(at ball24 room0)
	(at ball2 room4)
	(at ball3 room14)
	(at ball4 room13)
	(at ball5 room17)
	(at ball6 room6)
	(at ball7 room10)
	(at ball8 room5)
	(at ball9 room4)
	(at-robby room0)
	(ball ball0)
	(ball ball10)
	(ball ball11)
	(ball ball12)
	(ball ball13)
	(ball ball14)
	(ball ball15)
	(ball ball16)
	(ball ball17)
	(ball ball18)
	(ball ball19)
	(ball ball1)
	(ball ball20)
	(ball ball21)
	(ball ball22)
	(ball ball23)
	(ball ball24)
	(ball ball2)
	(ball ball3)
	(ball ball4)
	(ball ball5)
	(ball ball6)
	(ball ball7)
	(ball ball8)
	(ball ball9)
	(free gripper0)
	(free gripper1)
	(gripper gripper0)
	(gripper gripper1)
	(room room0)
	(room room10)
	(room room11)
	(room room12)
	(room room13)
	(room room14)
	(room room15)
	(room room16)
	(room room17)
	(room room18)
	(room room19)
	(room room1)
	(room room2)
	(room room3)
	(room room4)
	(room room5)
	(room room6)
	(room room7)
	(room room8)
	(room room9)
  )
  (:goal (and
	(at ball23 room1)
	(at ball12 room18)
	(at ball7 room14)
	(at ball10 room12)
	(at ball6 room8)))
)

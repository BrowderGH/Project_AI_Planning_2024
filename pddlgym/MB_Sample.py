import random
import numpy as np

#################################################################################
#################################################################################
# For the 2 fireball case
#       We will choose 2 fireball locations randomly out of 48.  This is 4% fireballs

#initialize
Fire_Set = np.zeros((200, 2))
Fire_Set

Fire_Set = np.zeros((200, 2))
Fire_Set

for i in range(0,200):
    random.seed(i)
    Fire_Set[i] = random.sample(range(1,48), 2)

# Note:  We pass over the Test_Set indices that are failures

print(Fire_Set[9])

# 1: 2-5, 0-7
# 2: 0-3, 5-5
# 3: 2-0, 2-1
# 4: 0-5, 7-3
# 5: 0-5, 6-0
# 6: 6-5, 3-3
# 7: 5-5, 2-1
# 8: 0-6, 2-2
# 9: 5-0, 5-2
#10: 3-5, 6-5


#################################################################################
#################################################################################
# For the 4 fireball case
#       We will choose 4 fireball locations randomly out of 48.  This is 8% fireballs

#initialize
Fire_Set_B = np.zeros((200, 4))
Fire_Set_B

for i in range(0,200):
    random.seed(i)
    Fire_Set_B[i] = random.sample(range(1,48), 4)

Fire_Set_B[0]
Fire_Set_B[1]
Fire_Set_B[2]
Fire_Set_B[3]
Fire_Set_B[4]
Fire_Set_B[5]
Fire_Set_B[6]
# Note:  Fireset[11] is replaced for Fireset[7], due to failure
Fire_Set_B[11]
Fire_Set_B[8]
Fire_Set_B[9]
Fire_Set_B[10]

#################################################################################
#################################################################################
# For the 8 fireball case
#       We will choose 8 fireball locations randomly out of 48.  This is about 16% fireballs

#initialize
Test_Set = np.zeros((200, 8))
Test_Set

Fire_Set_C = np.zeros((200, 8))
Fire_Set_C

for i in range(0,200):
    random.seed(i)
    Test_Set[i] = random.sample(range(1,48), 8)

# Note:  We pass over the Test_Set indices that are failures

Fire_Set_C[0]=Test_Set[3]   
Fire_Set_C[1]=Test_Set[8]
Fire_Set_C[2]=Test_Set[9]
Fire_Set_C[3]=Test_Set[10]
Fire_Set_C[4]=Test_Set[11]
Fire_Set_C[5]=Test_Set[16]
Fire_Set_C[6]=Test_Set[18]
Fire_Set_C[7]=Test_Set[19]
Fire_Set_C[8]=Test_Set[21]
Fire_Set_C[9]=Test_Set[22]



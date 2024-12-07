

#Things to update for each group:
    # Group Name
    # Title of Graph
    # Search in Lookahead
    # Change folders
    # adjust outer loop
    # environment index
    #loop - 11/12


import pandas as pd
import numpy as np
import pddlgym
from pddlgym_planners.fd import FD
import imageio
import time
import pint
import matplotlib.pyplot as plt
import os
import io
import sys
import logging


Group_Name = "a_Output_16PercentF_Astar_Hff_Uniform"

# for log:
#sys.stdout = io.open(f"{Group_Name}/a_Output_Charts/log", 'w')

Appended_Df = []
Appended_Df_nums = []
end = 11

for i in range(5,6):

    global appended_removals, check
    appended_removals = []
    
    check = 0
    Tot_Actions_in_Plans = 0

    Accumulated_Search_Time = 0
    Accumulated_Total_Plan_Time = 0
    Accumulated_Total_Nodes_Evaluated = 0 
    Accumulated_Total_Nodes_Expanded = 0

    start_time = time.time()

    # We will use the doors environment:

    env_Real_World = pddlgym.make("PDDLEnvDoors-v0")

    #Notes: 
    #       The index number below refers to the pddl problem file
    #       Each of these different lines corresponds to the level of fireballs:
    #       These are scripts for the "real world"

    # 8 percent fireballs (4 fireballs):
    #env_Real_World.fix_problem_index(18+(2*i))  
    
    #16 percent fireballs (8 fireballs):
    env_Real_World.fix_problem_index(40+(2*i))

    # 4 percent fireballs (2 fireballs):
    #env_Real_World.fix_problem_index(60+(2*i))

    # basline (no fireballs):
    #env_Real_World.fix_problem_index(82)

    obs_RW, debug_info_RW = env_Real_World.reset()

    img = env_Real_World.render()
    imageio.imsave(f"{Group_Name}/Image1.png", img)


# Lookahead
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

    def Lookahead(Journey, env_Perceived_World, obs_PW, loop_check):

        global Tot_Actions_in_Plans, Accumulated_Search_Time, Accumulated_Total_Plan_Time, Accumulated_Total_Nodes_Evaluated, Accumulated_Total_Nodes_Expanded

        if Journey == "Start": 
            #Notes: 
            #       The index number below refers to the pddl problem file
            #       Each of these different lines corresponds to the level of fireballs:
            #       These are scripts for the "perceived world"
            #S_Index = 19+(2*i)
            S_Index = 41+(2*i)
            #S_Index = 61+(2*i)
            #S_Index = 83
            env_Perceived_World = pddlgym.make("PDDLEnvDoors-v0")
            env_Perceived_World.fix_problem_index(S_Index)
            obs_PW, debug_info_PW = env_Perceived_World.reset()

        """
        If the agent encountered an obstacle in his/her path, the agent must used the 
        the updated perceived world environment from the simulate method
        """

        planner = FD(alias_flag="--alias seq-opt-hff")

        # We use the perceived world to make the plan, not the real world
        plan_PW = planner(env_Perceived_World.domain, obs_PW)

        from pddlgym_planners.pddl_planner import Search_Time_Float, Total_Time_Float, Total_Nodes_Expanded, Total_Nodes_Evaluated

        Accumulated_Search_Time = Accumulated_Search_Time + Search_Time_Float
        Accumulated_Total_Plan_Time = Accumulated_Total_Plan_Time + Total_Time_Float
        Accumulated_Total_Nodes_Evaluated =  Accumulated_Total_Nodes_Evaluated + Total_Nodes_Evaluated
        Accumulated_Total_Nodes_Expanded =  Accumulated_Total_Nodes_Expanded + Total_Nodes_Expanded 

        # We will change the plan vector to a panda series:
        Temp = pd.Series(plan_PW)

        # We will change the plan vector to a vector of strings
        Planned_Actions = Temp.astype(str)

        print(" ")
        print(" ")
        print("******************************")
        print(" ")
        print(f"We just ran lookahead.  Thus, we have created plan {loop_check}.")
        print(" ")
        print("******************************")
        print(" ")
        print("Here are the number of planned actions:", len(Planned_Actions))
        print(" ")
    
        Tot_Actions_in_Plans = Tot_Actions_in_Plans + len(Planned_Actions)

        # Now we will collect the locations of where we move to in the plan

        # "np.where" is a conditional statement for the vector
        Temp2 = np.where(Planned_Actions.str[0]== "m", Planned_Actions.str[7:16], "NA") 
        Temp3 = pd.Series(Temp2)

        # Here we remove the colon:
        def Function1(row):
            if ":" in row:
                row = row[0:row.find(":")]
            return row

        # Apply the function to each row
        Temp4 = Temp3.apply(Function1)

        Planned_Destinations = Temp4

        print("The planned actions are:\n", Planned_Actions)
        print(" ")
        print(" ")
        print("The list of planned destinations are:\n", Planned_Destinations)
        print(" ")
        print(" ")
        print("We will now begin a series of actions:")
        print(" ")
        return obs_PW, plan_PW, env_Perceived_World, Planned_Actions, Planned_Destinations
        
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################

    # Simulate
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################


    def Simulate_(obs_RW, obs_PW, Planned_Destinations, Planned_Actions, index, loop_check):
  
        global check, appended_removals

        if check == 0:
            appended_removals = []
    
        check = 1

        # Let's grab our current state in the real world:
        Current_State = str(obs_RW)

        """
        To infer that our next planned destination is free, 
        we must first find this needed condition in the real world (not perceived world):
        """

        Needed_Condition = f"free({Planned_Destinations[index]}:location)"
        
        """
        Let's check whether or not our next planned destination is "free".  This means it is 
        void of fire, wall, etc. To do this, we will need to check whether the current state 
        has our needed condition:  "free(loc-##-##:location)"
        """
        Result_of_Search = Current_State.find(Needed_Condition)

        if Planned_Actions[index][0:6] == "moveto":
        # Let's print our next planned destination from the planner:
            print("The next planned destination is:", Planned_Destinations[index])
            print("In the current state, we are looking for the following atom:", Needed_Condition)

    
        if Result_of_Search == -1 and Planned_Destinations[index] != "NA":
            print("After reviewing our environment, we observe that the planned destination is not reachable.  Thus, we must make a new plan.")
        
            """
            We must now update our perceived world by removing the atom "(free loc-#-#)" for 
            whatever spot we now see is unavailable
            """
            # First we need to grab the atoms of the current state. This corresponds to "literals" or obs[0]
            W1 = list(obs_PW[0])
            # Convert to a list of strings
            W2 = [str(x) for x in W1]
            # Save to appended list of adjustments:
            appended_removals.append(Needed_Condition)
            # Remove the element

            for element in appended_removals:
                #print("The element is", element)
                # Find the element we want to remove
                #print("Appended_removals:", appended_removals)
                Index_Atom = W2.index(element)
                #print("This is the element we are deleting:", W1[Index_Atom])
                #print("length of W1", len(W1))
                #print("length of W2", len(W2))
                del W1[Index_Atom]
                del W2[Index_Atom]

            # Convert back to frozenset
            New_Literals = frozenset(W1)
            obs_PW = pddlgym.structs.State.with_literals(obs_PW, New_Literals)

            return obs_PW, "Failure"

        else:
            if Planned_Destinations[index] != "NA":
                print("After reviewing our environment, we observe that the planned destination is in fact reachable.  Thus, we can proceed.")
            return obs_PW, "Success"

    ###########################################################################################
    ###########################################################################################
    ###########################################################################################



    # Failure Check
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################

    def Failure_Check(obs_RW, Planned_Destinations, Planned_Actions, index):
   
        # Let's grab our present state in the real world:
        Present_State = str(obs_RW)

        # Let's check two needed conditions for a failure:
        Needed_Condition1 = f"at({Planned_Destinations[index-1]}:location)"
        
        Find_Needed_Condition1 = Present_State.find(Needed_Condition1) 

        Needed_Condition2a = Planned_Actions[index-1][0:6]
        Needed_Condition2 = Needed_Condition2a.strip()

        if Find_Needed_Condition1 == -1 and Needed_Condition2 == "moveto":
            print("For the failure test, the correct current location of the agent should be:", Needed_Condition1)
            print(f"The Needed_Condition1 for failure test is: {Find_Needed_Condition1}, where -1 means not found.")
            print("The Needed_Condition2 for failure test is for the prior action =", Planned_Actions[index-1][0:6])
            return True
        else:
            return False

    ###########################################################################################
    ###########################################################################################
    ###########################################################################################


    # Run_Lazy_Lookahead
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################

    def Run_Lazy_Lookahead (env_Real_World, env_Perceived_World, obs_RW, obs_PW):

        global start_time, end_time, Tot_Actions_in_Plans

        Journey = "Start"
        Simulate_Check = "Empty"

        Action_Count = 1
        loop_check = 1

        while True:

            """
            If we are just starting the journey, we run Lookahead.  In this case, env_Real_World and obs_RW
            are not used in the Lookahead.  Rather we will use env_Perceived_World and obs_PW.
            """
            if Journey == "Start" or Simulate_Check == "Failure":
                obs_PW, plan_PW, env_Perceived_World, Planned_Actions, Planned_Destinations = Lookahead(Journey, env_Perceived_World, obs_PW, loop_check)
                Journey = "Start" 
        
            loop_check += 1
            count = 1
            index = 0
            Simulate_Check = "Proceed"

        
            for act in plan_PW:
        
                # Failure check.  We do this check only after the first attempted action (Journey != "Start").
                if Journey != "Start":
                    if Failure_Check(obs_RW, Planned_Destinations, Planned_Actions, index):
                        print(" ")
                        print("*** The process here terminates because the Plan Failed!! ***")
                        print(" ")
                        Flag = "Early_Break"
                        break
                
                Journey = "In_Motion"
            
                obs_PW, Simulate = Simulate_(obs_RW, obs_PW, Planned_Destinations, Planned_Actions, index, loop_check)

                # Here is the classic Run_Lazy_Lookahead check statement:

                if Simulate == "Failure":
                    Simulate_Check = "Failure"
                    print(" ")
                    print("Simulate = Failure")
                    print(" ")
                    Flag = "Early_Break"
                    break

                print(" ")
                print(" ")
                print("The agent now performs this act:", act)
                print(" ")
                print("Action Count:", Action_Count)
                print(" ")
                obs_RW, reward, done, truncated, debug_info = env_Real_World.step(act)
                obs_PW, reward, done, truncated, debug_info = env_Perceived_World.step(act)
            
                img = env_Real_World.render()
                count += 1
                index += 1
                Action_Count += 1
                imageio.imsave(f"{Group_Name}/Image{Action_Count}.png", img)
                Flag = "Successful_Completion"
                #print("Obs:", obs_RW)
            if Flag == "Successful_Completion":
                total_plans = loop_check - 1
                total_actions = Action_Count - 1
                end_time = time.time()
                a1 = end_time - start_time
                elapsed_time = round(a1, 5)
                A_PT = round(Accumulated_Total_Plan_Time, 5)
                A_ST = round(Accumulated_Search_Time, 5)
                A_PT_Str = str(A_PT) + "s"
                A_ST_Str = str(A_ST) + "s"
                E_Str = str(elapsed_time) + "s"

                TA = str(total_actions)
                TA2 = str(Tot_Actions_in_Plans)
                print(TA2)
                Actions_Tot = TA + "   " + TA2 + "  "
                print("The agent has reached the goal!")
                print("Our total number of plans created for this journey was:", total_plans)
                print("Our total number of actions for this journey was:", Actions_Tot)
                print("The total nodes evaluated in the journey:", Accumulated_Total_Nodes_Evaluated)
                print("The total nodes expanded in the journey:", Accumulated_Total_Nodes_Expanded)
                print(f"Our total time spent running search algorithms was: {Accumulated_Search_Time} seconds.")
                print(f"Our total time spent planning in this journey was: {Accumulated_Total_Plan_Time} seconds.")
                print(f"The total time for this journey was:  {elapsed_time} seconds.")
                trial = i
                """
                if i <= 8:
                    trial = i
                if i > 8:
                    trial = i - 1
                """
                row = pd.Series([trial, total_plans, Actions_Tot, E_Str, A_PT_Str, A_ST_Str, Accumulated_Total_Nodes_Evaluated, Accumulated_Total_Nodes_Expanded])
                # Make everything a num type so we can calculate mean, etc.
                row_nums = pd.Series([trial, total_plans, total_actions, Tot_Actions_in_Plans, elapsed_time, A_PT, A_ST, Accumulated_Total_Nodes_Evaluated, Accumulated_Total_Nodes_Expanded])
            
                Appended_Df.append(row)
                Appended_Df_nums.append(row_nums)
                """
                if i != 8:
                    Appended_Df.append(row)
                    Appended_Df_nums.append(row_nums)
                """
               
                return False    
        
        
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################



    # Call Statements
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################

    env_Perceived_World = "null"
    obs_PW = "null"
    Run_Lazy_Lookahead(env_Real_World, env_Perceived_World, obs_RW, obs_PW)

   

###############################################################################
###############################################################################

DF_nums = pd.DataFrame(Appended_Df_nums)
DF_nums.columns = ["Trial", "Plans", "Actions", "Actions in Plans", "Tot Time", "Pl Time", "S Time","N Eval.", "N Exp."]
#print(DF_nums)

quartiles = pd.DataFrame(DF_nums.quantile([0.25, 0.5, 0.75]))
Min = pd.DataFrame(DF_nums.min())
Max = pd.DataFrame(DF_nums.max())
Mean = pd.DataFrame(DF_nums.mean())
Std = pd.DataFrame(DF_nums.std())
Min_T = Min.T
Max_T = Max.T
Mean_T = Mean.T
Std_T = Std.T

Stats_DF = pd.concat([quartiles, Min_T, Max_T, Mean_T, Std_T], axis=0)
print(" ")
print("Stats:")
print(Stats_DF)
print(" ")

#DF_nums.boxplot()
#plt.show()

#Now, let's save it to the desired folder:
eval("DF_nums").to_csv(f"a_Output__Charts/{Group_Name}_Main.csv", header=True)
"""
eval("Stats_DF").to_csv(f"{Group_Name}/a_Output_Charts/{Group_Name}.csv", header=True)
eval("Stats_DF").to_csv(f"a_Output__Charts/{Group_Name}.csv", header=True)
"""
###############################################################################
###############################################################################

DF = pd.DataFrame(Appended_Df)
DF.columns = ["Trial", "Plans", "Actions", "Tot Time", "Pl Time", "S Time","N Eval.", "N Exp."]


###############################################################################
###############################################################################
print(" ")
print("Output for all trials:")
print(" ")
print(DF)
#globals()["File1"]=DF


fig, ax = plt.subplots()
# this hides the axes:
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
#ax.text( .5, .95, "A* HFF for 4% Fireballs and Uniform Distribution", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)
ax.text( .5, .95, "A* Hff for 16% Fireballs and Uniform Distribution", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)


table = ax.table(cellText=DF.values, colLabels=DF.columns, bbox = [-.118, 0, 1.2, .8])
table.set_fontsize(9)
table.auto_set_font_size(False)
table.scale(1.23, 1.23)


plt.savefig(f"{Group_Name}/a_Output_Charts/{Group_Name}.png")
plt.savefig(f"a_Output__Charts/{Group_Name}.png")
plt.show()





#My options for aliases:


"""
    # Astar with Landmark Cut Heuristic
    ALIASES["seq-opt-lmcut"] = [
        "--search", "astar(lmcut())"]

    # Astar with Fast Forward Heuristic
    ALIASES["seq-opt-hff"] = [
        "--search", "astar(ff())"]

    # Eager Greedy with Lanmdark Cut Heuristic
    ALIASES["seq_eager-opt-lmcut"] = [
        "--search", "eager_greedy([lmcut()])"]

    # Eager Greedy with Fast Forward Heuristic
    ALIASES["seq_eager-opt-hff"] = [
        "--search", "eager_greedy([ff()])"]

    # Lazy Greedy with Landmark Cut Heuristic
    ALIASES["seq_lazy-opt-lmcut"] = [
        "--search", "lazy_greedy([lmcut()])"]
"""
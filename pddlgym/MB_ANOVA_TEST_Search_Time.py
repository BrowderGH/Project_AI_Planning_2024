#replac key variable
#graph title
#rename key variable
# comments
# update plt.close

import statsmodels.api as sm 
from statsmodels.formula.api import ols 
import pandas as pd
import numpy as np

import pddlgym
from pddlgym_planners.fd import FD
import imageio
import matplotlib.pyplot as plt
import os
import io
import sys


# Core Variables
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

# Our core variables are :
#       Total Plans
#       Total Planning Time
#       Total Search Time
#       Nodes Evaluated
#       Nodes Expanded
#       Total Time of Journey
#       Total Actions in Journey
#       Sum of Actions in Plans      

# Read Data
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
 
# A* Hff
A1 = pd.read_csv("a_Output__Charts/a_Output_baseline_Astar_HFF_Uniform_Main_saved.csv")
A2 = pd.read_csv("a_Output__Charts/a_Output_4PercentF_Astar_Hff_Uniform_Main_saved.csv")
A3 = pd.read_csv("a_Output__Charts/a_Output_8PercentF_Astar_Hff_Uniform_Main_saved.csv")
A4 = pd.read_csv("a_Output__Charts/a_Output_16PercentF_Astar_Hff_Uniform_Main_saved.csv")

# GBFS Hff
B1 = pd.read_csv("a_Output__Charts/a_Output_baseline_Greedy_HFF_Uniform_Main_saved.csv")
B2 = pd.read_csv("a_Output__Charts/a_Output_4PercentF_Greedy_Hff_Uniform_Main_saved.csv")
B3 = pd.read_csv("a_Output__Charts/a_Output_8PercentF_Greedy_Hff_Uniform_Main_saved.csv")
B4 = pd.read_csv("a_Output__Charts/a_Output_16PercentF_Greedy_Hff_Uniform_Main_saved.csv")

# A* LMCUT
C1 = pd.read_csv("a_Output__Charts/a_Output_baseline_Astar_LMCUT_Uniform_Main_saved.csv")
C2 = pd.read_csv("a_Output__Charts/a_Output_4PercentF_Astar_LMCUT_Uniform_Main_saved.csv")
C3 = pd.read_csv("a_Output__Charts/a_Output_8PercentF_Astar_LMCUT_Uniform_Main_saved.csv")
C4 = pd.read_csv("a_Output__Charts/a_Output_16PercentF_Astar_LMCUT_Uniform_Main_saved.csv")

A1["Search"] = "A*"
A1["Heuristic"] = "Hff"
A1["Fireballs"] = "Baseline"
A2["Search"] = "A*"
A2["Heuristic"] = "Hff"
A2["Fireballs"] = "4 Percent"
A3["Search"] = "A*"
A3["Heuristic"] = "Hff"
A3["Fireballs"] = "8 Percent"
A4["Search"] = "A*"
A4["Heuristic"] = "Hff"
A4["Fireballs"] = "16 Percent"

B1["Search"] = "Greedy"
B1["Heuristic"] = "Hff"
B1["Fireballs"] = "Baseline"
B2["Search"] = "Greedy"
B2["Heuristic"] = "Hff"
B2["Fireballs"] = "4 Percent"
B3["Search"] = "Greedy"
B3["Heuristic"] = "Hff"
B3["Fireballs"] = "8 Percent"
B4["Search"] = "Greedy"
B4["Heuristic"] = "Hff"
B4["Fireballs"] = "16 Percent"

C1["Search"] = "A*"
C1["Heuristic"] = "LMCUT"
C1["Fireballs"] = "Baseline"
C2["Search"] = "A*"
C2["Heuristic"] = "LMCUT"
C2["Fireballs"] = "4 Percent"
C3["Search"] = "A*"
C3["Heuristic"] = "LMCUT"
C3["Fireballs"] = "8 Percent"
C4["Search"] = "A*"
C4["Heuristic"] = "LMCUT"
C4["Fireballs"] = "16 Percent"


# Search Time
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

#  Do two way ANOVA for Planning_Time, Fireballs, and Search Method
#########################################################################################
#########################################################################################

F1 = A1[["S Time", "Fireballs", "Search"]]
F2 = A2[["S Time", "Fireballs", "Search"]]
F3 = A3[["S Time", "Fireballs", "Search"]]
F4 = A4[["S Time", "Fireballs", "Search"]]
F5 = B1[["S Time", "Fireballs", "Search"]]
F6 = B2[["S Time", "Fireballs", "Search"]]
F7 = B3[["S Time", "Fireballs", "Search"]]
F8 = B4[["S Time", "Fireballs", "Search"]]
F9 = C1[["S Time", "Fireballs", "Search"]]
F10 = C2[["S Time", "Fireballs", "Search"]]
F11 = C3[["S Time", "Fireballs", "Search"]]
F12 = C4[["S Time", "Fireballs", "Search"]]

Search_T = pd.DataFrame(pd.concat([F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12], axis = 0))


Search_T.rename(columns={"S Time":"Planning_Time"}, inplace=True)
Search_T.info()


print(Search_T.tail)


model = ols("Search_Time ~ C(Fireballs) + C(Search) + C(Fireballs):C(Search)", 
            data=Search_T).fit() 
output_A = sm.stats.anova_lm(model, type=2) 
#print(Search_T.loc[0:20, :])

#pd.set_option('display.float_format', lambda x: '%.10f' % x)
#output_A.style.format({'sum_sq': '{:.10f}'})
output_A = output_A.drop(columns=["df", 'sum_sq', 'mean_sq'])
output_A = output_A.drop(output_A.index[3])
print(output_A)
########################### Save results to CSV file

eval("output_A").to_csv(f"a__Output_ANOVA/Search_Time_1_ANOVA.csv", header=True)

########################### Plot results
fig, ax = plt.subplots()
# this hides the axes:
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

ax.text( .5, .95, "ANOVA for Search Time by Fireballs", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)
ax.text( .5, .86, "and Search Method", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)

table = ax.table(cellText= output_A.values, rowLabels=output_A.index, colLabels=output_A.columns, bbox = [.15, 0, .95, .8])
table.set_fontsize(8)
table.auto_set_font_size(False)
table.scale(1.23, 1.23)


plt.savefig(f"a__Output_ANOVA/Search_Time_1_Picture_A.png")
plt.close()

#  Do two way ANOVA for Search_Time, Fireballs, and Heuristic
########################################################################################
########################################################################################


F1 = A1[["S Time", "Fireballs", "Heuristic"]]
F2 = A2[["S Time", "Fireballs", "Heuristic"]]
F3 = A3[["S Time", "Fireballs", "Heuristic"]]
F4 = A4[["S Time", "Fireballs", "Heuristic"]]
F5 = B1[["S Time", "Fireballs", "Heuristic"]]
F6 = B2[["S Time", "Fireballs", "Heuristic"]]
F7 = B3[["S Time", "Fireballs", "Heuristic"]]
F8 = B4[["S Time", "Fireballs", "Heuristic"]]
F9 = C1[["S Time", "Fireballs", "Heuristic"]]
F10 = C2[["S Time", "Fireballs", "Heuristic"]]
F11 = C3[["S Time", "Fireballs", "Heuristic"]]
F12 = C4[["S Time", "Fireballs", "Heuristic"]]

Search_T = pd.DataFrame(pd.concat([F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12], axis = 0))


Search_T.rename(columns={"S Time":"Search_Time"}, inplace=True)
Search_T.info()


print(Search_T.tail)


model = ols("Search_Time ~ C(Fireballs) + C(Heuristic) + C(Fireballs):C(Heuristic)", 
            data=Search_T).fit() 
output_A = sm.stats.anova_lm(model, type=2) 
#print(Search_T.loc[0:20, :])

#pd.set_option('display.float_format', lambda x: '%.10f' % x)
#output_A.style.format({'sum_sq': '{:.10f}'})
output_A = output_A.drop(columns=["df", 'sum_sq', 'mean_sq'])
output_A = output_A.drop(output_A.index[3])
print(output_A)
########################### Save results to CSV file

eval("output_A").to_csv(f"a__Output_ANOVA/Search_Time_2_ANOVA.csv", header=True)

########################### Plot results
fig, ax = plt.subplots()
# this hides the axes:
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

ax.text( .5, .95, "ANOVA for Search Time by Fireballs", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)
ax.text( .5, .86, "and Heuristic", transform=ax.transAxes, weight = "bold", ha='center', fontsize=14)

table = ax.table(cellText= output_A.values, rowLabels=output_A.index, colLabels=output_A.columns, bbox = [.2, 0, .90, .8])
table.set_fontsize(8)
table.auto_set_font_size(False)
table.scale(1.23, 1.23)

plt.savefig(f"a__Output_ANOVA/Search_Time_2_Picture_A.png")
plt.close()


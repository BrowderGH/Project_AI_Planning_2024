import pandas as pd
import numpy as np
import pddlgym
from pddlgym_planners.fd import FD
import imageio
import time
import matplotlib.pyplot as plt
import os
import io
import sys
import logging

# Results for Greedy HFF
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################


# Read in Files
################################################################################
################################################################################

Group_Name = "a_Output_Astar_LMCUT_Uniform"

A1 = pd.read_csv("a_Output__Charts/a_Output_baseline_Astar_LMCUT_Uniform_Main_saved.csv")
A2 = pd.read_csv("a_Output__Charts/a_Output_4PercentF_Astar_LMCUT_Uniform_Main_saved.csv")
A3 = pd.read_csv("a_Output__Charts/a_Output_8PercentF_Astar_LMCUT_Uniform_Main_saved.csv")
A4 = pd.read_csv("a_Output__Charts/a_Output_16PercentF_Astar_LMCUT_Uniform_Main_saved.csv")

print(A4)

# Total Plans
################################################################################
################################################################################

plt.title("A* LMCUT Number of Plans in Journey")
DF = pd.concat([A1["Plans"], A2["Plans"], A3["Plans"], A4["Plans"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Plans_Box_Plot.png")
plt.close()

# Total Actions
################################################################################
################################################################################

plt.title("A* LMCUT Total Actions in Journey")
DF = pd.concat([A1["Actions"], A2["Actions"], A3["Actions"], A4["Actions"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Actions_Box_Plot.png")
plt.close()

# Total Actions in Plans
################################################################################
################################################################################

plt.title("A* LMCUT Total Actions in Plans")
DF = pd.concat([A1["Actions in Plans"], A2["Actions in Plans"], A3["Actions in Plans"], A4["Actions in Plans"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Actions_in_Plans_Box_Plot.png")
plt.close()

# Total Time
################################################################################
################################################################################

plt.title("A* LMCUT Total Time for Journey")
DF = pd.concat([A1["Tot Time"], A2["Tot Time"], A3["Tot Time"], A4["Tot Time"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Tot_Time_Box_Plot.png")
plt.close()

# Total Planning Time
################################################################################
################################################################################

plt.title("A* LMCUT Total Planning Time")
DF = pd.concat([A1["Pl Time"], A2["Pl Time"], A3["Pl Time"], A4["Pl Time"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Pl_Time_Box_Plot.png")
plt.close()

# Total Search Time
################################################################################
################################################################################

plt.title("A* LMCUT Total Search Time")
DF = pd.concat([A1["S Time"], A2["S Time"], A3["S Time"], A4["S Time"]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_Search_Time_Box_Plot.png")
plt.close()

# Total Nodes Evaluated
################################################################################
################################################################################

plt.title("A* LMCUT Total Nodes Evaluated")
DF = pd.concat([A1["N Eval."], A2["N Eval."], A3["N Eval."], A4["N Eval."]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_N_Evaluated_Box_Plot.png")
plt.close()

# Total Nodes Expanded
################################################################################
################################################################################

plt.title("A* LMCUT Total Nodes Expanded")
DF = pd.concat([A1["N Exp."], A2["N Exp."], A3["N Exp."], A4["N Exp."]], axis = 1)
DF.columns = ["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"]
print(DF)
boxplot = DF.boxplot(column=["Baseline", "4% Fireballs", "8% Fireballs", "16% Fireballs"], showfliers=False) 
plt.savefig(f"a_Output__BoxPlots/{Group_Name}_N_Expanded_Box_Plot.png")
plt.show()
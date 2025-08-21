import numpy as np
from scipy.optimize import least_squares

#Input Variables
M = 0.03          #Molar Mass of Exhaust Gasses   (Kg/kmol)

m_p = 30        #Available Propellent Mass      (Kg)

dt = 30         #Burn Time                      (S)

T_c = 3000      #Chamber Temperature            (C)

gamma = 1.31    #Ratio of Specific Heats

A_e = 0.004418  #Exit Area                      (m^2)

P_a = 15        #Ambient Pressure               (Pa)



#Preliminary Calculations
R_s = 8.31446261815324 / M                  #Specific Gas Constant

mdot = m_p / dt                             #Mass Flow Rate

T_s = T_c                                   #Stagnation Temperature

P_e = P_a                                   #Exit Pressure

T_t = T_s * (1 + ((gamma - 1) / 2)) ** -1   #Throat Temperature



#Initial Recursive Variables Guesses
epsilon = 5            #Area Ratio Initial Guess
P_c = 700              #Chamber Pressure Initial Guess     (Pa)
A_t = 0.0008836        #Exit Area Initial Guess            (m^2)
rCalcsVars = [epsilon, P_c, A_t]

#least_squares bounds
#Variable     low <= x <= high
epsilonBounds   = [1, 15]
P_cBounds       = [P_e, 1000]
A_tBounds       = [A_e / 15, A_e]
rCalcsVarsBounds = ([epsilonBounds[0], P_cBounds[0], A_tBounds[0]], [epsilonBounds[1], P_cBounds[1], A_tBounds[1]])



def calcs():
    #Throat Temperature
    T_t = T_s * (1 + ((gamma - 1) / 2)) ** -1

    #Throat Sonic Velocity
    c_t = np.sqrt(gamma * R_s * T_t)

    #Mach Exit Number
    Ma_e = np.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ** ((gamma - 1) / gamma) - 1))



def rCalcs(rCalcsVars, T_t, gamma):
    epsilon, P_c, A_t = rCalcsVars

    #Throat Area
    A_t = A_e / epsilon

    #Chamber Pressure
    P_c = ((mdot * np.sqrt(T_t)) / A_t) * np.sqrt(R_s / gamma) * ((gamma + 1) / 2) ** ((gamma + 1) * (2 * (gamma - 1)))

    #Area Ratio
    epsilon = ((gamma + 1) / 2) ** (1 / (gamma - 1)) * (P_e / P_c) ** (1 / gamma) * np.sqrt(((gamma + 1) / (gamma - 1)) * (1 - (P_e / P_c) ** ((gamma - 1) / gamma)))

    return [epsilon, P_c, A_t]

def rCalcsOptimization():
    #Using Scipy's least_squares method to solve recursive calculations
    results = least_squares(rCalcs, rCalcsVars, args=(T_t, gamma), bounds=rCalcsVarsBounds)
    epsilon, P_c, A_t = results.x

calcs()
import numpy as np

#Input Variables
M = 30          #Molar Mass of Exhaust Gasses   (Kg/kmol)

m_p = 30        #Available Propellent Mass      (Kg)

dt = 30         #Burn Time                      (S)

T_c = 3000      #Chamber Temperature            (C)

gamma = 1.31    #Ratio of Specific Heats

A_e = 0.004418  #Exit Area                      (m^2)

P_a = 15        #Ambient Pressure               (Pa)

#Preliminary Calculations
R_s = 8.31446261815324 / M  #Specific Gas Constant

mdot = m_p / dt             #Mass Flow Rate

T_s = T_c                   #Stagnation Temperature

P_e = P_a                   #Exit Pressure

def calculations():
    #Specific Gas Constant
    R_s = 8.31446261815324 / M

    #Mass Flow Rate
    mdot = m_p / dt

    #Throat Temperature
    T_t = T_s * (1 + ((gamma - 1) / 2)) ** -1

    #Throat Sonic Velocity
    c_t = np.sqrt(gamma * R_s * T_t)



def recursiveCalculations():
    #Throat Area
    A_t = A_e / epsilon

    #Chamber Pressure
    P_c = ((mdot * np.sqrt(T_t)) / A_t) * np.sqrt(R_s / gamma) * ((gamma + 1) / 2) ** ((gamma + 1) * (2 * (gamma - 1)))

    #Mach Exit Number
    Ma_e = np.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ** ((gamma - 1) / gamma) - 1))

    #Area Ratio
    epsilon = ((gamma + 1) / 2) ** (1 / (gamma - 1)) * (P_e / P_c) ** (1 / gamma) * np.sqrt(((gamma + 1) / (gamma - 1)) * (1 - (P_e / P_c) ** ((gamma - 1) / gamma)))

#Initial Recursive Variables Guesses
epsilonGuess = 5
from scipy.optimize import fsolve
import math
import numpy

#Input Variables
A_e = 0.1   #Exit Area                          (m^2)
T_c = 3000  #Chamber Temperature                (k)
P_e = 15   #Exit Pressure                      (Pa)
gamma = 1.3 #Exit Gas Ratio of Specific Heats
m_p = 20    #Propellent Mass                    (kg)
dt = 30     #Burn Time                          (S)
M = 30      #Exit Gas Molar Mass                (kg/kmol)

#Initial Guesses
Ma_e = 3
P_c = 500
epsilon = 5
A_t = 0.02

def calculations1():
    #Specific Gas Consant
    R_s = 8.134462618 / M

    #Mass Flow Rate (2)
    mdot = m_p / dt

    #Stangation Temperature
    T_s = T_c

    #Throat Temperature
    T_t = T_s * (1 + ((gamma - 1 ) / 2)) ** (-1)

    #Chamber Sonic Velocity
    c_c = math.sqrt(gamma * R_s * T_c)

    #Throat Sonic Velocity
    c_t = math.sqrt(gamma * R_s * T_t)

    #Throat Velocity
    v_t = c_t

    return [mdot, T_t, R_s, c_c]

def recursiveCalculations(vars, P_e, mdot, T_t):
    Ma_e, P_c, epsilon, A_t = vars

    #Throat Area (12)
    A_t = A_e / epsilon

    #Chamber Pressure (13)
    P_c = ((mdot * numpy.sqrt(T_t)) / A_t) * numpy.sqrt(R_s / gamma) * ((gamma + 1) / 2) ** ((gamma + 1) / (2 * (gamma - 1)))

    #Exit Mach Number (14)
    Ma_e = numpy.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ** ((gamma - 1) / gamma) - 1))

    #Area Ratio (15)
    epsilon = ((gamma + 1) / 2) ** (1 / (gamma - 1)) * (P_e / P_c) ** (1 / gamma) * numpy.sqrt(((gamma + 1) / (gamma - 1)) * (1 - (P_e / P_c) ** ((gamma - 1) / gamma)))

    return [Ma_e, P_c, epsilon, A_t]

def calculations2(P_c, c_c):
    #Stagnation Density (9)
    rho_s = (gamma * P_c) / c_c ** 2

    #Throat Density (7)
    rho_t = rho_s * (1 + ((gamma -1) / 2)) ** (-1 / (gamma - 1))

    #Stagnation Pressure (4)
    P_s = P_c

    #Throat Pressure (5)
    P_t = P_s * (1 + ((gamma - 1) / 2)) ** ((-1 * gamma) / (gamma - 1))

    return [P_t, rho_t]

results = calculations1()
mdot, T_t, R_s, c_c = results

vars = [Ma_e, P_c, epsilon, A_t]
results = fsolve(recursiveCalculations, vars, args=(P_e, mdot, T_t))
Ma_e, P_c, epsilon, A_t = results

results = calculations2(P_c, c_c)
P_t, rho_t = results

print("mdot: ", mdot, "\nT_t: ", T_t, "\nR_s: ", R_s, "\nc_c: ", c_c, "\nMa_e: ", Ma_e, "\nP_c: ", P_c, "\nepsilon: ", epsilon, "\nA_t: ", A_t, "\nP_t: ", P_t, "\nrho_t: ", rho_t)
import math

#Input Variables
m_p = 10#Total Available Propellant Mass (kg)
dt = 20#Total Burn Time (S)
A_e = 0.1#Exit Area (M^2)
gamma = 1.31#Ratio of Specific heats
M = 24#Sum of Molar Mass of Gasses
T_c = 3000#Chamber Temperature (k)
P_e = 100#Exit Pressure

#TEMP Variables to Find

#Building Application

#Equations
def math():
    #Specific Gas Consant (1)
    R_s = 8.134462618 / M

    #Mass Flow Rate (2)
    mdot = m_p / dt

    #Stangation Temperature (3)
    T_s = T_c

    #Stagnation Pressure (4)
    P_s = P_c

    #Throat Pressure (5)
    P_t = P_s * (1 + ((gamma - 1) / 2)) ^ ((-1 * gamma) / (gamma - 1))

    #Throat Temperature (6)
    T_t = T_s * (1 + ((gamma - 1 ) / 2)) ^ (-1)

    #Throat Density (7)
    rho_t = rho_s * (1 + ((gamma -1) / 2)) ^ (-1 / (gamma - 1))

    #Chamber Sonic Velocity (8)
    c_c = math.sqrt(gamma * R_s * T_c)

    #Stagnation Density (9)
    rho_s = (gamma * P_c) / c_c ^ 2

    #Throat Sonic Velocity (10)
    c_t = math.sqrt(gamma * R_s * T_t)

    #Throat Velocity (11)
    v_t = c_t

    #Throat Area (12)
    A_t = (mdot / (rho_t * v_t))

    #Chamber Pressure (13)
    P_c = ((mdot * math.sqrt(T_t)) / A_t) * math.sqrt(R_s / gamma) * ((gamma + 1) / 2) ^ ((gamma + 1) / (2 * (gamma - 1)))

    #Exit Mach Number (14)
    Ma_e = math.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ^ ((gamma - 1) / gamma) - 1))

    #Area Ratio (15)
    epsilon = ((gamma + 1) / 2) ^ ((gamma + 1) / (2 * (gamma -1))) * Ma_e * (1 + ((gamma - 1) / 2) * Ma_e ^ 2) ^ (-1 * ((gamma + 1) / (2 * (gamma - 1))))
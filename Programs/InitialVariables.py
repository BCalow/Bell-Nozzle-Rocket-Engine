import math

#Input Variables
m_p = 10#Total Available Propellant Mass (kg)
dt = 20#Total Burn Time (S)
A_e = 0.1#Exit Area (M^2)
gamma = 1.31#Ratio of Specific heats
M_m = 24#Sum of Molar Mass of Gasses
T_c = 3000#Chamber Temperature (k)
P_e = 100#Exit Pressure

#TEMP Variables to Find
mdot = 1#Mass Flow Rate
R_s = 1#Specific Heat Constant
rho_s = 1#Stagnation Density

#Building Application

#Equations
def math():
    #Stangation Temperature
    T_s = T_c
    #Stagnation Pressure
    P_s = P_c
    #Throat Pressure
    P_t = P_s * (1 + ((gamma - 1) / 2)) ^ ((-1 * gamma) / (gamma - 1))
    #Throat Temperature
    T_t = T_s * (1 + ((gamma - 1 ) / 2)) ^ (-1)
    #Throat Density
    rho_t = rho_s * (1 + ((gamma -1) / 2)) ^ (-1 / (gamma - 1))
    #Throat Sonic Velocity
    c_t = math.sqrt(gamma * R_s * T_t)
    #Throat Velocity
    v_t = c_t
    #Throat Area
    A_t = (mdot / (rho_t * v_t))
    #Chamber Pressure
    P_c = ((mdot * math.sqrt(T_t)) / A_t) * math.sqrt(R_s / gamma) * ((gamma + 1) / 2) ^ ((gamma + 1) / (2 * (gamma - 1)))
    #Exit Mach Number
    Ma_e = math.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ^ ((gamma - 1) / gamma) - 1))
    #Area Ratio
    epsilon = ((gamma + 1) / 2) ^ ((gamma + 1) / (2 * (gamma -1))) * Ma_e * (1 + ((gamma - 1) / 2) * Ma_e ^ 2) ^ (-1 * ((gamma + 1) / (2 * (gamma - 1))))
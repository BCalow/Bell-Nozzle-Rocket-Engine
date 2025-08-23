import numpy as np
import matplotlib.pyplot as plt



#Setting Up Plot
plt.style.use('dark_background')



#Input Variables
M = 0.03        #Molar Mass of Exhaust Gasses       (Kg/kmol)

m_p = 25        #Available Propellent Mass          (Kg)

dt = 30         #Burn Time                          (S)

T_c = 3500      #Chamber Temperature                (C)

gamma = 1.31    #Ratio of Specific Heats

A_e = 0.004418  #Exit Area                          (m^2)

P_a = 101325    #Ambient Pressure                   (Pa)



#Preliminary Calculations
R_s = 8.31446261815324 / M                  #Specific Gas Constant

mdot = m_p / dt                             #Mass Flow Rate

T_s = T_c                                   #Stagnation Temperature

T_t = T_s * (1 + ((gamma - 1) / 2)) ** -1   #Throat Temperature

c_t = np.sqrt(gamma * R_s * T_t)            #Throat Sonic Velocity

v_t = c_t                                   #Throat Velocity



epsilon = np.linspace(1, 25, 1000)      #Creating Array of Possible epsilon Values


def calcs():
    R_s = 8.31446261815324 / M                  #Specific Gas Constant

    mdot = m_p / dt                             #Mass Flow Rate

    T_s = T_c                                   #Stagnation Temperature

    P_e = P_a                                   #Exit Pressure

    T_t = T_s * (1 + ((gamma - 1) / 2)) ** -1   #Throat Temperature

    c_t = np.sqrt(gamma * R_s * T_t)            #Throat Sonic Velocity

    v_t = c_t                                   #Throat Velocity

    #Throat Area
    A_t = A_e / epsilon

    #Chamber Pressure
    P_c = ((mdot * np.sqrt(T_t)) / A_t) * np.sqrt(R_s / gamma) * ((gamma + 1) / 2) ** ((gamma + 1) * (2 * (gamma - 1)))

    #Mach Exit Number
    Ma_e = np.sqrt((2 / (gamma - 1)) * ((P_c / P_e) ** ((gamma - 1) / gamma) - 1))

    T_e = T_s * (1 + ((gamma - 1) / 2) * Ma_e ** 2) ** -1

    c_e = np.sqrt(gamma * R_s * T_e)

    V_e = Ma_e * c_e

    F = mdot * V_e

    return [R_s, mdot, T_s, P_e, T_t, c_t, v_t, A_t, P_c, Ma_e, V_e, F]

R_s, mdot, T_s, P_e, T_t, c_t, v_t, A_t, P_c, Ma_e, V_e, F  = calcs()

#Plotting
fig, ax1 = plt.subplots()
ax1.plot(epsilon, Ma_e, color='red')

ax2 = ax1.twinx()
ax2.plot(epsilon, P_c, color='green')

ax3 = ax1.twinx()
ax3.plot(epsilon, A_t, color='white')

ax4 = ax1.twinx()
ax4.plot(epsilon, V_e, color='blue')

ax5 = ax1.twinx()
ax5.plot(epsilon, F, color='yellow')

fig.tight_layout()
plt.show()
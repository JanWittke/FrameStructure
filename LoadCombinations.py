# We are looking for the maximal internal forces ==============================================================================================
# Load combination 1 -> Snow as relevant force
# Load combination 2 -> Wind as relevant force
# First for the moment =======================================================================================================================

import InternalForcesCalculation
round_Moment_P_sd = InternalForcesCalculation.round_Moment_P_sd
round_Shear_force_P_sd = InternalForcesCalculation.round_Shear_force_P_sd
round_Normal_force_P_sd = InternalForcesCalculation.round_Normal_force_P_sd
round_Moment_P_wd = InternalForcesCalculation.round_Moment_P_wd
round_Shear_force_P_wd = InternalForcesCalculation.round_Shear_force_P_wd
round_Normal_force_P_wd = InternalForcesCalculation.round_Normal_force_P_wd

import InputValues
wd = InputValues.wd
H = InputValues.H


round_Moment_P_wd_60 = [i * 0.6 for i in round_Moment_P_wd]
round_Moment_P_sd_50 = [i * 0.5 for i in round_Moment_P_sd]

total_Moment_LK1 = [i + j for i, j in zip(round_Moment_P_sd, round_Moment_P_wd_60)]
total_Moment_LK1 = [round(num, 2) for num in total_Moment_LK1]
#print("M_total_LK1: a,b,c,d,e,f,g:" ,total_Moment_LK1,)

total_Moment_LK2 = [i + j for i, j in zip(round_Moment_P_sd_50, round_Moment_P_wd)]
total_Moment_LK2 = [round(num, 2) for num in total_Moment_LK2]
#print("M_total_LK2: a,b,c,d,e,f,g:" ,total_Moment_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Moment_LK1 = [-i if i <0 else i for i in total_Moment_LK1 ]
abs_total_Moment_LK2 = [-i if i <0 else i for i in total_Moment_LK2 ]

#print(abs_total_Moment_LK1)
#print(abs_total_Moment_LK2)

M_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Moment_LK1[i] >= abs_total_Moment_LK2[i]:
        M_d[i] = abs_total_Moment_LK1[i]
    else:
        M_d[i] = abs_total_Moment_LK2[i]
    i = i+1
#print("|M_d|: a,b,c,d,e,f,g",M_d,)

#There is a special feature with the moment
#The corner moment does not necessarily have to be decisive for the calculation, but theoretically it could also be the field moment
#This will be checked in the following step and taken into account if necessary

M_d_feld = M_d[1]*(2/3) + (wd*(H**2))/9 # The formula here is again not 100% correct but already relatively accurate
M_d_feld = round(M_d_feld, 2)

#print(M_d_feld)
if M_d[1] >= M_d_feld:
    M_d[1] = M_d[1]
else:
    M_d[0] = M_d_feld

# Shear force =========================================================================================================
round_Shear_force_P_wd_60 = [i * 0.6 for i in round_Shear_force_P_wd]
round_Shear_force_P_sd_50 = [i * 0.5 for i in round_Shear_force_P_sd]

total_Shear_force_LK1 = [i + j for i, j in zip(round_Shear_force_P_sd, round_Shear_force_P_wd_60)]
total_Shear_force_LK1 = [round(num, 2) for num in total_Shear_force_LK1]
#print("Q_total_LK1: a,b,c,d,e,f,g:" ,total_Shear_force_LK1,)

total_Shear_force_LK2 = [i + j for i, j in zip(round_Shear_force_P_sd_50, round_Shear_force_P_wd)]
total_Shear_force_LK2 = [round(num, 2) for num in total_Shear_force_LK2]
#print("Q_total_LK2: a,b,c,d,e,f,g:" ,total_Shear_force_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Shear_force_LK1 = [-i if i <0 else i for i in total_Shear_force_LK1 ]
abs_total_Shear_force_LK2 = [-i if i <0 else i for i in total_Shear_force_LK2 ]

#print(abs_total_Shear_force_LK1)
#print(abs_total_Shear_force_LK2)

Q_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Shear_force_LK1[i] >= abs_total_Shear_force_LK2[i]:
        Q_d[i] = abs_total_Shear_force_LK1[i]
    else:
        Q_d[i] = abs_total_Shear_force_LK2[i]
    i = i+1
#print("|Q_d|: a,b,c,d,e,f,g",Q_d,)

# Axial force = normal force =========================================================================================================
round_Normal_force_P_wd_60 = [i * 0.6 for i in round_Normal_force_P_wd]
round_Normal_force_P_sd_50 = [i * 0.5 for i in round_Normal_force_P_sd]

total_Normal_force_LK1 = [i + j for i, j in zip(round_Normal_force_P_sd, round_Normal_force_P_wd_60)]
total_Normal_force_LK1 = [round(num, 2) for num in total_Normal_force_LK1]
#print("N_total_LK1: a,b,c,d,e,f,g:" ,total_Normal_force_LK1,)

total_Normal_force_LK2 = [i + j for i, j in zip(round_Normal_force_P_sd_50, round_Normal_force_P_wd)]
total_Normal_force_LK2 = [round(num, 2) for num in total_Normal_force_LK2]
#print("N_total_LK2: a,b,c,d,e,f,g:" ,total_Normal_force_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Normal_force_LK1 = [-i if i <0 else i for i in total_Normal_force_LK1 ]
abs_total_Normal_force_LK2 = [-i if i <0 else i for i in total_Normal_force_LK2 ]

#print(abs_total_Normal_force_LK1)
#print(abs_total_Normal_force_LK2)

N_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Normal_force_LK1[i] >= abs_total_Normal_force_LK2[i]:
        N_d[i] = abs_total_Normal_force_LK1[i]
    else:
        N_d[i] = abs_total_Normal_force_LK2[i]
    i = i+1
#print("|N_d|: a,b,c,d,e,f,g",N_d,)

# Now the whole thing is brought to the component level
# First group M,Q,N for the column and the truss
# Then finally build a list, the M,Q,N for the column and the truss respectively. This list can be used later for the calculation

M_max_value_truss = max(M_d[2:5])
#print("M maximum value in the truss:", M_max_value_truss)

M_max_value_1 = max(M_d[0:2])
M_max_value_2 = max(M_d[5:7])
if M_max_value_1 >= M_max_value_2:
    M_max_value_pillar = M_max_value_1
else:
    M_max_value_pillar = M_max_value_2

#print("M maximum value in the pillar:", M_max_value_pillar)


Q_max_value_truss = max(Q_d[2:5])
#print("Q maximum value in the truss:", Q_max_value_truss)

Q_max_value_1 = max(Q_d[0:2])
Q_max_value_2 = max(Q_d[5:7])
if Q_max_value_1 >= Q_max_value_2:
    Q_max_value_pillar = Q_max_value_1
else:
    Q_max_value_pillar = Q_max_value_2

#print("Q maximum value in the pillar:", Q_max_value_pillar)


N_max_value_truss = max(N_d[2:5])
#print("N maximum value in the truss:", N_max_value_truss)

N_max_value_1 = max(N_d[0:2])
N_max_value_2 = max(N_d[5:7])
if N_max_value_1 >= N_max_value_2:
    N_max_value_pillar = N_max_value_1
else:
    N_max_value_pillar = N_max_value_2

#print("N maximum value in the pillar:", N_max_value_pillar)

# Finally, build a component array with the respective design internal forces

Internal_forces_truss = [M_max_value_truss,Q_max_value_truss,N_max_value_truss]
#print("The internal forces in the truss are: M_max =",Internal_forces_truss[0],"kNm; Q_max =",Internal_forces_truss[1],"kN; N_max =",-Internal_forces_truss[2],"kN !")

Internal_forces_pillar = [M_max_value_pillar,Q_max_value_pillar,N_max_value_pillar]
#print("The internal forces in the pillar are: M_max =",Internal_forces_pillar[0],"kNm; Q_max =",Internal_forces_pillar[1],"kN; N_max =",-Internal_forces_pillar[2],"kN !")

Truss_MQN = Internal_forces_truss
Pillar_MQN = Internal_forces_pillar

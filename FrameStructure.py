#Hello! This is your tool for a preselection of  a steel frame!
#First we have to enter the variabels

x = 1 #No other variants for static systems are available yet

V = input("Enter the needed Height, Wide and Length of your hall in [m]: (H,W,L): ")
V_einzeln = V.split(',')

H = V_einzeln[0]
W = V_einzeln[1]
L_total = V_einzeln[2]

H = float(H)
W = float(W)
L_total = float(L_total)

if H < 3 or W < 6 or L_total < 15:
    print("The Height should be between 3 and 20 [m].")
    print("The Wide should be between 6 and 30 [m].")
    print("The Length should be between 15 and 200 [m].")
    quit()
if H > 20 or W > 30 or L_total > 200:
    print("The Height should be between 3 and 20 [m].")
    print("The Wide should be between 6 and 30 [m].")
    print("The Length should be between 15 and 200 [m].")
    quit()


Load =  input("Enter the snow load s_k and the wind load w_k in [kN/m2]: (s_k,w_k): ")
Load_split = Load.split(',')

sk = Load_split[0]
wk = Load_split[1]

sk = float(sk)
wk = float(wk)

#=============================================================================================================

if L_total <= 20:
    X = L_total/5
    X = round(X)
    Q = L_total/X

elif L_total <= 40:
    X = L_total/6
    X = round(X)
    Q = L_total/X

elif L_total <= 60:
    X = L_total/7
    X = round(X)
    Q = L_total/X

elif L_total <= 80:
    X = L_total/8
    X = round(X)
    Q = L_total/X

elif L_total <= 100:
    X = L_total/10
    X = round(X)
    Q = L_total/X

elif L_total < 100:
    X = L_total/12
    X = round(X)
    Q = L_total/X

L_section = Q.__round__(2)


print("The hall is divided into",X,"sections with a distance of",L_section,"[m]. In total we have",X+1,"frames.")


sd = sk * 1.5 * L_section #kN/m
wd = wk * 1.5 * L_section #kN/m

sd = sd.__round__(2)
wd = wd.__round__(2)

print("This results in design line loads for the snow load of s_d =",sd,"[kN/m] and for the wind load of w_d =",wd,"[kN/m].")


#Calculation of the internal forces on a three hinged frame
#Snowload =======================================================================================================
# M = moment
# Q = shear force (Querkraft)
# N = axial force (Normalkraft)



Ma_sd = 0
Mb_sd = - sd * (W**2)/8
Mc_sd = Mb_sd
Md_sd = 0
Me_sd = Mb_sd
Mf_sd = Me_sd
Mg_sd = 0
Moment_P_sd = [Ma_sd,Mb_sd,Mc_sd,Md_sd,Me_sd,Mf_sd,Mg_sd] #P = point
round_Moment_P_sd = [round(num, 2) for num in Moment_P_sd]

M1_sd = Mb_sd
M2_sd = Mb_sd
M3_sd = Mb_sd
M4_sd = Mb_sd
Moment_E_sd = [M1_sd,M2_sd,M3_sd,M4_sd] #E = element
round_Moment_E_sd = [round(num, 2) for num in Moment_E_sd]

#print("M_sd: a,b,c,d,e,f,g :",round_Moment_P_sd,)
#print("M_sd: 1,2,3,4 :",round_Moment_E_sd,)
#print("                 linear, quadratic, quadratic, linear")

Qa_sd = Mb_sd/H
Qb_sd = Qa_sd
Qc_sd = sd * W/2
Qd_sd = 0
Qe_sd = - Qc_sd
Qf_sd = -Qa_sd
Qg_sd = Qf_sd
Shear_force_P_sd = [Qa_sd,Qb_sd,Qc_sd,Qd_sd,Qe_sd,Qf_sd,Qg_sd]
round_Shear_force_P_sd = [round(num, 2) for num in Shear_force_P_sd]

Q1_sd = Qa_sd
Q2_sd = Qc_sd
Q3_sd = Qe_sd
Q4_sd = Qf_sd
Shear_force_E_sd = [Q1_sd,Q2_sd,Q3_sd,Q4_sd]
round_Shear_force_E_sd = [round(num, 2) for num in Shear_force_E_sd]

#print("Q_sd: a,b,c,d,e,f,g :",round_Shear_force_P_sd,)
#print("Q_sd: 1,2,3,4 :",round_Shear_force_E_sd,)
#print("                 constant, linear, linear, constant")

Av_sd = sd * W/2
Gv_sd = Av_sd

N1_sd = - Av_sd
N2_sd = Q1_sd
N3_sd = N2_sd
N4_sd = N1_sd
Normal_force_sd = [N1_sd,N2_sd,N3_sd,N4_sd]
round_Normal_force_sd = [round(num, 2) for num in Normal_force_sd]

Normal_force_P_sd = [N1_sd,N1_sd,N2_sd,N2_sd,N3_sd,N4_sd,N4_sd]
round_Normal_force_P_sd = [round(num, 2) for num in Normal_force_P_sd]

#print("N_sd: a,b,c,d,e,f,g :",round_Normal_force_P_sd,)
#print("N_sd: 1,2,3,4 :",round_Normal_force_sd,)
#print("                 constant, constant, constant, constant")

#one-sided wind load =================================================================================

Gv_wd = (wd*H**2)/(2*W)
Av_wd = -Gv_wd

Gh_wd = (Gv_wd*W)/(2*H)
Qg_wd = Gh_wd

N4_wd = - Gv_wd
N1_wd = -Av_wd

Q3_wd = N4_wd
Md_wd = Q3_wd*W/2

Ma_wd = 0
Mb_wd = - Md_wd
Mc_wd = Mb_wd
Md_wd = 0
Me_wd = -Mb_wd
Mf_wd = Me_wd
Mg_wd = 0
Moment_P_wd = [Ma_wd,Mb_wd,Mc_wd,Md_wd,Me_wd,Mf_wd,Mg_wd] #P = point
round_Moment_P_wd = [round(num, 2) for num in Moment_P_wd]

M1_wd = Mb_wd*2/3 + (wd*(H**2))/9 # this formula is not fully correct but for the moments its ok because this value is not relevant
M2_wd = Mb_wd
M3_wd = Me_wd
M4_wd = Mf_wd
Moment_E_wd = [M1_wd,M2_wd,M3_wd,M4_wd] #E = element
round_Moment_E_wd = [round(num, 2) for num in Moment_E_wd]

#print("M_wd: a,b,c,d,e,f,g :",round_Moment_P_wd,)
#print("M_wd: 1,2,3,4 :",round_Moment_E_wd,)
#print("                 quadratic, linear, linear, linear")
M1_wd = Mb_wd #the moment is changed here again, so that the corner moment is decisive for M_ges.
Moment_E_wd = [M1_wd,M2_wd,M3_wd,M4_wd] #E = element #saved again


Qa_wd = -Qg_wd + wd*H
Qb_wd = -Qg_wd
Qc_wd = N4_wd
Qd_wd = N4_wd
Qe_wd = N4_wd
Qf_wd = Qg_wd
Qg_wd = Qg_wd
Shear_force_P_wd = [Qa_wd,Qb_wd,Qc_wd,Qd_wd,Qe_wd,Qf_wd,Qg_wd]
round_Shear_force_P_wd = [round(num, 2) for num in Shear_force_P_wd]

Q1_wd = Qa_wd
Q2_wd = Qc_wd
Q3_wd = Qe_wd
Q4_wd = Qf_wd
Shear_force_E_wd = [Q1_wd,Q2_wd,Q3_wd,Q4_wd]
round_Shear_force_E_wd = [round(num, 2) for num in Shear_force_E_wd]

#print("Q_wd: a,b,c,d,e,f,g :",round_Shear_force_P_wd,)
#print("Q_wd: 1,2,3,4 :",round_Shear_force_E_wd,)
#print("                 linear, constant, constant, constant")

N1_wd = -Av_wd
N2_wd = -Q4_wd
N3_wd = -Q4_wd
N4_wd = - Gv_wd
Normal_force_wd = [N1_wd,N2_wd,N3_wd,N4_wd]
round_Normal_force_wd = [round(num, 2) for num in Normal_force_wd]

Normal_force_P_wd = [N1_wd,N1_wd,N2_wd,N2_wd,N3_wd,N4_wd,N4_wd]
round_Normal_force_P_wd = [round(num, 2) for num in Normal_force_P_wd]

#print("N_wd: a,b,c,d,e,f,g :",round_Normal_force_P_wd,)
#print("N_wd: 1,2,3,4 :",round_Normal_force_wd,)
#print("                 constant, constant, constant, constant")

# We are looking for the maximal internal forces ==============================================================================================
# Load combination 1 -> Snow as relevent force
# Load combination 2 -> Wind as relevent force
# First for the moment =======================================================================================================================

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
print("The internal forces in the truss are: M_max =",Internal_forces_truss[0],"kNm; Q_max =",Internal_forces_truss[1],"kN; N_max =",-Internal_forces_truss[2],"kN !")

Internal_forces_pillar = [M_max_value_pillar,Q_max_value_pillar,N_max_value_pillar]
print("The internal forces in the pillar are: M_max =",Internal_forces_pillar[0],"kNm; Q_max =",Internal_forces_pillar[1],"kN; N_max =",-Internal_forces_pillar[2],"kN !")

Truss_MQN = Internal_forces_truss
Pillar_MQN = Internal_forces_pillar

# Import Profile list for the truss

#gk =  input("Enter now the own weight of the roof g_k in [kN/m2]: (g_k): ")
#gk = float(gk)
#gk_roof = gk * L_section #kN/m
#print(gk_roof)

import math
import sys
import pandas
import numpy

import InputValues
W = InputValues.W
sd = InputValues.sd
gk_roof = InputValues.gk_roof

import InternalForcesCalculation
Moment_P_sd = InternalForcesCalculation.Moment_P_sd
Shear_force_P_sd = InternalForcesCalculation.Shear_force_P_sd
Normal_force_P_sd = InternalForcesCalculation.Normal_force_P_sd

import LoadCombinations
M_d = LoadCombinations.M_d
Q_d = LoadCombinations.Q_d
N_d = LoadCombinations.N_d

IPE = []
IPE = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\IPE-profiles.xlsx")
HEA = []
HEA = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEA-profiles.xlsx")
HEB = []
HEB = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEB-profiles.xlsx")

#print(IPE)

# Starting with IPE =================================================================================================
# Zuerst wird das Eigengewicht ermittelt
# Dieses besteht aus dem Eigengewicht des Profils (gk_vektor_IPE) und der Dachkonstruktion (gk_vektor_roof)

mass_vektor_IPE = []
gk_vektor_roof = []
sd_vektor = []

num_rows_IPE = IPE.shape[0]
num_rows_IPE = int(num_rows_IPE)

for i in range(num_rows_IPE):
    mass = IPE.iat[i, 8]
    mass_vektor_IPE.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)


gk_vektor_IPE = []
factor_gk = 9.81/1000

for value in mass_vektor_IPE:
    new_value = value * factor_gk
    gk_vektor_IPE.append(new_value)

gk_vektor_IPE = [round(num, 2) for num in gk_vektor_IPE]

gk_vektor = [a + b for a, b in zip(gk_vektor_IPE, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)
gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = IPE.shape[0]

# Das Eigengewicht ist nun als Liste für alle Profile abgespeichert
# Im nächsten Schritt werden für alle Profile die neuen Schnittgrößen berechnet

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)


# This is a lot of code, so I will store it in a function

def Internal_Forces_Matrix(factor_vektor,num_factor_vektor):
    # For the Moment===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Moment_P_gd_matrix = []
    M_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Moment_P_gd = [i * factor for i in Moment_P_sd]
        Moment_P_gd = [round(num, 2) for num in Moment_P_gd]
        abs_Moment_P_gd = [-i if i < 0 else i for i in Moment_P_gd]
        abs_Moment_P_gd_matrix.append(abs_Moment_P_gd)
        M_d_matrix.append(M_d)

    #print(abs_Moment_P_gd_matrix)
    #print(M_d_matrix)

    M_d_new_matrix = [[abs_Moment_P_gd_matrix[i][j] + M_d_matrix[i][j] for j in range(len(abs_Moment_P_gd_matrix[0]))]
                      for i in range(len(abs_Moment_P_gd_matrix))]

    #for row in M_d_new_matrix:
     #   print(row)
   # print(M_d_new_matrix)

    max_values = [max(row[2:5]) for row in M_d_new_matrix]
    m_max_values = [round(num, 3) for num in max_values]

    #print(m_max_values)

    # For the Shear Force===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Shear_force_P_gd_matrix = []
    Q_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Shear_force_P_gd = [i * factor for i in Shear_force_P_sd]
        Shear_force_P_gd = [round(num, 2) for num in Shear_force_P_gd]
        abs_Shear_force_P_gd = [-i if i < 0 else i for i in Shear_force_P_gd]
        abs_Shear_force_P_gd_matrix.append(abs_Shear_force_P_gd)
        Q_d_matrix.append(Q_d)

    # print(abs_Shear_force_P_gd_matrix)
    # print(Q_d_matrix)

    Q_d_new_matrix = [
        [abs_Shear_force_P_gd_matrix[i][j] + Q_d_matrix[i][j] for j in range(len(abs_Shear_force_P_gd_matrix[0]))] for i
        in range(len(abs_Shear_force_P_gd_matrix))]

    # for row in Q_d_new_matrix:
    #   print(row)
    # print(Q_d_new_matrix)

    max_values = [max(row[2:5]) for row in Q_d_new_matrix]
    q_max_values = [round(num, 3) for num in max_values]

    # print(m_max_values)

    # For the Axial Force===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Normal_force_P_gd_matrix = []
    N_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Normal_force_P_gd = [i * factor for i in Normal_force_P_sd]
        Normal_force_P_gd = [round(num, 2) for num in Normal_force_P_gd]
        abs_Normal_force_P_gd = [-i if i < 0 else i for i in Normal_force_P_gd]
        abs_Normal_force_P_gd_matrix.append(abs_Normal_force_P_gd)
        N_d_matrix.append(N_d)

    # print(abs_Normal_force_P_gd_matrix)
    # print(N_d_matrix)

    N_d_new_matrix = [
        [abs_Normal_force_P_gd_matrix[i][j] + N_d_matrix[i][j] for j in range(len(abs_Normal_force_P_gd_matrix[0]))] for
        i in range(len(abs_Normal_force_P_gd_matrix))]

    # for row in N_d_new_matrix:
    #   print(row)
    # print(n_d_new_matrix)

    max_values = [max(row[2:5]) for row in N_d_new_matrix]
    n_max_values = [round(num, 3) for num in max_values]

    return m_max_values, q_max_values, n_max_values #return the 3 important lists

    # print(N_max_values)

    # end of def - function

#Internal_Forces_Matrix()
Result_IPE = []
Result_IPE = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_IPE

Truss_MQN_Matrix_IPE = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_IPE = [list(row) for row in zip(*Truss_MQN_Matrix_IPE)]

#for row in Truss_MQN_Matrix_IPE:
 #   print(row)

# Now for HEA =========================================================================================================

mass_vektor_HEA = []
num_rows_HEA =HEA.shape[0]
num_rows_HEA = int(num_rows_HEA)
gk_vektor_roof = []
sd_vektor = []


for i in range(num_rows_HEA):
    mass = HEA.iat[i, 8]
    mass_vektor_HEA.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)

gk_vektor_HEA = []
factor_gk = 9.81/1000

for value in mass_vektor_HEA:
    new_value = value * factor_gk
    gk_vektor_HEA.append(new_value)

gk_vektor_HEA = [round(num, 2) for num in gk_vektor_HEA]

gk_vektor = [a + b for a, b in zip(gk_vektor_HEA, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)
gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = HEA.shape[0]

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)

# take results from same function
Internal_Forces_Matrix(factor_vektor,num_factor_vektor)
Result_HEA = []
Result_HEA = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_HEA

Truss_MQN_Matrix_HEA = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_HEA = [list(row) for row in zip(*Truss_MQN_Matrix_HEA)]

#for row in Truss_MQN_Matrix_HEA:
 #   print(row)


# Now for HEB =========================================================================================================

mass_vektor_HEB = []
num_rows_HEB =HEB.shape[0]
num_rows_HEB = int(num_rows_HEB)
gk_vektor_roof = []
sd_vektor = []


for i in range(num_rows_HEB):
    mass = HEB.iat[i, 8]
    mass_vektor_HEB.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)

gk_vektor_HEB = []
factor_gk = 9.81/1000

for value in mass_vektor_HEB:
    new_value = value * factor_gk
    gk_vektor_HEB.append(new_value)

gk_vektor_HEB = [round(num, 2) for num in gk_vektor_HEB]

gk_vektor = [a + b for a, b in zip(gk_vektor_HEB, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)

gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = HEB.shape[0]

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)

# take results from same function
Internal_Forces_Matrix(factor_vektor,num_factor_vektor)
Result_HEB = []
Result_HEB = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_HEB

Truss_MQN_Matrix_HEB = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_HEB = [list(row) for row in zip(*Truss_MQN_Matrix_HEB)]

#for row in Truss_MQN_Matrix_HEB:
 #   print(row)

#=====================================================================================================================
#=====================================================================================================================
#=====================================================================================================================

# M-Nachweis generell
def M_function (W_pl_i, M_ed, f_y):
    M_pl_Rd_i = W_pl_i * f_y / 100  # kNm
    eta_M_i = M_ed / M_pl_Rd_i

    return eta_M_i


# MN-Nachweis generell
def MN_interaction (W_pl_i ,A_i ,h_i , t_w_i, b_i, t_f_i ,M_ed ,N_ed, f_y):

    M_pl_Rd_i = W_pl_i * f_y / 100      # kNm
    N_pl_Rd_i = A_i * f_y          # kN
    h_w_i = h_i - 2 * t_f_i

    N_pl_Rd_i_red_1 = 0.25 * N_pl_Rd_i
    N_pl_Rd_i_red_2 = 0.5 * h_w_i * t_w_i * f_y
    N_pl_Rd_i_red = min(N_pl_Rd_i_red_1, N_pl_Rd_i_red_2)

    if N_ed > N_pl_Rd_i_red:

        n = N_ed/N_pl_Rd_i

        a_1 = (A_i - 2 * b_i * t_f_i)/A_i
        a_2 = 0.5
        a = min(a_1, a_2)

        M_N_Rd_1 = M_pl_Rd_i * ((1-n)/(1-0.5*a))
        M_N_Rd_2 = M_pl_Rd_i
        M_N_Rd_i = min(M_N_Rd_1,M_N_Rd_2)           # kNm

        eta_MN_i = M_ed / M_N_Rd_i

    else:
        eta_MN_i = M_ed / M_pl_Rd_i

    return eta_MN_i

# N-Nachweis generell
def N_buckling (I_z_i,L_cr,A_i,N_ed,f_y):

    E = 21000 #KN/cm2
    N_pl_Rd_i = A_i * f_y   # kN
    #print(N_pl_Rd_i)
    N_cr_z = E * I_z_i * (math.pi**2)/L_cr**2

    lamda = (N_pl_Rd_i/N_cr_z)**(1/2)

    alpha = 0.34 # später noch ändern; verschiedene Fälle

    omega = 0.5 * (1 + alpha * (lamda - 0.2) + lamda**2)
    Xi = 1/(omega+(omega**2-lamda**2)**(1/2))
    Xi = min(Xi,1)
    N_b_Rd = Xi*N_pl_Rd_i/1.1

    eta_N_i = N_ed / N_b_Rd

    return eta_N_i


print("You can choose for the truss one of the profiles:")
# Ausnutzung IPE Träger =====================================================================================================================================================

count = 0
f_y = 23.5
L_cr = W * 100 # cm   # 2*W/2 because of buckling length

num_rows_XXX = num_rows_IPE
Eta_M_i_vektor = []
Eta_MN_i_vektor = []
Eta_N_i_vektor = []


for i in range(num_rows_XXX, 0, -1):
    i = i - 1

    M_ed = Truss_MQN_Matrix_IPE[i][0] * 1
    N_ed = Truss_MQN_Matrix_IPE[i][2] * 1
    S_x_i = IPE.iat[i, 16]
    W_pl_i = float(2 * S_x_i)  # cm3

    A_i = IPE.iat[i, 7]
    h_i = IPE.iat[i, 2]
    t_w_i = IPE.iat[i, 4]
    b_i = IPE.iat[i, 3]
    t_f_i = IPE.iat[i, 5]
    I_z_i = IPE.iat[i, 13]


    def Iteration (A_i,h_i,t_w_i,b_i,t_f_i,I_z_i,L_cr,count,Eta_M_i_vektor,Eta_MN_i_vektor,Eta_N_i_vektor):
        A_i = float(A_i)            # cm2
        h_i = float(h_i) / 10       # cm
        t_w_i = float(t_w_i) / 10   # cm
        b_i = float(b_i) / 10       # cm
        t_f_i = float(t_f_i) / 10   # cm
        I_z_i = float(I_z_i)        # cm4

        #Result_MN_interaction = []
        Result_MN_interaction = MN_interaction(W_pl_i, A_i, h_i, t_w_i, b_i, t_f_i, M_ed, N_ed,f_y)

        eta_MN_i = Result_MN_interaction
        Eta_MN_i = round(eta_MN_i, 2)  # Round to two decimal
        Eta_MN_i_vektor.append(Eta_MN_i)

        Result_M = M_function(W_pl_i, M_ed,f_y)

        eta_M_i = Result_M
        Eta_M_i = round(eta_M_i, 2)  # Round to two decimal
        Eta_M_i_vektor.append(Eta_M_i)

        Result_N = N_buckling (I_z_i,L_cr,A_i,N_ed,f_y)

        eta_N_i = Result_N
        Eta_N_i = round(eta_N_i, 2)  # Round to two decimal
        Eta_N_i_vektor.append(Eta_N_i)

        Eta_max_vektor = [max(x,y,z) for x,y,z in zip(Eta_M_i_vektor, Eta_MN_i_vektor, Eta_N_i_vektor)]

        count += 1

        return Eta_max_vektor, count



    Result_Iteration = Iteration(A_i,h_i,t_w_i,b_i,t_f_i,I_z_i,L_cr,count,Eta_M_i_vektor,Eta_MN_i_vektor,Eta_N_i_vektor)
    Eta_max_vektor, count = Result_Iteration

    Eta_max_vektor_IPE = Eta_max_vektor
    Wert = count -1
    Eta_max_IPE = Eta_max_vektor_IPE[Wert]
    #print("Eta_i =",Eta_max_IPE,)
    if Eta_max_IPE >= 0.9:
        if count == 1:
            print("The loads are too high! No suitable IPE profile found.")
            Auswahl_IPE = 0
            break
        else:
            profile_number_IPE = num_rows_XXX - count + 1
            eta_number_IPE = count - 2
            print("IPE", IPE.iat[profile_number_IPE, 1], "with eta =", Eta_max_vektor_IPE[eta_number_IPE], )

            Auswahl_IPE = IPE.iat[profile_number_IPE, 1]
            break

# Ausnutzung HEA Träger =====================================================================================================================================================

M_function (W_pl_i, M_ed, f_y)

MN_interaction (W_pl_i ,A_i ,h_i , t_w_i, b_i, t_f_i ,M_ed ,N_ed, f_y)

N_buckling (I_z_i,L_cr,A_i,N_ed,f_y)

count = 0
f_y = 23.5
L_cr = W * 100  # cm   # 2*W/2 because of buckling length

num_rows_XXX = num_rows_HEA
Eta_M_i_vektor = []
Eta_MN_i_vektor = []
Eta_N_i_vektor = []

for i in range(num_rows_XXX, 0, -1):
    i = i - 1

    M_ed = Truss_MQN_Matrix_HEA[i][0] * 1
    N_ed = Truss_MQN_Matrix_HEA[i][2] * 1
    S_x_i = HEA.iat[i, 16]
    W_pl_i = float(2 * S_x_i)  # cm3

    A_i = HEA.iat[i, 7]
    h_i = HEA.iat[i, 2]
    t_w_i = HEA.iat[i, 4]
    b_i = HEA.iat[i, 3]
    t_f_i = HEA.iat[i, 5]
    I_z_i = HEA.iat[i, 13]

    #Iteration(A_i,h_i,t_w_i,b_i,t_f_i,I_z_i,L_cr,count,Eta_M_i_vektor,Eta_MN_i_vektor,Eta_N_i_vektor)

    Result_Iteration = Iteration(A_i, h_i, t_w_i, b_i, t_f_i, I_z_i, L_cr, count, Eta_M_i_vektor, Eta_MN_i_vektor,
                                 Eta_N_i_vektor)
    Eta_max_vektor, count = Result_Iteration

    Eta_max_vektor_HEA = Eta_max_vektor
    Wert = count - 1
    Eta_max_HEA = Eta_max_vektor_HEA[Wert]
    #print("Eta_i =", Eta_max_HEA, )
    if Eta_max_HEA >= 0.9:
        if count == 1:
            print("The loads are too high! No suitable HEA profile found.")
            Auswahl_HEA = 0
            break
        else:
            profile_number_HEA = num_rows_XXX - count + 1
            eta_number_HEA = count - 2
            print("HEA", HEA.iat[profile_number_HEA, 1], "with eta =", Eta_max_vektor_HEA[eta_number_HEA], )

            Auswahl_HEA = HEA.iat[profile_number_HEA, 1]
            break


# Ausnutzung HEB Träger =====================================================================================================================================================

M_function (W_pl_i, M_ed, f_y)

MN_interaction (W_pl_i ,A_i ,h_i , t_w_i, b_i, t_f_i ,M_ed ,N_ed, f_y)

N_buckling (I_z_i,L_cr,A_i,N_ed,f_y)

count = 0
f_y = 23.5
L_cr = W * 100  # cm   # 2*W/2 because of buckling length

num_rows_XXX = num_rows_HEB
Eta_M_i_vektor = []
Eta_MN_i_vektor = []
Eta_N_i_vektor = []

for i in range(num_rows_XXX, 0, -1):
    i = i - 1

    M_ed = Truss_MQN_Matrix_HEB[i][0] * 1
    N_ed = Truss_MQN_Matrix_HEB[i][2] * 1
    S_x_i = HEB.iat[i, 16]
    W_pl_i = float(2 * S_x_i)  # cm3

    A_i = HEB.iat[i, 7]
    h_i = HEB.iat[i, 2]
    t_w_i = HEB.iat[i, 4]
    b_i = HEB.iat[i, 3]
    t_f_i = HEB.iat[i, 5]
    I_z_i = HEB.iat[i, 13]

    #Iteration(A_i,h_i,t_w_i,b_i,t_f_i,I_z_i,L_cr,count,Eta_M_i_vektor,Eta_MN_i_vektor,Eta_N_i_vektor)

    Result_Iteration = Iteration(A_i, h_i, t_w_i, b_i, t_f_i, I_z_i, L_cr, count, Eta_M_i_vektor, Eta_MN_i_vektor,
                                 Eta_N_i_vektor)
    Eta_max_vektor, count = Result_Iteration

    Eta_max_vektor_HEB = Eta_max_vektor
    Wert = count - 1
    Eta_max_HEB = Eta_max_vektor_HEB[Wert]
    #print("Eta_i =", Eta_max_HEB, )
    if Eta_max_HEB >= 0.9:
        if count == 1:
            print("The loads are too high! No suitable HEB profile found. Program is closed.")
            sys.exit()
            break
        else:
            profile_number_HEB = num_rows_XXX - count + 1
            eta_number_HEB = count - 2
            print("HEB", HEB.iat[profile_number_HEB, 1], "with eta =", Eta_max_vektor_HEB[eta_number_HEB], )

            Auswahl_HEB = HEB.iat[profile_number_HEB, 1]
            break


# ======================================================================================================================
# Auswahl und Ausgabe der Schnittgrößen
#print("You can now choose a profile for the truss: IPE", Auswahl_IPE, "or HEA", Auswahl_HEA, "or HEB",Auswahl_HEB, )
print("Write IPE or HEA or HEB to choose a profile!")

while True:
    profile_choice = input("Your profile choice: ")

    if (profile_choice == "IPE" or profile_choice == "Ipe" or profile_choice == "ipe") and Auswahl_IPE > 0:
        print("You choice is IPE", Auswahl_IPE, )
        print("The internal forces are: M_max =", Truss_MQN_Matrix_IPE[profile_number_IPE][0], "kNm; Q_max =",
              Truss_MQN_Matrix_IPE[profile_number_IPE][1], "kN; N_max =", -Truss_MQN_Matrix_IPE[profile_number_IPE][2],
              "kN !")
        break

    elif (profile_choice == "HEA" or profile_choice == "Hea" or profile_choice == "hea") and Auswahl_HEA > 0:
        print("You choice is HEA", Auswahl_HEA, )
        print("The internal forces are: M_max =", Truss_MQN_Matrix_HEA[profile_number_HEA][0], "kNm; Q_max =",
              Truss_MQN_Matrix_HEA[profile_number_HEA][1], "kN; N_max =", -Truss_MQN_Matrix_HEA[profile_number_HEA][2],
              "kN !")
        break

    elif (profile_choice == "HEB" or profile_choice == "Heb" or profile_choice == "heb") and Auswahl_HEB > 0:
        print("You choice is HEB", Auswahl_HEB, )
        print("The internal forces are: M_max =", Truss_MQN_Matrix_HEB[profile_number_HEB][0], "kNm; Q_max =",
              Truss_MQN_Matrix_HEB[profile_number_HEB][1], "kN; N_max =", -Truss_MQN_Matrix_HEB[profile_number_HEB][2],
              "kN !")
        break

    else:
        print("Please enter a valid profile.")



# ok wie geht es weiter?
# Ich will zwei NW führen! MQN NW und Stabilitäts NW
# Diese sind ziemlich aufwändig. Kann ich das als Funktion machen?
# Beachte: Für IPE, HEA und HEB ... später dann genau das selbe nochmal für Stütze...
# Wenn das klappt ist aber eigentlich alles wichtige geschafft
# danach den Code schöner machen
# Schnittgrößen neu berechnen? Version 2 und 3 wären damit sehr schnell möglich! ... theoretisch
# Webseite bauen und grafisch darstellen? Matlab?

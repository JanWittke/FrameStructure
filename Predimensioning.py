# Import old data here just example values

Truss_MQN = [388.24, 131.2, -77.65]
Pillar_MQN = [388.24, 93.72, -131.2]

L_section = 7.14
sd = 21.42

# Import Profile list for the truss

import pandas
IPE = []
IPE = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\IPE-profiles.xlsx")
HEA = []
HEA = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEA-profiles.xlsx")
HEB = []
HEB = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEB-profiles.xlsx")


M_Ed = Truss_MQN[0]*1.2 #Increase of 20% for later reserves

# Starting with IPE

W_pl_vector_IPE = []

num_rows_IPE = IPE.shape[0]
num_rows_IPE = int(num_rows_IPE)

for i in range(num_rows_IPE):
    S_x = IPE.iat[i, 16]#
    W_pl = float(2*S_x)
    row_number = IPE.iat[i, 0]
    profile = IPE.iat[i, 1]
    mass = HEA.iat[i, 8]
    W_pl_vector_IPE = [row_number,profile,W_pl,mass]

    M_cRD = (W_pl) * 23.5 / 100
    eta = M_Ed/M_cRD
    Eta_IPE = round(eta, 2)  # Round to two decimal

    if Eta_IPE <= 1:
        break

print(Eta_IPE)
print(W_pl_vector_IPE)


# Same for HEA

W_pl_vector_HEA = []

num_rows_HEA = HEA.shape[0]
num_rows_HEA = int(num_rows_HEA)

for i in range(num_rows_HEA):
    S_x = HEA.iat[i, 16]#
    W_pl = float(2*S_x)
    row_number = HEA.iat[i, 0]
    profile = HEA.iat[i, 1]
    mass = HEA.iat[i, 8]
    W_pl_vector_HEA = [row_number,profile,W_pl,mass]

    M_cRD = (W_pl) * 23.5 / 100
    eta = M_Ed/M_cRD
    Eta_HEA = round(eta, 2)  # Round to two decimal

    if Eta_HEA <= 1:
        break

print(Eta_HEA)
print(W_pl_vector_HEA)


# Same for HEB

W_pl_vector_HEB = []

num_rows_HEB = HEB.shape[0]
num_rows_HEB = int(num_rows_HEB)

for i in range(num_rows_HEB):
    S_x = HEB.iat[i, 16]#
    W_pl = float(2*S_x)
    row_number = HEB.iat[i, 0]
    profile = HEB.iat[i, 1]
    mass = HEA.iat[i, 8]
    W_pl_vector_HEB = [row_number,profile,W_pl,mass]

    M_cRD = (W_pl) * 23.5 / 100
    eta = M_Ed/M_cRD
    Eta_HEB = round(eta, 2)  # Round to two decimal

    if Eta_HEB <= 1:
        break

print(Eta_HEB)
print(W_pl_vector_HEB)

if Eta_IPE <= 1 and Eta_HEA <= 1 and Eta_HEB <= 1:
    print("You can now choose a profile for the truss: IPE",W_pl_vector_IPE[1],"or HEA",W_pl_vector_HEA[1],"or HEB",W_pl_vector_HEB[1],)
    print("Write IPE or HEA or HEB to choose a profile!")

    profile_choice = input("Your profile choice: ")

    if profile_choice == "IPE":
        print("You choice is IPE",W_pl_vector_IPE[1],)
    elif profile_choice == "HEA":
        print("You choice is HEA",W_pl_vector_HEA[1],)
    elif profile_choice == "HEB":
        print("You choice is HEB",W_pl_vector_HEB[1],)
    else:
        print("Invalid entry. Please enter IPE or HEA or HEB!")

elif Eta_HEA <= 1 and Eta_HEB <= 1:
    print("You can now choose a profile for the truss: HEA",W_pl_vector_HEA[1], "or HEB",W_pl_vector_HEB[1],)
    print("Write HEA or HEB to choose a profile!")

    profile_choice = input("Your profile choice: ")

    if profile_choice == "HEA":
        print("You choice is HEA",W_pl_vector_HEA[1],)
    elif profile_choice == "HEB":
        print("You choice is HEB",W_pl_vector_HEB[1],)
    else:
        print("Invalid entry. Please enter HEA or HEB!")
elif Eta_HEB <= 1:
    print("You can now choose as profile for the truss: HEB",W_pl_vector_HEB[1],)
    print("Automatic selection of HEB",W_pl_vector_HEB[1],)
else:
    print("Your internal forces are to high!")


# Add the self weight

g_k_roof = 0.5 * L_section #kN/m

if profile_choice == "IPE":
    g_k_profile = (W_pl_vector_IPE[3]*9.81/1000)
elif profile_choice == "HEA":
    g_k_profile = (W_pl_vector_HEA[3]*9.81/1000)
elif profile_choice == "HEB":
    g_k_profile = (W_pl_vector_HEB[3]*9.81/1000)

gd = 1.35 * (g_k_roof+g_k_profile)
factor = gd/sd                      # this factor will make following calculations more simple
print(gd)
print(factor)

# ... now I copied everything to the main file (FrameStructure.py)... otherwise I can not use the internal forces













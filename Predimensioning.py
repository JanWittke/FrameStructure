# Import old data here just example values

Truss_MQN = [388.24, 131.2, -77.65]
Pillar_MQN = [388.24, 93.72, -131.2]

# Import Profile list for the truss (HEA)

import pandas
HEA = []
HEA = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEA-profiles.xlsx")
#print(HEA)

num_rows = HEA.shape[0]
num_rows = int(num_rows)

W_pl_vector = []
M_Ed = Truss_MQN[0]*1.2 #Increase of 20% for later reserves


for i in range(num_rows):
    S_x = HEA.iat[i, 16]#
    W_pl = float(2*S_x)
    row_number = HEA.iat[i, 0]
    profile = HEA.iat[i, 1]
    W_pl_vector = [row_number,profile,W_pl]

    M_cRD = (W_pl) * 23.5 / 100
    eta = M_Ed/M_cRD
    Eta = round(eta, 2)  # Round to two decimal

    if Eta <= 1:
        break

print(Eta)
print(W_pl_vector)



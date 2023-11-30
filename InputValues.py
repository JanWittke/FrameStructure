#This is a tool for a predimensioning and preselection of a steel frame!
#First we have to enter the variabels

import math
import sys

system = 1 #No other variants for static systems are available yet

while True:
    V = input("Enter the needed Height, Wide and Length of your hall in [m]: (H,W,L) ")

    V_einzeln = V.split(',')

    H = V_einzeln[0]
    W = V_einzeln[1]
    L_total = V_einzeln[2]

    H = float(H)
    W = float(W)
    L_total = float(L_total)
    # Check your conditions for valid input
    if H >= 3 and H <= 20 and W >= 6 and W <= 30 and L_total >= 15 and L_total <= 200:
        break

    else:
        print("The Height should be between 3 and 20 [m].")
        print("The Wide should be between 6 and 30 [m].")
        print("The Length should be between 15 and 200 [m].")


while True:
    Load = input(
        "Enter now the dead load for the roof g_k, the snow load s_k and the wind load w_k in [kN/m2]: (g_k,s_k,w_k) ")
    Load_split = Load.split(',')

    gk = Load_split[0]
    sk = Load_split[1]
    wk = Load_split[2]

    gk = float(gk)
    sk = float(sk)
    wk = float(wk)
    if gk >= 0 and sk > 0 and wk >= 0:
        break
    if sk == 0:
        print("Its necessary to enter a snow load.")
    if gk < 0 or sk < 0 or wk < 0:
        print("Please enter only positive loads.")


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


print("The hall is divided into",X,"sections with a distance (L_section) of",L_section,"[m].")
print("In total we have",X+1,"frames.")



#"s_d =",sd,"[kN/m] and for the wind load of w_d =",wd,"[kN/m].")

while True:
    sd = sk * 1.5 * L_section  # kN/m
    wd = wk * 1.5 * L_section  # kN/m
    gk_roof = gk * L_section  # kN/m
    gd_roof = gk_roof * 1.35

    gd_roof = gd_roof.__round__(2)
    sd = sd.__round__(2)
    wd = wd.__round__(2)

    print("This results in design line loads:")
    print("g_d =", gd_roof, "[kN/m]")
    print("s_d =", sd, "[kN/m]")
    print("w_d =", wd, "[kN/m]")

    print("Are you satisfied with this values?")
    print("If no, then enter a new maximum length for a section in [m]: (L_section) ")
    print("If yes, then press enter and start calculations.")

    L_section_new = input()


    if not L_section_new:
        break
    else:
        try:
            L_section_new = float(L_section_new)
            if L_section_new > 0:
                L_section = L_section_new
                # restart
            if L_section_new < 0:
                print("Negative entry not possible. The previous value remains the same.")
                break

        except ValueError:
            print("Incorrect entry. The previous value remains the same.")
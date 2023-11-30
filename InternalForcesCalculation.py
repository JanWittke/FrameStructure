#Calculation of the internal forces on a three hinged frame
#Snowload =======================================================================================================
# M = moment
# Q = shear force (Querkraft)
# N = axial force (Normalkraft)

import InputValues

H = InputValues.H
W = InputValues.W

#gd_roof = InputValues.gd_roof
sd = InputValues.sd
wd = InputValues.wd

#sd = 1  #Value is 1 but is later increased by a factor
#wd = 1  #Value is 1 but is later increased by a factor

Ma_sd = 0
Mb_sd = - sd * (W**2)/8
Mc_sd = Mb_sd
Md_sd = 0
Me_sd = Mb_sd
Mf_sd = Me_sd
Mg_sd = 0
Moment_P_sd = [Ma_sd,Mb_sd,Mc_sd,Md_sd,Me_sd,Mf_sd,Mg_sd] #P = point
round_Moment_P_sd = [round(num, 2) for num in Moment_P_sd]

#print("M_sd: a,b,c,d,e,f,g :",round_Moment_P_sd,)

Qa_sd = Mb_sd/H
Qb_sd = Qa_sd
Qc_sd = sd * W/2
Qd_sd = 0
Qe_sd = - Qc_sd
Qf_sd = -Qa_sd
Qg_sd = Qf_sd
Shear_force_P_sd = [Qa_sd,Qb_sd,Qc_sd,Qd_sd,Qe_sd,Qf_sd,Qg_sd]
round_Shear_force_P_sd = [round(num, 2) for num in Shear_force_P_sd]

#print("Q_sd: a,b,c,d,e,f,g :",round_Shear_force_P_sd,)

Av_sd = sd * W/2
Gv_sd = Av_sd

Na_sd = - Av_sd
Nb_sd = Na_sd
Nc_sd = Qa_sd
Nd_sd = Nc_sd
Ne_sd = Nc_sd
Nf_sd = Na_sd
Ng_sd = Nf_sd

Normal_force_P_sd = [Na_sd,Nb_sd,Nc_sd,Nd_sd,Ne_sd,Nf_sd,Ng_sd]
round_Normal_force_P_sd = [round(num, 2) for num in Normal_force_P_sd]

#print("N_sd: a,b,c,d,e,f,g :",round_Normal_force_P_sd,)

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

#print("M_wd: a,b,c,d,e,f,g :",round_Moment_P_wd,)

Qa_wd = -Qg_wd + wd*H
Qb_wd = -Qg_wd
Qc_wd = N4_wd
Qd_wd = N4_wd
Qe_wd = N4_wd
Qf_wd = Qg_wd
Qg_wd = Qg_wd
Shear_force_P_wd = [Qa_wd,Qb_wd,Qc_wd,Qd_wd,Qe_wd,Qf_wd,Qg_wd]
round_Shear_force_P_wd = [round(num, 2) for num in Shear_force_P_wd]

#print("Q_wd: a,b,c,d,e,f,g :",round_Shear_force_P_wd,)

Na_wd = -Av_wd
Nb_wd = Na_wd
Nc_wd = -Qf_wd
Nd_wd = Nc_wd
Ne_wd = Nc_wd
Nf_wd = - Gv_wd
Ng_wd = Nf_wd

Normal_force_P_wd = [Na_wd,Nb_wd,Nc_wd,Nd_wd,Ne_wd,Nf_wd,Ng_wd]
round_Normal_force_P_wd = [round(num, 2) for num in Normal_force_P_wd]

#print("N_wd: a,b,c,d,e,f,g :",round_Normal_force_P_wd,)

round_Moment_P_gd_roof = round_Moment_P_sd
round_Shear_force_P_gd_roof = round_Shear_force_P_sd
round_Normal_force_P_gd_roof = round_Normal_force_P_sd


import ctypes
from array import array
import numpy as np
import ROOT
from ROOT import TH1F, TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend, TH1D
#import CMS_lumi, tdrstyle
#import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
import sys

#for i in range(10):
binss = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 3500, 4000]
def createCard(i):
    print(i)    
    infile = TFile.Open("../template_bin"+str(i+1)+".root")
    mu_data = infile.Get("mu_data_obs")

    el_data = infile.Get("el_data_obs")

    infile_mu_dy = TFile.Open("template_bin"+str(i+1)+".root")
    infile_el_dy = TFile.Open("template_bin"+str(i+1)+".root")

    mu_S = infile_mu_dy.Get("mu_S")
    el_S = infile_el_dy.Get("el_S")
    #err_mu= ctypes.c_double(0)
    #n_mu=mu_data.IntegralAndError(0, -1, err_mu)

    nel_dy = el_S.Integral()

    print("hello", nel_dy)
    n_mu = mu_S.Integral()

    #err_el= ctypes.c_double(0)
    n_el = el_S.Integral()

    #n_el=el_data.IntegralAndError(0, -1, err_el)

    
    #print(n_mu, n_el)
    if(n_el ==0.0):
      n_el = 0.00125
    acc_eff = n_mu/n_el

    #err=acc_eff*np.sqrt((err_mu/n_mu)**2+(err_el/n_el)**2)
    mu_B = infile_mu_dy.Get("mu_B")

    el_B = infile_el_dy.Get("el_B")

    input_mu = []
    input_el = []



    input_mu = mu_data.Integral()
    input_el = el_data.Integral()

    input_mu_b = []
    input_el_b = []

    input_mu_b.append(mu_B.Integral())
    input_el_b.append(el_B.Integral()) 
    #print(input_mu_top)

    N = mu_data.GetNbinsX()
#
#    def createCard():
#        datacard_start = ["##################",
#                       "jmax 2 number of bins",
#                       "jmax 5 number of processes minus 1",
#                       "kmax * number of nuisance parameters",
#    
#    
#                        "-------------------------------------------------------------------------------",
#                        "shapes *          control template.root   e1_$PROCESS",
#                        "shapes e1_DY      control template.root   $PROCESS   $PROCESS$SYSTEMATIC",
#                        "shapes e1_Top     control template.root   $PROCESS   $PROCESS$SYSTEMATIC",
#                        "shapes e1_Diboson control template.root   $PROCESS   $PROCESS$SYSTEMATIC",
#                        "shapes *          signal  template.root   mu_$PROCESS",
#                        "shapes mu_DY      signal  template.root   $PROCESS   $PROCESS$SYSTEMATIC",   
#                        "shapes mu_Top     signal  template.root   $PROCESS   $PROCESS$SYSTEMATIC",
#                        "shapes mu_Diboson signal  template.root   $PROCESS   $PROCESS$SYSTEMATIC",
#    
#                        "-------------------------------------------------------------------------------",
#                        "bin          signal         control",
#                        ]
#        datacard_sec =  ["bin         signal      signal     signal       control   control    control",
#                         "process     mu_DYJets   mu_Top     mu_Diboson   e1_DY     e1_Top     e1_Diboson",
#                         "process     0           1          2            1         2          3",
#                        ]
#        datacard_sys =  ["-------------------------------------------------------------------------------",
#                         "_btagUp   shape  1.0        1.0      1.0          -         -           -",
#                         "_btagDown shape  1.0        1.0      1.0          -         -           -",
#                         "_btagUp   shape  1.0        1.0      1.0          -         -           -",
#                         "_btagDown shape  1.0        1.0      1.0          -         -           -",
#                       ]
    
    
    
#        for i in range(N):
    
    
#    datacard = open("card"+"_bin"+str(i+1)+".txt", 'w')
#    for lines in datacard_start:
#        datacard.write(lines+"\n")
#    datacard.write("observation  {:<14.5f} {:<14.5f}\n".format(input_mu, input_el))
#    datacard.write("------------------------------------------------------------------------------- \n")
#    for lines in datacard_sec:
#        datacard.write(lines+"\n")
#    datacard.write("rate          {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f}\n".format(1, input_mu_top[0], input_mu_diboson[0], 1, input_el_top[0], input_el_diboson[0]))   
#    datacard.write("------------------------------------------------------------------------------- \n")
#    
#    datacard.write("R2018bb     rateParam    signal    mu_DYJets   {:<14.10f}\n".format(acc_eff))
#    #    for lines in datacard_sys:
#    #        datacard.write(lines+"\n")
#    
#    
#    datacard.close()    

#def createCard():
    datacard_start = ["##################",
                   "jmax 2 number of bins",
                   "jmax 3 number of processes minus 1",
                   "kmax * number of nuisance parameters",


                    "-------------------------------------------------------------------------------",
                    "shapes *          control template_bin9.root      el_$PROCESS",
                    "shapes el_S       control template_bin9.root      $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes el_B       control template_bin9.root      $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes *          signal  template_bin9.root      mu_$PROCESS",
                    "shapes mu_S       signal  template_bin9.root      $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes mu_B       signal  template_bin9.root      $PROCESS   $PROCESS$SYSTEMATIC",

                    "-------------------------------------------------------------------------------",
                    "bin          signal         control",
                    ]
    datacard_sec =  ["bin           signal         signal         control        control",
                     "process       mu_S           mu_B           el_S           el_B   ",
                     "process       0              1              1              2      ",
                    ]
    datacard_sys =  ["-------------------------------------------------------------------------------",
                     "_btagUp   shape  1.0        1.0      1.0          -         -           -",
                     "_btagDown shape  1.0        1.0      1.0          -         -           -",
                     "_btagUp   shape  1.0        1.0      1.0          -         -           -",
                     "_btagDown shape  1.0        1.0      1.0          -         -           -",
                   ]
    val = i+1
    print(val)
    datacard = open("card"+"_bin"+str(val)+".txt", 'w')
    for lines in datacard_start:
        datacard.write(lines+"\n")
    datacard.write("observation  {:<14.5f} {:<14.5f}\n".format(input_mu, input_el))
    datacard.write("------------------------------------------------------------------------------- \n")
    for lines in datacard_sec:
        datacard.write(lines+"\n")
    datacard.write("rate          {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f}\n".format(1, input_mu_b[0], 1, input_el_b[0]))
    datacard.write("------------------------------------------------------------------------------- \n")

    datacard.write("R2018bb     rateParam    signal    mu_S       {:<14.10f}\n".format(acc_eff))
    datacard.write("Rmu2018bb   rateParam    signal    mu_S       (@0) Rel2018bb\n"             )
    datacard.write("Rel2018bb   rateParam    control   el_S       {:<14.10f}\n".format(nel_dy))
    
    datacard.write("------------------------------------------------------------------------------- \n")
    datacard.write("signal              autoMCStats 0 0 1 \n")
    datacard.write("control             autoMCStats 0 0 1 \n")


    #    for lines in datacard_sys:
    #        datacard.write(lines+"\n")


    datacard.close()

    
def main():
    createCard(8) 

if __name__ == '__main__':
    main()

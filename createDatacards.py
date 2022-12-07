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
binss = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 3500, 6000]
def createCard(i):
    print(i)    
    infile = TFile.Open("template_bin"+str(i+1)+".root")
    mu_data = infile.Get("mu_data_obs")

    el_data = infile.Get("el_data_obs")

    infile_mu_dy = TFile.Open("mu/1b_inclusive_2018.root")
    infile_el_dy = TFile.Open("el/1b_inclusive_2018.root")

    mu_dy = infile_mu_dy.Get("DYJets")
    el_dy = infile_el_dy.Get("DY")
    #err_mu= ctypes.c_double(0)
    #n_mu=mu_data.IntegralAndError(0, -1, err_mu)
    binx = el_dy.GetXaxis().FindBin(i)
    binsxx = el_dy.GetXaxis().FindBin(i+1)  

    nel_dy = el_dy.Integral(binx, binsxx)

    print("hello", nel_dy)
    n_mu=mu_dy.Integral()

    #err_el= ctypes.c_double(0)
    n_el=el_dy.Integral()

    #n_el=el_data.IntegralAndError(0, -1, err_el)

    
    #print(n_mu, n_el)
    if(n_el ==0.0):
      n_el = 0.00125
    acc_eff = n_mu/n_el

    #err=acc_eff*np.sqrt((err_mu/n_mu)**2+(err_el/n_el)**2)
    mu_DYJets = infile.Get("mu_DYJets")
    mu_Top = infile.Get("mu_Top")
    mu_Diboson = infile.Get("mu_Diboson")

    el_DY = infile.Get("el_DY")
    el_Top = infile.Get("el_Top")
    el_Diboson = infile.Get("el_Diboson")

    input_mu = []
    input_el = []

    input_mu_dy = []
    input_mu_top = []
    input_mu_diboson = []

    input_el_dy = []
    input_el_top = []
    input_el_diboson = []

    input_mu = mu_data.Integral()
    input_el = el_data.Integral()

    for j in range(mu_data.GetNbinsX()):
        #input_mu.append(mu_data.GetBinContent(i+1))
        #input_el.append(el_data.GetBinContent(i+1))
 
        input_mu_dy.append(mu_DYJets.GetBinContent(j+1))
        input_mu_top.append(mu_Top.GetBinContent(j+1))
        input_mu_diboson.append(mu_Diboson.GetBinContent(j+1))
    
        input_el_dy.append(el_DY.GetBinContent(j+1))
        input_el_top.append(el_Top.GetBinContent(j+1))
        input_el_diboson.append(el_Diboson.GetBinContent(j+1))

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
    
    print(i, input_mu_top[0])
    
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
                   "jmax 5 number of processes minus 1",
                   "kmax * number of nuisance parameters",


                    "-------------------------------------------------------------------------------",
                    "shapes *          control template_bin9.root   el_$PROCESS",
                    "shapes el_DY      control template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes el_Top     control template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes el_Diboson control template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes *          signal  template_bin9.root   mu_$PROCESS",
                    "shapes mu_DYJets  signal  template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes mu_Top     signal  template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",
                    "shapes mu_Diboson signal  template_bin9.root   $PROCESS   $PROCESS$SYSTEMATIC",

                    "-------------------------------------------------------------------------------",
                    "bin          signal         control",
                    ]
    datacard_sec =  ["bin         signal      signal     signal       control   control    control",
                     "process     mu_DYJets   mu_Top     mu_Diboson   el_DY     el_Top     el_Diboson",
                     "process     0           1          2            1         2          3",
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
    datacard.write("rate          {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f} {:<14.10f}\n".format(1, input_mu_top[0], input_mu_diboson[0], 1, input_el_top[0], input_el_diboson[0]))
    datacard.write("------------------------------------------------------------------------------- \n")

    datacard.write("R2018bb     rateParam    signal    mu_DYJets   {:<14.10f}\n".format(acc_eff))
    datacard.write("Rmu2018bb   rateParam    signal    mu_DYJets   (@0) Rel2018bb\n"             )
    datacard.write("Rel2018bb   rateParam    control   el_DY       {:<14.10f}\n".format(nel_dy))
    #    for lines in datacard_sys:
    #        datacard.write(lines+"\n")


    datacard.close()

    
def main():
    createCard(8) 

if __name__ == '__main__':
    main()

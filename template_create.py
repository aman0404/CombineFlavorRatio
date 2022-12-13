from array import array
import numpy as np
import ROOT
from ROOT import TH1F, TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend, TH1D
#import CMS_lumi, tdrstyle
#import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
import sys

print("getting the root files now")


filemu_s = TFile("1b_inclusive_2018_mu_a400.root")

fileel_s = TFile("1b_inclusive_2018_el_a400.root")

filemu_b = TFile("1b_inclusive_2018_mu_b400.root")

fileel_b = TFile("1b_inclusive_2018_el_b400.root")

filemu_data = TFile("../mu/1b_inclusive_2018.root")
fileel_data = TFile("../el/1b_inclusive_2018.root")

bins = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 4000]

binss = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 3500, 6000]
muhist_s = {"mu_S" :[]}
elhist_s = {"mu_S" :[]}

muhist_b = {"mu_B" :[]}
elhist_b = {"mu_B" :[]}

mu_data = {"data_obs" :[]}
el_data = {"data_obs" :[]}

#musys   = {"Top": [], "Diboson":[], "data_obs": [], "DYJets_btagUp" :[], "Top_btagUp": [], "Diboson_btagUp" :[], "DYJets_btagDown" :[], "Top_btagDown": [], "Diboson_btagDown" :[]}
#elsys   = {"Top": [], "Diboson":[], "data_obs": [], "DY_btagUp" :[], "Top_btagUp": [], "Diboson_btagUp" :[], "DY_btagDown" :[], "Top_btagDown": [], "Diboson_btagDown" :[]}

for key, value_mu_data in mu_data.items():
    hmu_data = filemu_data.Get(key)
    for i in range(len(bins)-1):
        binx_ = hmu_data.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = hmu_data.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_

        value_mu_data.append((hmu_data.Integral(binx_, binx1_))/bin_width_)

for key, value_el_data in el_data.items():
    hel_data = fileel_data.Get(key)
    for i in range(len(bins)-1):
        binx_ = hel_data.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = hel_data.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_

        value_el_data.append((hel_data.Integral(binx_, binx1_))/bin_width_)




for key, values in muhist_s.items():
    h = filemu_s.Get(key)
    for i in range(len(bins)-1):
        binx_ = h.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_ 

        values.append((h.Integral(binx_, binx1_))/bin_width_)


for key, values_b in muhist_b.items():
    h_b = filemu_b.Get(key)
    for i in range(len(bins)-1):
        binx_ = h.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_ 

        values_b.append((h_b.Integral(binx_, binx1_))/bin_width_)

for key, el_values in elhist_s.items():
    elh = fileel_s.Get(key)
    for i in range(len(bins)-1):
        binx_ = h.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_

        el_values.append((elh.Integral(binx_, binx1_))/bin_width_)

for key, el_values_b in elhist_b.items():
    elh_b = fileel_b.Get(key)
    for i in range(len(bins)-1):
        binx_ = h.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h.GetXaxis().FindBin(bins[i+1])

        bin_width_ = binx1_-binx_

        el_values_b.append((elh_b.Integral(binx_, binx1_))/bin_width_)

for i in range(len(bins)-1):
    myfile = TFile( 'template_bin'+str(i+1)+'.root', 'RECREATE' )

    for keys, yields in muhist_s.items():
        print(i)
        histname = TH1F(str(keys), "hist", 1, bins[i], bins[i+1])
        histname.SetBinContent(1, yields[i]) 
        histname.Scale(1/histname.Integral())
        histname.Draw()
        histname.Write()

    for keys, yields in muhist_b.items():
        histname2 = TH1F(str(keys), "hist", 1, bins[i], bins[i+1])
        histname2.SetBinContent(1, yields[i])

        #histname.Scale(1/histname.Integral())
        histname2.Draw()
        histname2.Write()

    for keys, yields in elhist_s.items():
        histname3 = TH1F("el_S", "hist", 1, bins[i], bins[i+1])
        histname3.SetBinContent(1, yields[i])

        histname3.Scale(1/histname3.Integral())
        histname3.Draw()
        histname3.Write()

    for keys, yields in elhist_b.items():
        histname4 = TH1F("el_B", "hist", 1, bins[i], bins[i+1])
        histname4.SetBinContent(1, yields[i])

        #histname4.Scale(1/histname.Integral())
        histname4.Draw()
        histname4.Write()

    for keys, yield_mu_data in mu_data.items():
        histname5 = TH1F("mu_data_obs", "hist", 1, bins[i], bins[i+1])
        histname5.SetBinContent(1, yield_mu_data[i])

        #histname4.Scale(1/histname.Integral())
        histname5.Draw()
        histname5.Write()

    for keys, yield_el_data in el_data.items():
        histname6 = TH1F("el_data_obs", "hist", 1, bins[i], bins[i+1])
        histname6.SetBinContent(1, yield_el_data[i])

        #histname4.Scale(1/histname.Integral())
        histname6.Draw()
        histname6.Write()



    myfile.Close()

#for key, valuesys in musys.items():
#    hsys = filemu.Get(key)
#    for i in range(len(bins)):
#        binx_ = hsys.GetXaxis().FindBin(bins[i])
#        if i < len(bins)-1:
#           binx1_ = hsys.GetXaxis().FindBin(bins[i+1])
#        else:
#           binx1_ = hsys.GetXaxis().FindBin(6000)
#        bin_width_ = binx1_-binx_
#
#        valuesys.append((hsys.Integral(binx_, binx1_))/bin_width_)
#
#
#
#for key, values_el in elhists.items():
#    h_el = fileel.Get(key)
#    for i in range(len(bins)):
#        binx_ = h_el.GetXaxis().FindBin(bins[i])
#        if i < len(bins)-1:
#           binx1_ = h_el.GetXaxis().FindBin(bins[i+1])
#        else:
#           binx1_ = h_el.GetXaxis().FindBin(6000)
#        bin_width_ = binx1_-binx_
#
#        values_el.append((h_el.Integral(binx_, binx1_))/bin_width_)
#
#for key, values_el_sys in elsys.items():
#    h_sys = fileel.Get(key)
#    for i in range(len(bins)):
#        binx_ = h_sys.GetXaxis().FindBin(bins[i])
#        if i < len(bins)-1:
#           binx1_ = h_sys.GetXaxis().FindBin(bins[i+1])
#        else:
#           binx1_ = h_sys.GetXaxis().FindBin(6000)
#        bin_width_ = binx1_-binx_
#
#        values_el_sys.append((h_sys.Integral(binx_, binx1_))/bin_width_)
#
#runArray = array('d',bins + [bins[-1]+1])
#print(runArray)
#
#for i in range(len(binss)-1):
#    myfile = TFile( 'template_bin'+str(i+1)+'.root', 'RECREATE' )
#
#    for keys, yields in muhists.items():
#        if(i < len(binss)-1):
#           print(binss[i], binss[i+1])   
#           histname = TH1F("mu_"+str(keys), "hist", 1, binss[i], binss[i+1])
#        else:
#           continue
#        histname.SetBinContent(1, yields[i]) 
#    
#        histname.Scale(1/histname.Integral())
#        histname.Draw()
#        histname.Write()
#  
#
#    for keys, yields in musys.items():
#         if(i < len(binss)-1):
#            hist_sysup = TH1F("mu_"+str(keys), "hist", 1 , binss[i], binss[i+1])
#         else:
#            continue
#     
#    
#         hist_sysup.SetBinContent(1, yields[i])
#    
#         hist_sysup.Draw()
#         hist_sysup.Write()
#    
#    for keys, yields in elhists.items():
#         if(i < len(binss)-1):
#            histname_el = TH1F("el_"+str(keys), "hist", 1, binss[i], binss[i+1])
#         else:
#            continue
#         histname_el.SetBinContent(1, yields[i])
#         histname_el.Scale(1/histname_el.Integral())
#    
#    
#         histname_el.Draw()
#         histname_el.Write()
#    
#    for keys, yields in elsys.items():
#         if(i < len(binss)-1):
#            histel_sysup = TH1F("el_"+str(keys), "hist", 1, binss[i], binss[i+1])
#         else:
#            continue
#    
#         histel_sysup.SetBinContent(1, yields[i])
#    
#         histel_sysup.Draw()
#         histel_sysup.Write()
#
#
#    myfile.Close()


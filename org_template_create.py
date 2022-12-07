from array import array
import numpy as np
import ROOT
from ROOT import TH1F, TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend, TH1D
#import CMS_lumi, tdrstyle
#import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
import sys

print("getting the root files now")


filemu = TFile("mu/1b_inclusive_2018.root")

fileel = TFile("el/1b_inclusive_2018.root")

bins = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 3500]

muhists = {"DYJets" :[]}
elhists = {"DY" :[]}


musys   = {"Top": [], "Diboson":[], "data_obs": [], "DYJets_btagUp" :[], "Top_btagUp": [], "Diboson_btagUp" :[], "DYJets_btagDown" :[], "Top_btagDown": [], "Diboson_btagDown" :[]}
elsys   = {"Top": [], "Diboson":[], "data_obs": [], "DY_btagUp" :[], "Top_btagUp": [], "Diboson_btagUp" :[], "DY_btagDown" :[], "Top_btagDown": [], "Diboson_btagDown" :[]}

for key, values in muhists.items():
    h = filemu.Get(key)
    for i in range(len(bins)):
        binx_ = h.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h.GetXaxis().FindBin(bins[i+1])
        else:
           binx1_ = h.GetXaxis().FindBin(6000)
        bin_width_ = binx1_-binx_ 

        values.append((h.Integral(binx_, binx1_))/bin_width_)



for key, valuesys in musys.items():
    hsys = filemu.Get(key)
    for i in range(len(bins)):
        binx_ = hsys.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = hsys.GetXaxis().FindBin(bins[i+1])
        else:
           binx1_ = hsys.GetXaxis().FindBin(6000)
        bin_width_ = binx1_-binx_

        valuesys.append((hsys.Integral(binx_, binx1_))/bin_width_)



for key, values_el in elhists.items():
    h_el = fileel.Get(key)
    for i in range(len(bins)):
        binx_ = h_el.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h_el.GetXaxis().FindBin(bins[i+1])
        else:
           binx1_ = h_el.GetXaxis().FindBin(6000)
        bin_width_ = binx1_-binx_

        values_el.append((h_el.Integral(binx_, binx1_))/bin_width_)

for key, values_el_sys in elsys.items():
    h_sys = fileel.Get(key)
    for i in range(len(bins)):
        binx_ = h_sys.GetXaxis().FindBin(bins[i])
        if i < len(bins)-1:
           binx1_ = h_sys.GetXaxis().FindBin(bins[i+1])
        else:
           binx1_ = h_sys.GetXaxis().FindBin(6000)
        bin_width_ = binx1_-binx_

        values_el_sys.append((h_sys.Integral(binx_, binx1_))/bin_width_)

runArray = array('d',bins + [bins[-1]+1])
myfile = TFile( 'template.root', 'RECREATE' )

for keys, yields in muhists.items():
    histname = TH1F("mu_"+str(keys), "hist", len(bins), runArray)

    for i in range(len(yields)):
        histname.SetBinContent(i+1, yields[i]) 

    histname.Scale(1/histname.Integral())
    histname.Draw()
    histname.Write()

for keys, yields in musys.items():
    hist_sysup = TH1F("mu_"+str(keys), "hist", len(bins), runArray)
 
    for i in range(len(yields)):

        hist_sysup.SetBinContent(i+1, yields[i])

    hist_sysup.Draw()
    hist_sysup.Write()

for keys, yields in elhists.items():
    histname_el = TH1F("el_"+str(keys), "hist", len(bins), runArray)

    for i in range(len(yields)):
        histname_el.SetBinContent(i+1, yields[i])
    histname_el.Scale(1/histname_el.Integral())


    histname_el.Draw()
    histname_el.Write()

for keys, yields in elsys.items():
    histel_sysup = TH1F("el_"+str(keys), "hist", len(bins), runArray)

    for i in range(len(yields)):
        histel_sysup.SetBinContent(i+1, yields[i])

    histel_sysup.Draw()
    histel_sysup.Write()


myfile.Close()


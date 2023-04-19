
double acc_mu(double m) {
    double p0 = 0.114031;
    double p1 = 0.000243256;
    double p2 = -6.87957e-08;
    double p3 = 1.48064e-11;
    double p4 = -1.68326e-15;
    double val = p4*(pow(m, 4)) + p3*(pow(m, 3)) + p2*(pow(m, 2)) + p1*(m) + p0;
    return val;
}

double acc_el(double m) {
    double p0 = 0.133578;
    double p1 = 0.000247002;
    double p2 = -7.98043e-08;
    double p3 = 1.43033e-11;
    double p4 = -1.30924e-15;
    double val = p4*(pow(m, 4)) + p3*(pow(m, 3)) + p2*(pow(m, 2)) + p1*(m) + p0;
    return val;
}

void acc_double_fratio_mc_bb()
{
TCanvas *c1 = new TCanvas("c1", "stacked hists",61,24,744,744);
   c1->Range(-29.17415,-0.08108108,263.2406,0.6466216);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
//   c1->SetGridx();
//   c1->SetGridy();
   c1->SetRightMargin(0.05);
   c1->SetLeftMargin(0.14);
   c1->SetTopMargin(0.06406685);
   c1->SetBottomMargin(0.1114206);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   c1->SetLogx();
//   c1->SetLogy();

TH1 *unfolded_mu_dy , *unfolded_el_dy;
TH1 *unfolded_mu_data , *unfolded_el_data;

TFile *f1 = TFile::Open("unfolded_mc_muon_bb.root");
f1->GetObject("o", unfolded_mu_dy);

TFile *f2 = TFile::Open("unfolded_mc_elec_bb.root");
f2->GetObject("o", unfolded_el_dy);

TFile *f3 = TFile::Open("unfolded_mc_muon_bb_data.root");
f3->GetObject("o", unfolded_mu_data);

TFile *f4 = TFile::Open("unfolded_mc_elec_bb_data.root");
f4->GetObject("o", unfolded_el_data);



        TH1F *hdiv1 = (TH1F*)unfolded_mu_data->Clone("hdiv1"); //data-bkg
        TH1F *hdiv2 = (TH1F*)unfolded_el_data->Clone("hdiv2");  //data-bkg
        TH1F *hdiv3 = (TH1F*)unfolded_mu_dy->Clone("hdiv3");  //dy
        TH1F *hdiv4 = (TH1F*)unfolded_el_dy->Clone("hdiv4");  //dy

for(int i=1; i<=5; i++)
{
std::cout<<hdiv1->GetBinCenter(i)<<'\t'<<hdiv1->GetBinContent(i)<<std::endl;
std::cout<<hdiv2->GetBinCenter(i)<<'\t'<<hdiv2->GetBinContent(i)<<std::endl;
}

for(int i=1; i <= unfolded_mu_dy->GetNbinsX(); i++)
{
double bin = unfolded_mu_dy->GetBinCenter(i);
hdiv1->SetBinContent(i, hdiv1->GetBinContent(i)/acc_mu(bin));
hdiv1->SetBinError(i, hdiv1->GetBinError(i)/hdiv1->GetBinContent(i));

hdiv2->SetBinContent(i, hdiv2->GetBinContent(i)/acc_el(bin));
hdiv2->SetBinError(i, hdiv2->GetBinError(i)/hdiv2->GetBinContent(i));

hdiv3->SetBinContent(i, hdiv3->GetBinContent(i)/acc_mu(bin));
hdiv3->SetBinError(i, hdiv3->GetBinError(i)/hdiv3->GetBinContent(i));

hdiv4->SetBinContent(i, hdiv4->GetBinContent(i)/acc_el(bin));
hdiv4->SetBinError(i, hdiv4->GetBinError(i)/hdiv4->GetBinContent(i));
}

std::cout<<"After changing "<<std::endl;
for(int i=1; i<=5; i++)
{
std::cout<<hdiv1->GetBinCenter(i)<<'\t'<<hdiv1->GetBinContent(i)<<std::endl;
std::cout<<hdiv2->GetBinCenter(i)<<'\t'<<hdiv2->GetBinContent(i)<<std::endl;
}

hdiv1->Divide(hdiv2);
hdiv3->Divide(hdiv4);

TH1F *hscale = (TH1F*)unfolded_mu_dy->Clone("hscale");

for(int i=1; i <= hscale->GetNbinsX(); i++)
{
hscale->SetBinContent(i,0);
hscale->SetBinError(i,0);
hscale->SetBinContent(i, 1.16778);
hscale->SetBinError(i, 1.84399e-08);
}

TH1F *hscale_mc = (TH1F*)unfolded_mu_dy->Clone("hscale_mc");

for(int i=1; i <= hscale_mc->GetNbinsX(); i++)
{
hscale_mc->SetBinContent(i,0);
hscale_mc->SetBinError(i,0);
hscale_mc->SetBinContent(i, 1.09807);
hscale_mc->SetBinError(i, 7.12149e-09 );
}

hdiv1->Divide(hscale);
hdiv3->Divide(hscale_mc);

hdiv1->Divide(hdiv3);  //double ratio
hdiv1->Draw("lep");
hdiv1->SetStats(kFALSE);
hdiv1->SetTitle("");
hdiv1->SetMarkerStyle(20);
hdiv3->SetMarkerStyle(20);
hdiv1->SetMarkerColor(kBlack);
hdiv3->SetMarkerColor(kBlue);
hdiv1->SetMarkerSize(1.2);
hdiv3->SetMarkerSize(1.2);

   hdiv1->GetYaxis()->SetLabelFont(42);
   hdiv1->GetYaxis()->SetNdivisions(20505);
   hdiv1->GetYaxis()->SetLabelSize(0.04);
   hdiv1->GetYaxis()->SetTitleSize(0.04);
   hdiv1->GetYaxis()->SetTitleOffset(1.3);
   hdiv1->GetYaxis()->SetTitleFont(42);
   hdiv1->SetLineColor(kBlue+2);
   hdiv1->SetLineWidth(1);
   hdiv3->SetLineWidth(0);
   hdiv1->GetYaxis()->SetRangeUser(0,2.5);
   hdiv1->GetXaxis()->SetTitle("m  [GeV]");
   hdiv1->GetYaxis()->SetTitle("R^{Data}_{#mu#mu/ee}/R^{MC}_{#mu#mu/ee}");

   hdiv1->GetXaxis()->SetLabelFont(42);
   hdiv1->GetXaxis()->SetLabelOffset(0.02);
   hdiv1->GetXaxis()->SetTitleSize(0.04);
   hdiv1->GetXaxis()->SetTitleOffset(1.1);
      hdiv1->GetXaxis()->SetLabelSize(0.04);

   hdiv1->GetXaxis()->SetRangeUser(200,3490);
//line
   TLine *line = new TLine(200, 1,3500, 1);
   line->SetLineColor(kRed);
   line->Draw();


        double y_legend = hdiv1->GetMaximum() + 0.01;
        double x_legend = 250;
        TLatex *   tex = new TLatex(x_legend,y_legend,"CMS");
//      TLatex *   tex = new TLatex(105,400,"CMS");
     tex->SetTextAlign(20);
   tex->SetTextSize(0.05);
   tex->SetLineWidth(2);
        tex->Draw();
        TLatex *   tex1 = new TLatex(x_legend+120,y_legend,"#it{#bf{Preliminary}}");
   tex1->SetTextAlign(20);
   tex1->SetTextSize(0.03);

   tex1->SetLineWidth(2);
   tex1->Draw();

        TLegend *legend = new TLegend(0.37,0.750899,0.94,0.8843167,NULL,"brNDC");

        legend->SetHeader("BB category");
        legend->SetTextSize(0.03);
        legend->AddEntry(hdiv1,"flavor ratio","lep");


        legend->Draw();

c1->SaveAs("plots/double_acc_corr_fratio_bb_mc.png");
c1->SaveAs("plots/double_acc_corr_fratio_bb_mc.pdf");
c1->SaveAs("plots/double_acc_corr_fratio_bb_mc.root");
}

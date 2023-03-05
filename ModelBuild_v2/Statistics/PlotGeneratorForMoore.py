import ROOT

def PlotGenerator(data,normalization,legend_default,layer_default,variable_name,path_filename,lower,upper,title,nDivision):
    
    canvas=ROOT.TCanvas()
    canvas.SetRightMargin(0.09)
    canvas.SetLeftMargin(0.09)
    canvas.SetBottomMargin(0.15)
    
    if legend_default==True:
    
        legend=ROOT.TLegend(0.6,0.8,0.89,0.89)
    
    else:
        legend=ROOT.TLegend(0.45,0.8,0.1,0.89)
        

    text=ROOT.TPaveText(0.7,0.2,0.89,0.30, "NDC")

    downPlot = ROOT.TH1D('','',100,lower,upper)
    ghostPlot = ROOT.TH1D('','',100,lower,upper)
    for index,row in data.iterrows():
        downPlot.Fill(row[variable_name],row['Downstream']==True)
        ghostPlot.Fill(row[variable_name],row['Downstream']==False)



    downPlot.SetStats(0)
    ghostPlot.SetStats(0)
    
    
    ghostPlot.GetXaxis().SetTitle(title)
    ghostPlot.GetXaxis().CenterTitle()
    ghostPlot.GetXaxis().SetTitleOffset(1.3)
    ghostPlot.GetXaxis().SetTitleSize(0.05)
    ghostPlot.GetXaxis().SetNdivisions(nDivision)
    
    downPlot.GetXaxis().SetTitle(title)
    downPlot.GetXaxis().CenterTitle()
    downPlot.GetXaxis().SetTitleOffset(1.3)
    downPlot.GetXaxis().SetTitleSize(0.05)
    downPlot.GetXaxis().SetNdivisions(nDivision)

    if (layer_default==True)&(normalization==True):
        
        downPlot.SetFillColorAlpha(46,0.5)
        downPlot.SetFillStyle(4050)
        downPlot.DrawNormalized('HIST')


        ghostPlot.SetFillColorAlpha(9,0.5)
        ghostPlot.SetFillStyle(4050)
        ghostPlot.DrawNormalized('HIST SAME')
        
    elif (layer_default==True)&(normalization==False):
        
        downPlot.SetFillColorAlpha(46,0.5)
        downPlot.SetFillStyle(4050)
        downPlot.Draw('HIST')


        ghostPlot.SetFillColorAlpha(9,0.5)
        ghostPlot.SetFillStyle(4050)
        ghostPlot.Draw('HIST SAME')
        
    elif (layer_default==False)&(normalization==True):
        
        ghostPlot.SetFillColorAlpha(9,0.5)
        ghostPlot.SetFillStyle(4050)
        ghostPlot.DrawNormalized('HIST')
        
        
        downPlot.SetFillColorAlpha(46,0.5)
        downPlot.SetFillStyle(4050)
        downPlot.DrawNormalized('HIST SAME')
        
        
        
    elif (layer_default==False)&(normalization==False):
        
        

        ghostPlot.SetFillColorAlpha(9,0.5)
        ghostPlot.SetFillStyle(4050)
        ghostPlot.Draw('HIST')
        
        
        downPlot.SetFillColorAlpha(46,0.5)
        downPlot.SetFillStyle(4050)
        downPlot.Draw('HIST SAME')
        
        
    





    text.AddText('LHCb Simulation')
    text.SetBorderSize(1)


    legend.AddEntry(ghostPlot,'Ghost Tracks','f')
    legend.AddEntry(downPlot,'True Tracks','f')


    

    
    legend.Draw()
    text.Draw()
    canvas.Draw()

    return canvas.SaveAs(f"./Plots/{path_filename}.png")


def plot_fun(data_tree,v,condition='seed_p<100e3'):
    
    data_tree.SetLineColor(1)
    data_tree.Draw(v,'seed_p<100e3')
    
    
    data_tree.SetLineColor(4)
    data_tree.Draw(v,condition+'&'+'Downstream==0','SAME')

    data_tree.SetLineColor(2)
    data_tree.Draw(v,condition+'&'+'Downstream==1','SAME')


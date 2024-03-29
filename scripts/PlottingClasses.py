#!/usr/bin/env python
import sys,os
#sys.argv.append('-b')
from ROOT import *
from collections import defaultdict
import numpy as np

#color dictionary
colorDict = {'DYJets':kGreen+1,'ZGToLLG':kBlue,'DYToMuMu':kOrange,'DYToEE':kOrange,'DYJetsS10':kGreen+1}
colorList = [kBlack,kRed,kBlue,kGreen+1,kMagenta+1,kOrange,kYellow+2,kMagenta+3,kGreen-1,kCyan,kGray]

# class for multi-layered nested dictionaries, pretty cool
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

class Plotter:
  """Class to handle most standard plotting needs"""
  def __init__(self, thisFile, inFolder, outFolder, year, lepton, signal):
    self.thisFile = thisFile
    self.folder = inFolder
    self.directory = outFolder
    self.year = year
    self.lepton = lepton
    self.sigName = signal
    self.FolderDump()
    self.doProj = False
    self.can = None
    self.myCut = None

  def FolderDump(self):
    '''Input file and folder name, output default dictionary of histogram lists. the key name is the distribution, the lists are all the samples for the given distribution'''
    if type(self.thisFile) != list:
      folderDict = defaultdict(list)
      lok = self.thisFile.GetDirectory(self.folder).GetListOfKeys()
      for i in range(0, lok.GetEntries()):
        name = lok.At(i).GetName()
        key = name.split('_')[1]
        folderDict[key].append(self.thisFile.GetDirectory(self.folder).Get(name))
      self.folderDict = folderDict
    else:
      if type(self.folder) != list: raise RuntimeError('folder must be list if files are list')
      folderDict = []
      for a,aFile in enumerate(self.thisFile):
        lok = aFile.GetDirectory(self.folder[a]).GetListOfKeys()
        folderDict.append(defaultdict(list))
        for i in range(0, lok.GetEntries()):
          name = lok.At(i).GetName()
          key = name.split('_')[1]
          folderDict[-1][key].append(aFile.GetDirectory(self.folder[a]).Get(name))
      self.folderDict = folderDict

  def LumiXSScale(self,name,fNum=None):
    print name
    '''Outputs scale for MC with respect to lumi and XS'''

    if name == 'DATA': return 1

    lumi = 0
    if self.lepton is 'mu': lumi = 19.672
    elif self.lepton is 'el': lumi = 19.711
    else: raise NameError('LumiXSScale lepton incorrect')

    scaleDict = AutoVivification()

    scaleDict['2012']['DYJets'] = 3532.8*1000
    scaleDict['2012']['DYJetsS10'] = 3532.8*1000
    scaleDict['2012']['DYToMuMu'] = 1966.7*1000
    scaleDict['2012']['DYToEE'] = 1966.7*1000
    scaleDict['2012']['ZGToLLG'] = 156.2*1000
    scaleDict['2012']['gg']['123'] = 20.15*0.00136*0.10098*1000
    scaleDict['2012']['gg']['125'] = 19.52*0.00154*0.10098*1000
    scaleDict['2012']['gg']['135'] = 16.79*0.00227*0.10098*1000
    scaleDict['2012']['gg']['200'] = 5.356*0.000175*0.10098*1000
    scaleDict['2012']['gg']['500'] = 1.283*0.00000759*0.10098*1000

    if type(self.thisFile) != list:
      initEvents = self.thisFile.GetDirectory('Misc').Get('h1_acceptanceByCut_'+name).Integral(1,1)
    else:
      initEvents = self.thisFile[fNum].GetDirectory('Misc').Get('h1_acceptanceByCut_'+name).Integral(1,1)

    if 'Signal' in name:
      sig = name[10:].partition('M')[0]
      mass = name[10:].partition('M')[-1][0:3]
      scale = initEvents/scaleDict[self.year][sig][mass]
    else:
      scale = initEvents/scaleDict[self.year][name]
    scale = lumi/scale
    return scale

  def ChooseTwoHists(self,chooseNames,histList, histList2 = None, norm = False):
    outList = []
    for hist in histList: print hist.GetName()
    if chooseNames[0].lower() == 'bg' or chooseNames[0].lower() == 'background':
      bgList = self.GetBGHists(histList)
      bgHist = bgList[0].Clone()
      bgHist.Reset()
      for hist in bgList:
        label = hist.GetName().split('_')[-1]
        scale = self.LumiXSScale(label)
        hist.Scale(scale)
        bgHist.Add(hist)
      outList.append(bgHist)
    else:
      for hist in histList:
        if chooseNames[0] in hist.GetName():
          outList.append(hist.Clone())
          label = outList[-1].GetName().split('_')[-1]
          print label
          scale = self.LumiXSScale(label)
          outList[-1].Scale(scale)
          break

    if histList2 == None: histList2 = histList
    if chooseNames[1].lower() == 'bg' or chooseNames[1].lower() == 'background':
      bgList = self.GetBGHists(histList2)
      bgHist = bgList[0].Clone()
      bgHist.Reset()
      for hist in bgList:
        label = hist.GetName().split('_')[-1]
        scale = self.LumiXSScale(label)
        hist.Scale(scale)
        bgHist.Add(hist)
      outList.append(bgHist)
    else:
      for hist in histList2:
        if chooseNames[1] in hist.GetName():
          outList.append(hist.Clone())
          label = outList[-1].GetName().split('_')[-1]
          scale = self.LumiXSScale(label)
          outList[-1].Scale(scale)
          break

    if len(outList) != 2:
      outList = None
      return outList

    if norm:
      outList[0].Scale(1/outList[0].Integral(0,outList[0].GetNbinsX()+1))
      outList[1].Scale(1/outList[1].Integral(0,outList[1].GetNbinsX()+1))

    ymax = max(map(lambda x:x.GetMaximum(),outList))*1.1
    ymin = 0
    outList[0].SetMaximum(ymax)
    outList[0].SetMinimum(ymin)
    if chooseNames[0] == 'DATA' and chooseNames[1] != 'DATA':
      outList[0].SetLineColor(kBlack)
    else:
      outList[0].SetLineColor(kRed)
    outList[0].SetLineWidth(2)
    outList[0].GetYaxis().SetTitleOffset(0.82)
    outList[0].GetYaxis().SetTitleSize(0.06)
    outList[0].GetYaxis().CenterTitle()
    outList[0].GetXaxis().SetTitleSize(0.05)

    if chooseNames[1] == 'DATA' and chooseNames[0] != 'DATA':
      outList[1].SetLineColor(kBlack)
    else:
      outList[1].SetLineColor(kBlue)
    outList[1].SetLineWidth(2)
    #outList[1].Scale(1/outList[1].Integral())
    return outList

  def ChooseNHists(self,chooseNames,histListN, norm = False, fNum = None ):
    outList = []
    for i, histList in enumerate(histListN):
      for hist in histList: print hist.GetName()
      if chooseNames[i].lower() == 'bg' or chooseNames[i].lower() == 'background':
        bgList = self.GetBGHists(histList)
        bgHist = bgList[0].Clone()
        bgHist.Reset()
        for hist in bgList:
          label = hist.GetName().split('_')[-1]
          scale = self.LumiXSScale(label,fNum)
          hist.Scale(scale)
          bgHist.Add(hist)
        outList.append(bgHist)
      else:
        for hist in histList:
          if chooseNames[i] in hist.GetName():
            outList.append(hist.Clone())
            break

    if len(outList) != len(histListN):
      outList = None
      return outList

    if norm:
      for hist in outList:
        hist.Scale(1/hist.Integral(0,hist.GetNbinsX()+1))

    ymax = max(map(lambda x:x.GetMaximum(),outList))*1.1
    #ymin = 0.00001
    outList[0].SetMaximum(ymax)
    #outList[0].SetMinimum(ymin)
    outList[0].SetLineColor(colorList[0])
    outList[0].SetMarkerColor(colorList[0])
    outList[0].SetLineWidth(2)
    outList[0].GetYaxis().SetTitleOffset(0.82)
    outList[0].GetYaxis().SetTitleSize(0.06)
    outList[0].GetYaxis().CenterTitle()
    outList[0].GetXaxis().SetTitleSize(0.05)

    for i,hist in enumerate(outList[1:]):
      hist.SetLineColor(colorList[i+1])
      hist.SetMarkerColor(colorList[i+1])
      hist.SetLineWidth(2)

    return outList

  def GetDataHist(self,histList,sigWindow = False):
    dataHist = None
    if self.doProj:
      for hist in histList:
        if 'DATA' in hist.GetName():
          if sigWindow: hist.GetXaxis().SetRange(hist.GetXaxis().FindBin(sigWindow-3),hist.GetXaxis().FindBin(sigWindow+3))
          dataHist = hist.Clone().ProjectionY('proj'+hist.GetName())
          break
    else:
      for hist in histList:
        if 'DATA' in hist.GetName():
          dataHist = hist.Clone()
          break
    if not dataHist: return dataHist
    dataHist.SetLineColor(kBlack)
    dataHist.SetMarkerColor(kBlack)
    dataHist.SetMarkerStyle(20)
    dataHist.SetFillStyle(0)
    return dataHist

  def GetDataHistsMD(self,histList,sigWindow = False):
    dataHistM = None
    dataHistD = None
    for hist in histList:
      if 'DATA' in hist.GetName():
        dataHistM = hist.Clone().ProjectionX('projM'+hist.GetName(),1,hist.GetNbinsY(),'[mycut]')
        dataHistD = hist.Clone().ProjectionY('projD'+hist.GetName(),1,hist.GetNbinsX(),'[mycut]')
        break
    if not dataHistM: return dataHist
    dataHistM.SetLineColor(kBlack)
    dataHistM.SetMarkerColor(kBlack)
    dataHistM.SetMarkerStyle(20)
    dataHistM.SetFillStyle(0)
    dataHistM.GetYaxis().SetTitle('Entries')
    dataHistM.SetTitle('Mass')
    dataHistD.SetLineColor(kBlack)
    dataHistD.SetMarkerColor(kBlack)
    dataHistD.SetMarkerStyle(20)
    dataHistD.SetFillStyle(0)
    dataHistD.GetYaxis().SetTitle('Entries')
    dataHistD.SetTitle('Discriminator')
    return (dataHistM, dataHistD)

  def GetBGHists(self, histList,sigWindow = False):
    if self.doProj:
      if sigWindow:
        bgList = []
        for hist in histList:
          if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1):
            hist.GetXaxis().SetRange(hist.GetXaxis().FindBin(sigWindow-3),hist.GetXaxis().FindBin(sigWindow+3))
            bgList.append(hist.Clone().ProjectionY('proj'+hist.GetName()))
      else:
        bgList = [hist.ProjectionY('proj'+hist.GetName()) for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]
    else:
      bgList = [hist.Clone() for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]
    if len(bgList) == 0:
      bgList = None
      return bgList
    bgList = sorted(bgList, key=lambda hist:hist.GetName())
    return bgList

  def GetBGHistsMD(self, histList,sigWindow = False):
    bgListM = [hist.Clone().ProjectionX('projM'+hist.GetName(),1,hist.GetNbinsY(),'[mycut]') for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]
    bgListD = [hist.Clone().ProjectionY('projD'+hist.GetName(),1,hist.GetNbinsX(),'[mycut]') for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]
    #bgListM = [hist.ProjectionX('projM'+hist.GetName(),1,hist.GetNbinsY(),'') for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]
    #bgListD = [hist.ProjectionY('projD'+hist.GetName(),1,hist.GetNbinsX(),'') for hist in histList if (hist.GetName().find('DATA') == -1 and hist.GetName().find('Signal') == -1)]

    if len(bgListM) == 0: raise NameError('No BG hists found in this list')
    bgListM = sorted(bgListM, key=lambda hist:hist.GetName())
    bgListD = sorted(bgListD, key=lambda hist:hist.GetName())
    for i,hist in enumerate(bgListM):
      bgListM[i].GetYaxis().SetTitle('Entries')
      bgListD[i].GetYaxis().SetTitle('Entries')
      bgListM[i].SetTitle('Mass')
      bgListD[i].SetTitle('Discriminator')
    return (bgListM, bgListD)

  def GetSignalHist(self, histList,sigWindow = False):
    signalHist = None
    if self.doProj:
      for hist in histList:
        if self.sigName in hist.GetName():
          if sigWindow: hist.GetXaxis().SetRange(hist.GetXaxis().FindBin(sigWindow-3),hist.GetXaxis().FindBin(sigWindow+3))
          signalHist = hist.Clone().ProjectionY('proj'+hist.GetName())
          break
    else:
      for hist in histList:
        if self.sigName in hist.GetName():
          signalHist= hist.Clone()
          break
    if not signalHist: return signalHist
    signalHist.SetLineColor(kRed)
    signalHist.SetLineWidth(2)
    signalHist.SetFillStyle(0)
    return signalHist

  def GetSignalHistsMD(self,histList, sigWindow=False):
    signalHistM = None
    signalHistD = None
    for hist in histList:
      if self.sigName in hist.GetName():
        signalHistM = hist.Clone().ProjectionX('projM'+hist.GetName(),1,hist.GetNbinsY(),'[mycut]')
        signalHistD = hist.Clone().ProjectionY('projD'+hist.GetName(),1,hist.GetNbinsX(),'[mycut]')
        break
    if not signalHistM: raise NameError('No signalHist found in this list')
    signalHistM.SetLineColor(kRed)
    signalHistM.SetLineWidth(2)
    signalHistM.SetFillStyle(1001)
    signalHistD.SetLineColor(kRed)
    signalHistD.SetLineWidth(2)
    signalHistD.SetFillStyle(1001)
    return (signalHistM, signalHistD)


  def MakeBGStack(self, bgList, leg = None, dontStack = False):
    bgNoStack = bgList[0].Clone()
    bgNoStack.Reset()
    for hist in bgList:
      hist = hist.Clone()
      label = hist.GetName().split('_')[-1]
      scale = self.LumiXSScale(label)
      hist.Scale(scale)
      bgNoStack.Add(hist)
    bgNoStack.SetFillColor(kBlue)
    if leg and dontStack: leg.AddEntry(bgNoStack,'BG','f')
    bgStack = THStack('stack'+bgList[0].GetName(),'bgs')
    for hist in bgList:
      hist = hist.Clone()
      label = hist.GetName().split('_')[-1]
      hist.SetFillStyle(1001)
      hist.SetFillColor(colorDict[label])
      hist.SetLineColor(colorDict[label])
      scale = self.LumiXSScale(label)
      hist.Scale(scale)
      if leg and not dontStack: leg.AddEntry(hist,label,'f')
      bgStack.Add(hist)
      print hist.GetName()
      print 'bin1:',hist.GetBinContent(1)
      #raw_input()
    if dontStack:
      return bgNoStack, bgStack
    else:
      return bgStack, bgNoStack

  def MakeLegend(self,x1 = None, y1 = None, x2 = None, y2 = None):
    if x1 == y1 == x2 == y2 == None:
      x1 = 0.81
      y1 = 0.73
      x2 = 0.97
      y2 = 0.92
    leg = TLegend(x1,y1,x2,y2,'',"brNDC")
    leg.SetBorderSize(1)
    leg.SetTextSize(0.03)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    return leg

  def DrawHists(self, data,bg,signal, do2D = False, lineX = None, lineY = None):
    ymax = max(map(lambda x:x.GetMaximum(),[data,bg,signal]))*1.2
    ymin = 0
    bg.SetMaximum(ymax)
    bg.SetMinimum(ymin)
    if not do2D: bg.Draw('hist')
    else: bg.Draw('box')
    #else: bg.Draw('')
    bg.GetYaxis().SetTitle(data.GetYaxis().GetTitle())
    bg.GetYaxis().SetTitleSize(0.06)
    bg.GetYaxis().CenterTitle()
    bg.GetXaxis().SetTitle(data.GetXaxis().GetTitle())
    bg.GetXaxis().SetTitleSize(0.05)
    if do2D:
      bg.SetMarkerStyle(kBlack)
      bg.Rebin2D(3,2)
      bg.SetFillColor(kBlack)
    #bg.GetYaxis().SetLabelSize(0.05)
    #bg.GetXaxis().SetLabelSize(0.05)
    #bg.GetXaxis().SetTitle(dist)
    bg.SetTitle(self.lepton+self.lepton+' '+data.GetTitle())
    bg.GetYaxis().SetTitleOffset(0.82)
    #bg.GetXaxis().SetRangeUser(100,200)

    if not do2D: data.Draw('pesame')
    #else: data.Draw('boxsame')

    if not do2D: signal.Draw('histsame')
    else:
      signal.Set
      signal.Rebin2D(3,2)
      signal.SetFillColor(kRed)
      signal.SetFillStyle(1001)
      signal.Draw('boxsame')
      #signal.Draw('same')

    if lineX:
      print 'lineX',lineX
      print 'lineStats', lineX,bg.GetMinimum(),lineX,bg.GetMaximum()*1.05
      line = TLine(lineX,bg.GetMinimum(),lineX,ymax*1.05)
      line.SetLineColor(kRed+1)
      line.SetLineWidth(2)
      line.SetLineStyle(2)
      line.Draw()
      SetOwnership(line,0)

  def DrawHist(self, hist, do2D = False, lineX = None, lineY = None):
    if not do2D: hist.Draw('hist')
    else: hist.Draw('colz')
    if 'ME Disc' in hist.GetYaxis().GetTitle():
      ytitle = 'ME Discriminator'
    else:
      ytitle = hist.GetYaxis().GetTitle()
    hist.GetYaxis().SetTitle(ytitle)
    hist.GetYaxis().SetTitleSize(0.06)
    hist.GetYaxis().CenterTitle()
    if 'm_{ll#gamma}' in hist.GetXaxis().GetTitle():
      xtitle = 'm_{ll#gamma} (GeV)'
    else:
      xtitle = hist.GetXaxis().GetTitle()
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetXaxis().SetTitleSize(0.05)
    #bg.GetYaxis().SetLabelSize(0.05)
    #bg.GetXaxis().SetLabelSize(0.05)
    #bg.GetXaxis().SetTitle(dist)
    if 'ME Disc' in hist.GetYaxis().GetTitle():
      hist.SetTitle('ME Discriminator vs Mass')
    else:
      hist.SetTitle(self.lepton+self.lepton+' '+hist.GetTitle())
    hist.GetYaxis().SetTitleOffset(0.82)
    #bg.GetXaxis().SetRangeUser(100,200)

    if lineX:
      print 'lineX',lineX
      print 'lineStats', lineX,bg.GetMinimum(),lineX,bg.GetMaximum()*1.05
      line = TLine(lineX,bg.GetMinimum(),lineX,ymax*1.05)
      line.SetLineColor(kRed+1)
      line.SetLineWidth(2)
      line.SetLineStyle(2)
      line.Draw()
      SetOwnership(line,0)



  def MakeDrawROCandSignif(self,signalHist,bgStack,sigWindow=None):
    '''Make the ROC and significance plots, and return the best values'''
    bestCut = None
    bestBGEff= None
    bestSigEff= None
    bestSignif = 0
    rocCurve = TProfile('rocCurve',signalHist.GetTitle()+' ROC;BG eff;Signal eff',signalHist.GetNbinsX(),0,1,0,1)
    signifPlot = TProfile('signifPlot',signalHist.GetTitle()+' Signif;MEDisc;s/#sqrt{s+b}',signalHist.GetNbinsX(),signalHist.GetBinLowEdge(1),signalHist.GetBinLowEdge(1+signalHist.GetNbinsX()))

    for bin in range(1,signalHist.GetNbinsX()+1):
      #print bin, signalHist.GetBinLowEdge(bin), signalHist.GetBinContent(bin), signalHist.Integral(bin,signalHist.GetNbinsX())
      bgYield = bgStack.Integral(bin, bgStack.GetNbinsX())
      sigYield = signalHist.Integral(bin, signalHist.GetNbinsX())
      rocCurve.Fill(bgYield/bgStack.Integral(), sigYield/signalHist.Integral())


      if bin == 1:
        initialSignif = sigYield/sqrt(sigYield+bgYield)
      if sigYield+bgYield > 0:
        if (sigYield/sqrt(sigYield+bgYield) > bestSignif) and (sigYield>0.6*signalHist.Integral(1, signalHist.GetNbinsX())):
          bestSignif = sigYield/sqrt(sigYield+bgYield)
          bestCut = signalHist.GetBinLowEdge(bin)
          bestBGEff = bgYield/bgStack.Integral()
          bestSigEff = sigYield/signalHist.Integral()
        signifPlot.Fill(signalHist.GetBinLowEdge(bin),sigYield/sqrt(sigYield+bgYield))
      else:
        signifPlot.Fill(signalHist.GetBinLowEdge(bin),0)

    percentImprovement = (bestSignif-initialSignif)*100/initialSignif

    #reversed
    #for bin in range(0,signalHist.GetNbinsX()):
      #print bin, signalHist.GetBinLowEdge(bin), signalHist.GetBinContent(bin), signalHist.Integral(bin,signalHist.GetNbinsX())
      #bgYield = bgStack.Integral(1, bgStack.GetNbinsX()-bin)
      #sigYield = signalHist.Integral(1, signalHist.GetNbinsX()-bin)
      #rocCurve.Fill(bgYield/bgStack.Integral(), sigYield/signalHist.Integral())
      #if sigYield+bgYield > 0:
        #if sigYield/sqrt(sigYield+bgYield) > bestSignif:
          #bestSignif = sigYield/sqrt(sigYield+bgYield)
          #bestCut = signalHist.GetBinLowEdge(signalHist.GetNbinsX()-bin)
          #bestBGEff = bgYield/bgStack.Integral()
        #signifPlot.Fill(signalHist.GetBinLowEdge(signalHist.GetNbinsX()-bin),sigYield/sqrt(sigYield+bgYield))
      #else:
        #signifPlot.Fill(signalHist.GetBinLowEdge(signalHist.GetNbinsX()-bin),0)


    rocCurve.GetYaxis().SetTitleSize(0.06)
    rocCurve.GetYaxis().CenterTitle()
    rocCurve.GetXaxis().SetTitleSize(0.05)
    rocCurve.GetYaxis().SetTitleOffset(0.82)
    rocCurve.Draw('pe')
    line = TLine(bestBGEff,rocCurve.GetMinimum(),bestBGEff,rocCurve.GetMaximum()*1.05)
    line.SetLineColor(kRed+1)
    line.SetLineStyle(2)
    line.SetLineWidth(2)
    line.Draw()

    if sigWindow: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHist.GetName().split('_')[1]+'_ROC_window.pdf')
    else: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHist.GetName().split('_')[1]+'_ROC.pdf')

    signifPlot.SetMarkerColor(kRed)
    signifPlot.GetYaxis().SetTitleSize(0.05)
    signifPlot.GetYaxis().CenterTitle()
    signifPlot.GetXaxis().SetTitle(signalHist.GetXaxis().GetTitle())
    signifPlot.GetXaxis().SetTitleSize(0.05)
    signifPlot.GetYaxis().SetTitleOffset(1.04)
    signifPlot.GetYaxis().SetLabelSize(0.045)
    signifPlot.Draw('pe')
    line = TLine(bestCut,signifPlot.GetMinimum(),bestCut,signifPlot.GetMaximum()*1.05)
    line.SetLineColor(kRed+1)
    line.SetLineWidth(2)
    line.SetLineStyle(2)
    line.Draw()
    signifStats = TPaveText(bestCut,signifPlot.GetMaximum()*0.02,bestCut+0.5,signifPlot.GetMaximum()*0.30)
    #SetOwnership(signifStats,False)
    signifStats.SetBorderSize(0)
    signifStats.SetFillStyle(0)
    signifStats.SetFillColor(0)
    signifStats.SetTextFont(42)
    signifStats.SetTextSize(0.035)
    signifStats.AddText('Discrim Cut: {0:.2}'.format(bestCut))
    signifStats.AddText('Significance (start): {0:.2}'.format(initialSignif))
    signifStats.AddText('Significance (best): {0:.2}'.format(bestSignif))
    signifStats.AddText('Improvement: {0:.3}%'.format(percentImprovement))
    signifStats.AddText('BG Eff: {0:.2}'.format(bestBGEff))
    signifStats.AddText('Sig Eff: {0:.2}'.format(bestSigEff))
    signifStats.Draw()


    if sigWindow: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHist.GetName().split('_')[1]+'_Signif_Window.pdf')
    else: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHist.GetName().split('_')[1]+'_Signif.pdf')

    return (bestCut,bestBGEff,bestSignif,percentImprovement)


  def DataBGComp(self,histList,soloPlot = None, doLeg = True):
    '''Give a list of histograms that contain the data and backgrounds, plot them and save them'''
    if len(histList) == 0: raise NameError('histList is empty')

    gStyle.SetOptStat(0)
    do2D = False
    if histList[0].GetName().split('_')[0] in ['h2','p']: do2D = True

    dataHist = self.GetDataHist(histList)
    bgList = self.GetBGHists(histList)
    signalHist = self.GetSignalHist(histList)

    if None in [dataHist,bgList,signalHist]:
      print 'Missing data, signal, or bg in', histList[0].GetName().split('_')[1], 'skipping'
      return

    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    # Make legend and canvas
    self.can= TCanvas('can','canvas',800,600)
    self.can.cd()
    if do2D:
      self.can.SetRightMargin(0.1)
      leg = self.MakeLegend(0.75,0.75,0.90,0.92)
    else:
      leg = self.MakeLegend()
    if soloPlot in [None, 'Data']:
      if not do2D:
        leg.AddEntry(dataHist,'DATA','lep')

    if soloPlot in [None, 'bg']:
      bgStack,tmp = self.MakeBGStack(bgList,leg,do2D)

    scale = self.LumiXSScale(self.sigName)
    signalHist.Scale(scale*200)
    if soloPlot in [None, 'Signal']:
      if do2D:
        leg.AddEntry(signalHist,'Signalx200','f')
      else:
        leg.AddEntry(signalHist,'Signalx200','l')

    if soloPlot == None:
      self.DrawHists(dataHist,bgStack,signalHist,do2D)
      #self.DrawHists(dataHist,dataHist,signalHist,do2D)
    elif soloPlot == 'Data':
      self.DrawHist(dataHist,do2D)
    elif soloPlot == 'Signal':
      self.DrawHist(signalHist,do2D)
    elif soloPlot == 'bg':
      self.DrawHist(bgStack,do2D)
    else:
      print 'you didnt specify soloPlot correctly'


    if doLeg: leg.Draw()
    if soloPlot == None:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+dataHist.GetName().split('_')[1]+'.pdf')
    else:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+dataHist.GetName().split('_')[1]+'_'+soloPlot+'.pdf')

    self.can.IsA().Destructor(self.can)

  def DataBGComp2DProj(self,histList, sigWindow = False):
    '''Project the Y-axis of 2D hists.  If a sigWindow is specified, the assumption is that the x-axis is the 3body mass'''
    if len(histList) == 0: raise NameError('histList is empty')
    gStyle.SetOptStat(0)
    if histList[0].GetName().split('_')[0] != 'h2':
      print 'skipping 2D proj for', histList[0].GetName()
      return

    self.doProj = True

    dataHist = self.GetDataHist(histList,sigWindow)
    bgList =self.GetBGHists(histList,sigWindow)
    signalHist = self.GetSignalHist(histList,sigWindow)


    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    # Make canvas and legend
    self.can= TCanvas('can','canvas',800,600)
    self.can.cd()
    leg = self.MakeLegend()

    leg.AddEntry(dataHist,'DATA','lep')

    # Set the bg histograms
    bgStack = self.MakeBGStack(bgList,leg)

    # Set the signal histograms
    scale = self.LumiXSScale(self.sigName)
    signalHist.Scale(scale*500)
    leg.AddEntry(signalHist,'Signalx500','l')

    self.DrawHists(dataHist,bgStack,signalHist)

    leg.Draw()
    if sigWindow:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+dataHist.GetName().split('_')[1]+'projWindow.pdf')
    else:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+dataHist.GetName().split('_')[1]+'proj.pdf')
    self.can.IsA().Destructor(self.can)
    self.doProj = False

  def ROCcurves(self, histList,sigWindow=False):
    '''Give a list of histograms, calculate ROC curve for that distribution.  Need 2D hist, mass vs disc for proper significance calculation'''
    if len(histList) == 0: raise NameError('histList is empty')
    gStyle.SetOptStat(0)
    if histList[0].GetName().split('_')[0] != 'h2':
      print 'skipping ROC curve for', histList[0].GetName()
      return
    if sigWindow:
      self.myCut = TCutG('mycut',5)
      self.myCut.SetPoint(0,sigWindow-4,-2)
      self.myCut.SetPoint(1,sigWindow-4,2)
      self.myCut.SetPoint(2,sigWindow+4,2)
      self.myCut.SetPoint(3,sigWindow+4,-2)
      self.myCut.SetPoint(4,sigWindow-4,-2)
    else:
      self.myCut = TCutG('mycut',5)
      self.myCut.SetPoint(0,115,-2)
      self.myCut.SetPoint(1,115,2)
      self.myCut.SetPoint(2,165,2)
      self.myCut.SetPoint(3,165,-2)
      self.myCut.SetPoint(4,115,-2)




    for hist in histList:
      print hist.GetName()
    dataHistM,dataHistD = self.GetDataHistsMD(histList,sigWindow)
    bgListM,bgListD = self.GetBGHistsMD(histList,sigWindow)
    signalHistM, signalHistD = self.GetSignalHistsMD(histList,sigWindow)


    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TH2.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    self.can= TCanvas('can'+self.lepton,'canvas',800,600)
    self.can.cd()
    legM = self.MakeLegend()
    legD = self.MakeLegend()
    legM.AddEntry(dataHistM,'DATA','lep')
    legD.AddEntry(dataHistD,'DATA','lep')

    # Set the bg histograms

    print 'mass'
    bgStackM = self.MakeBGStack(bgListM,legM)
    print 'disc'
    bgStackD = self.MakeBGStack(bgListD,legD)
    bgStackROC = self.MakeBGStack(bgListD,None,True)

    scale = self.LumiXSScale(self.sigName)
    signalHistM.Scale(scale*100)
    signalHistD.Scale(scale)

    #temp switch, use data instead of MC:
    #WARNING: TURN THIS OFF FOR ACTUAL RUNNING
    #bgStackM = dataHistM
    #bgStackD = dataHistD
    #bgStackROC = dataHistD

    #make ROC and signif plots and get the best values
    cutVal,BGeffVal,signifVal,signifChange = self.MakeDrawROCandSignif(signalHistD,bgStackROC,sigWindow)

    print 'cutVal:', cutVal
    print 'BGeffVal:', BGeffVal
    print 'signifVal:', signifVal
    print 'signifChange:', signifChange

    legM.AddEntry(signalHistM,'Signalx100','l')
    legD.AddEntry(signalHistD,'Signalx100','l')

    self.DrawHists(dataHistM,bgStackM,signalHistM,False)
    legM.Draw()

    if sigWindow: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHistM.GetName().split('_')[1]+'_MassCheck_Window.pdf')
    else: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHistM.GetName().split('_')[1]+'_MassCheck.pdf')
    self.can.Clear()
    signalHistD.Scale(100)

    self.DrawHists(dataHistD,bgStackD,signalHistD,False,cutVal)
    legD.Draw()

    if sigWindow: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHistD.GetName().split('_')[1]+'_DiscCheck_Window.pdf')
    else: self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+signalHistD.GetName().split('_')[1]+'_DiscCheck.pdf')
    self.can.Clear()

    dataHistD.IsA().Destructor(dataHistD)
    dataHistM.IsA().Destructor(dataHistM)
    signalHistD.IsA().Destructor(signalHistD)
    signalHistM.IsA().Destructor(signalHistM)
    for hist in bgListM:
      hist.IsA().Destructor(hist)
    for hist in bgListD:
      hist.IsA().Destructor(hist)
    self.myCut.Clear()

    #self.can.IsA().Destructor(self.can)

  def RatioPlot(self, key, chooseNames, legendNames, norm = False, logy = False):
    '''Get two plots, normalize them, compare with ratio'''
    if type(self.thisFile) != list:
        histList = self.folderDict[key]
        if len(histList) == 0: raise NameError('histList is empty')
        gStyle.SetOptStat(0)
        if histList[0].GetName().split('_')[0] == 'h2':
          print 'skipping ratio plot for', histList[0].GetName()
          return

        compHists = self.ChooseTwoHists(chooseNames, histList, norm = norm)
    else:
        histList1 = self.folderDict[0][key]
        histList2 = self.folderDict[1][key]
        if len(histList1) == 0: raise NameError('histList1 is empty')
        if len(histList2) == 0: raise NameError('histList2 is empty')
        gStyle.SetOptStat(0)
        if histList1[0].GetName().split('_')[0] == 'h2':
          print 'skipping ratio plot for', histList1[0].GetName()
          return
        if histList2[0].GetName().split('_')[0] == 'h2':
          print 'skipping ratio plot for', histList2[0].GetName()
          return

        compHists = self.ChooseTwoHists(chooseNames,histList1,histList2,norm = norm)

    if compHists == None:
      print 'Cannot find all the necessary histograms for ratio, skipping', key
      return

    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    self.can= TCanvas('ratioCan','canvas',800,600)
    self.can.cd()
    leg = self.MakeLegend(0.85,0.83,1.00,1.00)

    pad1 = TPad('pad1', '', 0.00, 0.30, 1.0, 0.98, 0)
    #SetOwnership(pad1,False)
    pad1.SetBottomMargin(0.03)
    pad1.SetLeftMargin(0.09)
    pad1.SetRightMargin(0.018)
    pad1.SetGrid(2,2)
    pad2 = TPad('pad2', '', 0.00, 0.02, 1.0, 0.32, 0)
    #SetOwnership(pad2,False)
    pad2.SetTopMargin(0.)
    pad2.SetBottomMargin(0.25)
    pad2.SetLeftMargin(0.09)
    pad2.SetRightMargin(0.018)
    pad2.SetGrid(2,2)

    self.can.cd()
    pad1.Draw()
    pad2.Draw()
    pad1.cd()
    if logy: pad1.SetLogy()

    bgStack = None
    bgNoStack = None
    if type(compHists[0]) is TProfile:
      h1 = compHists[0].ProjectionX()
      h2 = compHists[1].ProjectionX()
      ratio = h1.Clone()
      ratio.Divide(h2.Clone())
      h1.IsA().Destructor(h1)
      h2.IsA().Destructor(h2)
    else:
      ratio = compHists[0].Clone()
      ratio.Divide(compHists[1])
    for i,plot in enumerate(compHists):
      stackLeg = False
      if i == 0:
        if chooseNames[0] == 'DATA' and chooseNames[1] != 'DATA':
          if logy:
            plot.SetMinimum(0.1)
          plot.SetMarkerColor(kBlack)
          plot.SetMarkerStyle(20)
          plot.Draw('pe')

        elif chooseNames[0] == 'BG' and chooseNames[1] != 'BG':
          if norm:
            plot.Draw('hist')
          else:
            try: bgList = self.GetBGHists(histList)
            except: bgList = self.GetBGHists(histList1)
            if logy:
              for bg in bgList:
                bg.SetMinimum(0.1)
            bgStack,bgNoStack = self.MakeBGStack(bgList,leg,False)
            bgStack.Draw('hist')
            stackLeg = True
        else:
          plot.Draw('hist')
      else:
        if chooseNames[1] == 'DATA' and chooseNames[0] != 'DATA':
          plot.SetMarkerColor(kBlack)
          plot.SetMarkerStyle(20)
          plot.Draw('pesame')
        elif chooseNames[1] == 'BG' and chooseNames[0] != 'BG':
          if norm:
            plot.Draw('histsame')
          else:
            try: bgList = self.GetBGHists(histList)
            except: bgList = self.GetBGHists(histList2)
            if logy:
              for bg in bgList:
                bg.SetMinimum(0.1)
            bgStack,bgNoStack = self.MakeBGStack(bgList,leg,False)
            bgStack.Draw('histsame')
            stackLeg = True
        else:
          plot.Draw('histsame')
      if not stackLeg: leg.AddEntry(plot,legendNames[i],'l')
    if 'DATA' in chooseNames:
      idat = chooseNames.index('DATA')
      compHists[idat].Draw('pesame')
    if 'Signal' in chooseNames:
      idat = chooseNames.index('Signal')
      compHists[idat].Draw('histsame')
    if bgNoStack != None: print compHists[0].GetName(), compHists[0].Integral(), bgNoStack.GetName(), bgNoStack.Integral(), compHists[0].Integral()/sqrt(bgNoStack.Integral()+compHists[0].Integral())

    leg.Draw()
    pad2.cd()
    ratio.SetTitle('')
    ratio.SetLineColor(kBlack)
    ratio.SetMarkerColor(kBlack)
    ratio.GetYaxis().SetTitle('#frac{'+legendNames[0]+'}{'+legendNames[1]+'}')
    ratio.GetYaxis().CenterTitle()
    ratio.GetXaxis().SetTitleSize(0.12)
    ratio.GetXaxis().SetLabelSize(0.12)
    ratio.GetYaxis().SetTitleSize(0.08)
    ratio.GetYaxis().SetTitleOffset(0.38)
    ratio.GetYaxis().SetLabelSize(0.09)
    ratio.GetYaxis().SetNdivisions(506)
    ratio.SetMinimum(max(0.5,ratio.GetBinContent(ratio.GetMinimumBin())*0.9))
    ratio.SetMaximum(min(1.5,ratio.GetBinContent(ratio.GetMaximumBin())*1.1))
    #print 'max', ratio.GetBinContent(ratio.GetMaximumBin())
    #print 'min', ratio.GetBinContent(ratio.GetMinimumBin())
    #ratio.SetMinimum(max(ratio.GetMinimum()*0.7,0.5))
    #ratio.SetMaximum(min(ratio.GetMaximum()*1.3,2))
    ratio.Draw()
    line = TLine(ratio.GetBinLowEdge(1),1.00,ratio.GetBinLowEdge(ratio.GetNbinsX()+ 1),1.00)
    line.SetLineColor(kRed)
    line.SetLineWidth(2)
    line.Draw()
    self.can.cd()
    zero = TPaveText(0.07,0.305,0.087,0.335)
    #SetOwnership(zero,False)
    zero.SetBorderSize(0)
    zero.SetFillStyle(1001)
    zero.SetFillColor(0)
    zero.SetTextFont(42)
    zero.SetTextSize(0.035)
    zero.AddText('0')
    zero.Draw()
    if chooseNames[0] == chooseNames[1]: ratioNames = chooseNames[0]
    else: ratioNames = chooseNames[0]+chooseNames[1]
    self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+compHists[0].GetName().split('_')[1]+
            '_'+ratioNames+'.pdf')
    self.can.IsA().Destructor(self.can)

  def MultiPlots(self, keys, chooseNames, legendNames, norm = False,logy=False):
    '''Get N plots, plot them'''
    if type(self.thisFile) != list:
      print 'must have lists of files'
    else:
      histListN = []
      for i in range(len(self.folderDict)):
        histListN.append(self.folderDict[i][keys[i]])
        if len(histListN[-1]) == 0: raise NameError('histList{0} is empty, {1}'.format(i,keys[i]))
        if histListN[-1][0].GetName().split('_')[0] == 'h2':
          print 'skipping ratio plot for', histListN[-1][0].GetName()
          return
      gStyle.SetOptStat(0)
      compHists = self.ChooseNHists(chooseNames,histListN,norm = norm, fNum = chooseNames.index('BG'))

    if compHists == None:
      print 'Cannot find all the necessary histograms for ratio, skipping', keys
      return

    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    self.can= TCanvas('multiCan','canvas',800,600)
    self.can.cd()
    self.can.SetLogy(logy)
    leg = self.MakeLegend(0.7,0.90-0.05*len(legendNames),0.95,0.90)
    for i,plot in enumerate(compHists):
      if i ==0:
        if logy: plot.SetMinimum(0.0001)
        plot.Draw('hist')

      else:
        plot.Draw('histsame')
      leg.AddEntry(plot,legendNames[i],'l')
    leg.Draw()

    ratioNames = ''.join(chooseNames)
    self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+compHists[0].GetName().split('_')[1]+
            '_'+ratioNames+'.pdf')
    self.can.IsA().Destructor(self.can)

  def AcceptancePlot(self, massList, doNarrow = False):
    '''Make AcceptanceXEff plots as a function of mass'''
    x = np.array(massList,float)
    y = np.zeros(len(massList),float)
    xerr = np.zeros(len(massList),float)
    yerr = np.zeros(len(massList),float)
    histList = self.folderDict['acceptanceByCut']
    syst = 0
    if self.lepton == 'mu':
      syst = sqrt(0.04**2+0.035**2+0.01**2+0.014**2+0.004**2)
    else:
      syst = sqrt(0.04**2+0.02**2+0.01**2+0.008**2+0.008**2)
    for i,mass in enumerate(massList):
      if doNarrow:
        hist = filter(lambda x: str(mass) in x.GetName() and 'Narrow' in x.GetName(), histList)[0]
      else:
        hist = filter(lambda x: str(mass) in x.GetName() and 'Narrow' not in x.GetName(), histList)[0]
      initEvents = hist.GetBinContent(1)
      finalEvents= hist.GetBinContent(19)
      accEff = float(finalEvents)/float(initEvents/3)
      accErr = accEff*syst
      print initEvents, finalEvents, accEff
      y[i] = accEff
      yerr[i] = accErr

    print x, y
    accPlot = TGraphErrors(len(massList),x,y,xerr,yerr)
    accPlot.GetXaxis().SetTitle('Signal Mass (GeV)')
    accPlot.GetYaxis().SetTitle('Acceptance X Efficiency')
    accPlot.GetYaxis().CenterTitle()
    accPlot.SetTitle(self.lepton+self.lepton+' Channel')
    accPlot.SetFillColor(kCyan)

    gStyle.SetOptStat(0)

    if not os.path.isdir(self.directory):
      os.mkdir(self.directory)

    TH1.SetDefaultSumw2(kTRUE)
    TProfile.SetDefaultSumw2(kTRUE)

    self.can= TCanvas('multiCan','canvas',800,600)
    self.can.cd()
    self.can.SetLeftMargin(0.13)
    self.can.SetBottomMargin(0.13)
    accPlot.Draw('ALE3')
    accPlot.Draw('LXsame')
    leg = self.MakeLegend(0.7,0.30,0.85,0.45)

    leg.AddEntry(accPlot,'#pm 1 #sigma syst','F')
    leg.Draw()

    if doNarrow:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+'AccEffNarrow'+'.pdf')
    else:
      self.can.SaveAs(self.directory+'/'+self.lepton+self.lepton+'_'+'AccEff'+'.pdf')
    self.can.IsA().Destructor(self.can)

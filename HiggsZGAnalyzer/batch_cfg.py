#! /usr/bin/env python
import BatchMaster as b
import os

EOS         = '/eos/uscms/store/user/bpollack'
dCache      = '/pnfs/cms/WAX/11/store/user/bpollack'
t3storage   = '/tthome/share/noobs/'

outputPathFNAL  = '/uscms/home/bpollack/nobackup/BatchOutput'
outputPathNWU  = '/tthome/bpollack/BatchOutput'


do7Tev = False
doHighMass = True
doLite = False
configs = []

if doLite:
  leptonDict = {'MuE':'mueGamma'}
  analyzer = 'smzgAnalyzer'
  pu = 'S10'

if doHighMass:
  leptonDict = {'Mu':'mumuGamma','Electron':'eeGamma'}
  massList = [125]+range(200,550,50)
  sigList = ['gg']
  pu = 'S10'
  analyzer = 'higgsAnalyzer'
else:
  sigList = ['gg','vbf','tth','wh','zh']
  leptonDict = {'Mu':'mumuGamma','Electron':'eeGamma'}
  massList = range(120,165,5)+[123]
  pu = 'RD1'
  analyzer = 'higgsAnalyzer'


#different pathnames and executables for NWU or FNAL
if os.environ.get('AT_NWU') == None: raise Exception('cannot run at FNAL')

os.system('tar -zcvf stageball.tar.gz {0}* ../src  otherHistos ../plugins ../interface ../mva/testWeights* ../txtFiles ../input.DAT ../process.DAT ../Pdfdata ../br.sm*'.format(analyzer))

#####################
# regular selection #
#####################
if not do7Tev and not doLite:
  for lepton in leptonDict:
    for sig in sigList:
      if sig in ['wh','zh']:
        sigFile = 'whzh'
      else:
        sigFile = sig
      for mass in massList:
        if sig != 'gg' and mass == 123: continue
        if mass == 125:
          puPass = 'RD1'
        else:
          puPass = pu

        configs.append(b.JobConfig('{0}HZG_M{1}'.format(sig,mass),
          t3storage+'/nuTuples_v9.8_8TeV/MC/{0}HZG_M{1}_{2}'.format(sigFile,mass,puPass),
          5,
          'Signal2012{0}M{1} ABCD {2} 2012 {3} {4}'.format(sig,mass,leptonDict[lepton],puPass,analyzer),
          leptonDict[lepton]))

        if doHighMass:
          if mass == 125: pass
          else:
            configs.append(b.JobConfig('{0}HZG_M{1}_Narrow'.format(sig,mass),
              t3storage+'/nuTuples_v9.8_8TeV/MC/{0}HZG_M{1}_Narrow_{2}'.format(sigFile,mass,puPass),
              5,
              'Signal2012{0}M{1}Narrow ABCD {2} 2012 {3} {4}'.format(sig,mass,leptonDict[lepton],puPass,analyzer),
              leptonDict[lepton]))

    if lepton == 'Mu':
      configs.append(b.JobConfig('Run2012A', t3storage+'/nuTuples_v9.8_8TeV/Data/Double'+lepton+'_Run2012A_v2', 50, 'DATA ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu, analyzer),leptonDict[lepton]))
    else:
      configs.append(b.JobConfig('Run2012A', t3storage+'/nuTuples_v9.8_8TeV/Data/Double'+lepton+'_Run2012A', 50, 'DATA ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu, analyzer),leptonDict[lepton]))
    configs.append(b.JobConfig('Run2012B', t3storage+'/nuTuples_v9.8_8TeV/Data/Double'+lepton+'_Run2012B', 100, 'DATA ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu,analyzer),leptonDict[lepton]))
    configs.append(b.JobConfig('Run2012C', t3storage+'/nuTuples_v9.8_8TeV/Data/Double'+lepton+'_Run2012C', 150, 'DATA ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu,analyzer),leptonDict[lepton]))
    configs.append(b.JobConfig('Run2012D', t3storage+'/nuTuples_v9.8_8TeV/Data/Double'+lepton+'_Run2012D', 150, 'DATA ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu,analyzer),leptonDict[lepton]))

    if lepton == 'Mu': lepTag = 'MuMu'
    else: lepTag = 'EE'
    configs.append(b.JobConfig('ZGToLLG', t3storage+'/nuTuples_v9.8_8TeV/MC/ZGToLLG_'+pu, 50, 'ZGToLLG ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu,analyzer),leptonDict[lepton]))
    #configs.append(b.JobConfig('DYJets', t3storage+'/nuTuples_v9.8_8TeV/MC/DYJetsToLL_M-50_RD1', 150, 'DYJets ABCD {0} 2012 {1} {2} {0}'.format(leptonDict[lepton],pu,analyzer),leptonDict[lepton]))
    configs.append(b.JobConfig('DYTo'+lepTag, t3storage+'/nuTuples_v9.8_8TeV/MC/DYTo'+lepTag+'_M-20_'+pu, 200, 'DYTo{3} ABCD {0} 2012 {1} {2}'.format(leptonDict[lepton],pu,analyzer,lepTag),leptonDict[lepton]))

##################
# 2011 selection #
##################
elif do7Tev:
  configs.append(b.JobConfig('Run2011A', t3storage+'/nuTuples_v9.8_7TeV/Data/DoubleMu_Run2011A', 100, 'DATA AB mumuGamma 2011 RD1 {0}'.format(analyzer),'mumuGamma'))
  configs.append(b.JobConfig('Run2011B', t3storage+'/nuTuples_v9.8_7TeV/Data/DoubleMu_Run2011B', 100, 'DATA AB mumuGamma 2011 RD1 {0}'.format(analyzer),'mumuGamma'))

##################
# jpsi selection #
##################
elif doLite:
  configs.append(b.JobConfig('Run2012A', t3storage+'/nuTuples_v9.8_8TeV/Data/MuEG_Run2012A', 50, 'DATA ABCD mueGamma 2012 RD1 {0}'.format(analyzer),'mueGamma'))
  configs.append(b.JobConfig('Run2012B', t3storage+'/nuTuples_v9.8_8TeV/Data/MuEG_Run2012B', 100, 'DATA ABCD mueGamma 2012 RD1 {0}'.format(analyzer),'mueGamma'))
  configs.append(b.JobConfig('Run2012C', t3storage+'/nuTuples_v9.8_8TeV/Data/MuEG_Run2012C', 150, 'DATA ABCD mueGamma 2012 RD1 {0}'.format(analyzer),'mueGamma'))
  configs.append(b.JobConfig('Run2012D', t3storage+'/nuTuples_v9.8_8TeV/Data/MuEG_Run2012D', 150, 'DATA ABCD mueGamma 2012 RD1 {0}'.format(analyzer),'mueGamma'))
  configs.append(b.JobConfig('ZtoJPsiGamma','/tthome/bpollack/storage/nuTuples_v9.7_8TeV/MC/ZtoJPsiGamma', 10, 'ZtoJPsiGamma ABCD mueGamma 2012 S10 {0}'.format(analyzer),'mueGamma'))


batcher = b.BatchMaster(configs, outputPathNWU,'execBatch.sh')
batcher.SubmitToLPC()

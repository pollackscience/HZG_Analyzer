#include "../interface/AnalysisParameters.h"

using namespace std;

Parameters::Parameters():
  selection("lol"),
  period("lol"),
  JC_LVL(0),
  abcd("lol"),
  suffix("lol"),
  dataname("lol"),
  jobCount("lol"),

  VBFcuts(false),
  DYGammaVeto(true),
  customPhotoID(false),
  spikeVeto(true),
  R9switch(false),
  doEleMVA(true),
  doLooseMuIso(true),
  doAnglesMVA(true),
  doPhotonPurityStudy(false),
  doPhoMVA(true),

  dumps(false),
  dataDumps(false),
  EVENTNUMBER(-999),

  engCor(true),
  doR9Cor(true),
  doEleReg(true),
  doScaleFactors(true),
  doLumiXS(false)
{}


Cuts::~Cuts(){}
Cuts::Cuts():
  leadJetPt(30),
  trailJetPt(30),
  leadMuPt(20),
  trailMuPt(10),
  leadElePt(20),
  trailElePt(10),
  gPtOverMass(15./110.),
  gPt(15),
  zMassLow(50),
  zMassHigh(999999),
  metLow(-9999),
  metHigh(9999),
  zgMassLow(100),
  zgMassHigh(190),
  mzPmzg(185),
  dR(0.4),
  ME(0.02),
  dRJet(0.5),
  dEtaJet(3.5),
  zepp(2.5),
  mjj(500),
  dPhiJet(2.4),
  EAMu(),
  EAEle(),
  EAPho(),
  tightMuID(),
  tightMuIso(),
  looseMuIso(),
  vetoElID(),
  looseElID(),
  looseElIso(),
  loosePhID(),
  mediumPhID(),
  loosePhIso(),
  mediumPhIso(),
  vbfJetID()
{
  vetoElID.cutName =                     "vetoElID";
  vetoElID.dEtaIn[0] =                   0.007;
  vetoElID.dPhiIn[0] =                   0.8;
  vetoElID.sigmaIetaIeta[0] =            0.01;
  vetoElID.HadOverEm[0] =                0.15;
  vetoElID.dxy[0] =                      0.04;
  vetoElID.dz[0] =                       0.2;
  vetoElID.fabsEPDiff[0] =               99999;
  vetoElID.ConversionMissHits[0] =       99999;
  vetoElID.PassedConversionProb[0] =     1;

  vetoElID.dEtaIn[1] =                   0.01;
  vetoElID.dPhiIn[1] =                   0.7;
  vetoElID.sigmaIetaIeta[1] =            0.03;
  vetoElID.HadOverEm[1] =                999999;
  vetoElID.dxy[1] =                      0.04;
  vetoElID.dz[1] =                       0.2;
  vetoElID.fabsEPDiff[1] =               999999;
  vetoElID.ConversionMissHits[1] =       999999;
  vetoElID.PassedConversionProb[1] =     1;

  looseElID.cutName =                     "looseElID";
  looseElID.dEtaIn[0] =                   0.007;
  looseElID.dPhiIn[0] =                   0.15;
  looseElID.sigmaIetaIeta[0] =            0.01;
  looseElID.HadOverEm[0] =                0.12;
  looseElID.dxy[0] =                      0.02;
  looseElID.dz[0] =                       0.2;
  looseElID.fabsEPDiff[0] =               0.05;
  looseElID.ConversionMissHits[0] =       1;
  looseElID.PassedConversionProb[0] =     1;

  looseElID.dEtaIn[1] =                   0.009;
  looseElID.dPhiIn[1] =                   0.10;
  looseElID.sigmaIetaIeta[1] =            0.03;
  looseElID.HadOverEm[1] =                0.10;
  looseElID.dxy[1] =                      0.02;
  looseElID.dz[1] =                       0.2;
  looseElID.fabsEPDiff[1] =               0.05;
  looseElID.ConversionMissHits[1] =       1;
  looseElID.PassedConversionProb[1] =     1;

  mvaPreElID.cutName =                     "mvaPreElID";
  mvaPreElID.dEtaIn[0] =                   99999;
  mvaPreElID.dPhiIn[0] =                   9999;
  mvaPreElID.sigmaIetaIeta[0] =            0.014;
  mvaPreElID.HadOverEm[0] =                0.15;
  mvaPreElID.dxy[0] =                      99999;
  mvaPreElID.dz[0] =                       99999;
  mvaPreElID.fabsEPDiff[0] =               99999;
  mvaPreElID.ConversionMissHits[0] =       99999;
  mvaPreElID.PassedConversionProb[0] =     99999;
  mvaPreElID.dr03TkSumPt[0] =              0.2;
  mvaPreElID.dr03EcalRecHitSumEt[0] =      0.2;
  mvaPreElID.dr03HcalTowerSumEt[0] =       0.2;
  mvaPreElID.numberOfLostHits[0] =         0;

  mvaPreElID.dEtaIn[1] =                   99999;
  mvaPreElID.dPhiIn[1] =                   99999;
  mvaPreElID.sigmaIetaIeta[1] =            0.035;
  mvaPreElID.HadOverEm[1] =                0.10;
  mvaPreElID.dxy[1] =                      99999;
  mvaPreElID.dz[1] =                       99999;
  mvaPreElID.fabsEPDiff[1] =               99999;
  mvaPreElID.ConversionMissHits[1] =       99999;
  mvaPreElID.PassedConversionProb[1] =     99999;
  mvaPreElID.dr03TkSumPt[1] =              0.2;
  mvaPreElID.dr03EcalRecHitSumEt[1] =      0.2;
  mvaPreElID.dr03HcalTowerSumEt[1] =       0.2;
  mvaPreElID.numberOfLostHits[1] =         0;

  
  looseElIso.cutName =                    "looseElIso";
  looseElIso.chIso04 =                    99999;
  looseElIso.nhIso04 =                    99999;
  looseElIso.phIso04 =                    99999;
  looseElIso.relCombIso04 =               0.4;

  tightMuID.cutName =                     "tightMuID";
  tightMuID.IsPF =                        1;
  tightMuID.IsGLB =                       1;
  tightMuID.IsTRK =                       1;
  tightMuID.NormalizedChi2 =              10;
  tightMuID.NumberOfValidMuonHits =       0;
  tightMuID.NumberOfMatchedStations =     1;
  tightMuID.NumberOfValidPixelHits =      0;
  tightMuID.TrackLayersWithMeasurement =  5;
  tightMuID.dxy =                         0.2;
  tightMuID.dz =                          0.5;

  dalitzMuID.cutName =                     "dalitzMuID";
  dalitzMuID.IsPF =                        1;
  dalitzMuID.IsGLB =                       1;
  dalitzMuID.IsTRK =                       1;
  dalitzMuID.NormalizedChi2 =              9999;
  dalitzMuID.NumberOfValidMuonHits =       -1;
  dalitzMuID.NumberOfMatchedStations =     0;
  dalitzMuID.NumberOfValidPixelHits =      -1;
  dalitzMuID.TrackLayersWithMeasurement =  -1;
  dalitzMuID.dxy =                         0.2;
  dalitzMuID.dz =                          0.5;
  
  tightMuIso.cutName =                    "tightMuIso";
  tightMuIso.chIso04 =                    99999;
  tightMuIso.nhIso04 =                    99999;
  tightMuIso.phIso04 =                    99999;
  tightMuIso.relCombIso04 =               0.12;

  looseMuIso.cutName =                    "looseMuIso";
  looseMuIso.chIso04 =                    99999;
  looseMuIso.nhIso04 =                    99999;
  looseMuIso.phIso04 =                    99999;
  looseMuIso.relCombIso04 =               0.4;

  loosePhID.cutName =                     "loosePhID";
  loosePhID.PassedEleSafeVeto[0] =        1;
  loosePhID.HadOverEm[0] =                0.05;
  loosePhID.sigmaIetaIeta[0] =            0.012;

  loosePhID.PassedEleSafeVeto[1] =        1;
  loosePhID.HadOverEm[1] =                0.05;
  loosePhID.sigmaIetaIeta[1] =            0.034;

  loosePhIso.cutName =                    "loosePhIso";
  loosePhIso.chIso03[0] =                 2.6;
  loosePhIso.nhIso03[0] =                 3.5;
  loosePhIso.phIso03[0] =                 1.3;

  loosePhIso.chIso03[1] =                 2.3;
  loosePhIso.nhIso03[1] =                 2.9;
  loosePhIso.phIso03[1] =                 99999;

  mediumPhID.cutName =                     "mediumPhID";
  mediumPhID.PassedEleSafeVeto[0] =        1;
  mediumPhID.HadOverEm[0] =                0.05;
  mediumPhID.sigmaIetaIeta[0] =            0.011;

  mediumPhID.PassedEleSafeVeto[1] =        1;
  mediumPhID.HadOverEm[1] =                0.05;
  mediumPhID.sigmaIetaIeta[1] =            0.033;

  mediumPhIso.cutName =                    "mediumPhIso";
  mediumPhIso.chIso03[0] =                 1.5;
  mediumPhIso.nhIso03[0] =                 1.0;
  mediumPhIso.phIso03[0] =                 0.7;

  mediumPhIso.chIso03[1] =                 1.2;
  mediumPhIso.nhIso03[1] =                 1.5;
  mediumPhIso.phIso03[1] =                 1.0;

  preSelPhID.cutName =                     "preSelPhID";
  preSelPhID.PassedEleSafeVeto[0] =        1;
  preSelPhID.HadOverEm[0] =                0.082;
  preSelPhID.sigmaIetaIeta[0] =            0.014;
  preSelPhID.HcalIso[0] =                  50;
  preSelPhID.TrkIso[0] =                   50;
  preSelPhID.ChPfIso[0] =                  4;

  preSelPhID.PassedEleSafeVeto[1] =        1;
  preSelPhID.HadOverEm[1] =                0.075;
  preSelPhID.sigmaIetaIeta[1] =            0.034;
  preSelPhID.HcalIso[1] =                  4;
  preSelPhID.TrkIso[1] =                   4;
  preSelPhID.ChPfIso[1] =                  4;

  catPhMVAID.cutName =                     "catPhMVAID";
  catPhMVAID.mvaValCat1 =                  0.126;
  catPhMVAID.mvaValCat2 =                  0.107;
  catPhMVAID.mvaValCat3 =                  0.126;
  catPhMVAID.mvaValCat4 =                  0.135;

  vbfJetID.cutName =                       "vbfJetID";
  vbfJetID.betaStarC[0] =                  0.2;
  vbfJetID.dR2Mean[0] =                    0.06;

  vbfJetID.betaStarC[1] =                  0.3;
  vbfJetID.dR2Mean[1] =                    0.05;

  vbfJetID.dR2Mean[2] =                    0.05;

  vbfJetID.dR2Mean[3] =                    0.055;
}

void Cuts::InitEA(string year)
{
  if (year.find("2012") != string::npos){
    //combined rel ISO, 2012 Data, 0.5 GeV
    EAMu[0] =   0.674; //         eta < 1.0
    EAMu[1] =   0.565; // 1.0   < eta < 1.5
    EAMu[2] =   0.442; // 1.5   < eta < 2.0
    EAMu[3] =   0.515; // 2.0   < eta < 2.2
    EAMu[4] =   0.821; // 2.2   < eta < 2.3
    EAMu[5] =   0.660; // 2.3   < eta < 2.4

    EAEle[0] =   0.208; //         eta < 1.0
    EAEle[1] =   0.209; // 1.0   < eta < 1.5
    EAEle[2] =   0.115; // 1.5   < eta < 2.0
    EAEle[3] =   0.143; // 2.0   < eta < 2.2
    EAEle[4] =   0.183; // 2.2   < eta < 2.3
    EAEle[5] =   0.194; // 2.3   < eta < 2.4
    EAEle[6] =   0.261; // 2.4   < eta


  }else if (year.find("2011") != string::npos){
    //combined rel ISO, 2011 Data, 0.5 GeV
    EAMu[0] =   0.132; //         eta < 1.0
    EAMu[1] =   0.120; // 1.0   < eta < 1.5
    EAMu[2] =   0.114; // 1.5   < eta < 2.0
    EAMu[3] =   0.139; // 2.0   < eta < 2.2
    EAMu[4] =   0.168; // 2.2   < eta < 2.3
    EAMu[5] =   0.189; // 2.3   < eta < 2.4

    EAEle[0] =   0.208; //         eta < 1.0
    EAEle[1] =   0.209; // 1.0   < eta < 1.5
    EAEle[2] =   0.115; // 1.5   < eta < 2.0
    EAEle[3] =   0.143; // 2.0   < eta < 2.2
    EAEle[4] =   0.183; // 2.2   < eta < 2.3
    EAEle[5] =   0.194; // 2.3   < eta < 2.4
    EAEle[6] =   0.261; // 2.4   < eta


  }else{
    cerr<<year<<": period != 2011 OR 2012, figure your shit out"<<endl;
    abort();
  }

  // ch      nh       ph
  float EAPhoTemp[7][3] = {
    {0.012,  0.030,   0.148}, //         eta < 1.0
    {0.010,  0.057,   0.130}, // 1.0   < eta < 1.479
    {0.014,  0.039,   0.112}, // 1.479 < eta < 2.0
    {0.012,  0.015,   0.216}, // 2.0   < eta < 2.2
    {0.016,  0.024,   0.262}, // 2.2   < eta < 2.3
    {0.020,  0.039,   0.260}, // 2.3   < eta < 2.4
    {0.012,  0.072,   0.266}  // 2.4   < eta 
  };

  for (unsigned int i =0; i<7; i++){
    for (unsigned int j =0; j<3; j++){
      EAPho[i][j] = EAPhoTemp[i][j];
    }
  }
}




//static const float jetPtCut[] = {30,30}, muPtCut[] = {20,10}, elePtCut[] = {20,10}, gammaPtCut[] = {15./110.,15.}, zMassCut[] = {50,99999.}, metCut[] = {-9999.,9999.},
 // metByQtCut[] = {-999.,999.}, bJetVeto = 9999, qtCut = 0., nJets[] = {0,999}, MassZG[] = {100.,190.}, SumEt = 99999., AngCut = 999,
  //M12Cut = 999999999999999999999, drCut = 0.4, MZpMZGcut = 185, VBFdeltaEta = 3.5, VBFdeltaPhi = 2.4, diJetMassCut = 500, Zeppenfeld = 2.5, R9Cut = 0.94; 


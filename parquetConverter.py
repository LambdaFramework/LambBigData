#!/bin/python

import os
import uproot
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa

import awkward
from array import array
import numpy as np

import time
from timeit import default_timer as timer

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-i", "--inFile", action="store", type="string", dest="inFile", default="")
parser.add_option("-o", "--outFile", action="store", type="string", dest="outFile", default="")
(options, args) = parser.parse_args()

path = os.getcwd()
if len(options.outFile) == 0 or os.path.exists(options.outFile):
    print '--- ERROR ---'
    print '  \''+options.outFile+'\' folder already exists or is null!'
    print '  please delete it or use a different name using option \'-o FOLDER-NAME\''
    print
    exit()
    
os.system('mkdir '+options.outFile)

main=[
    'nElectron',
#    'Electron_deltaEtaSC',
#    'Electron_dr03EcalRecHitSumEt',
#    'Electron_dr03HcalDepth1TowerSumEt',
#    'Electron_dr03TkSumPt',
    'Electron_dxy',
    'Electron_dxyErr',
    'Electron_dxyErr_ugo',
    'Electron_dxy_ugo',
    'Electron_dz',
    'Electron_dzErr',
    'Electron_eCorr',
#    'Electron_eInvMinusPInv',
    'Electron_energyErr',
    'Electron_eta',
#    'Electron_hoe',
    'Electron_ip3d',
    'Electron_ip3d_ugo',
    'Electron_mass',
    'Electron_miniPFRelIso_all',
    'Electron_miniPFRelIso_chg',
#    'Electron_mvaSpring16GP',
#    'Electron_mvaSpring16HZZ',
    'Electron_pfRelIso03_all',
    'Electron_pfRelIso03_chg',
    'Electron_phi',
    'Electron_pt',
#    'Electron_r9',
#    'Electron_sieie',
#    'Electron_sip3d',
#    'Electron_sip3d_ugo',
#    'Electron_mvaTTH',
    'Electron_charge',
    'Electron_jetIdx',
    'Electron_pdgId',
    'Electron_photonIdx',
    'Electron_tightCharge',
#    'Electron_vidNestedWPBitmap',
    'Electron_lostHits',
    'nGenJetAK8',
    'GenJetAK8_eta',
    'GenJetAK8_mass',
    'GenJetAK8_phi',
    'GenJetAK8_pt',
    'nGenJet',
    'GenJet_eta',
    'GenJet_mass',
    'GenJet_phi',
    'GenJet_pt',
    'nGenPart',
    'GenPart_eta',
    'GenPart_mass',
    'GenPart_phi',
    'GenPart_pt',
    'GenPart_genPartIdxMother',
    'GenPart_pdgId',
    'GenPart_status',
    'GenPart_statusFlags',
    'nJet',
    'Jet_area',
    'Jet_btagCMVA',
    'Jet_btagCSVV2',
    'Jet_btagDeepB',
    'Jet_btagDeepC',
    'Jet_chEmEF',
    'Jet_chHEF',
    'Jet_eta',
    'Jet_mass',
    'Jet_neEmEF',
    'Jet_neHEF',
    'Jet_phi',
    'Jet_pt',
    'Jet_qgl',
#    'Jet_rawFactor',
    'Jet_bReg',
    'Jet_electronIdx1',
    'Jet_electronIdx2',
    'Jet_jetId',
    'Jet_muonIdx1',
    'Jet_muonIdx2',
    'Jet_nConstituents',
    'Jet_nElectrons',
    'Jet_nMuons',
    'Jet_puId',
#    'MET_MetUnclustEnUpDeltaX',
#    'MET_MetUnclustEnUpDeltaY',
#    'MET_covXX',
#    'MET_covXY',
#    'MET_covYY',
    'MET_phi',
    'MET_pt',
#    'MET_significance',
    'MET_sumEt',
    'nMuon',
    'Muon_dxy',
    'Muon_dxyErr',
    'Muon_dxyErr_ugo',
    'Muon_dxy_ugo',
    'Muon_dz',
    'Muon_dzErr',
    'Muon_eta',
    'Muon_ip3d',
    'Muon_ip3d_ugo',
    'Muon_mass',
    'Muon_miniPFRelIso_all',
    'Muon_miniPFRelIso_chg',
    'Muon_pfRelIso03_all',
    'Muon_pfRelIso03_chg',
    'Muon_pfRelIso04_all',
    'Muon_phi',
    'Muon_pt',
#    'Muon_ptErr',
#    'Muon_segmentComp',
    'Muon_sip3d',
    'Muon_sip3d_ugo',
#    'Muon_mvaTTH',
    'Muon_charge',
    'Muon_jetIdx',
#    'Muon_nStations',
#    'Muon_nTrackerLayers',
    'Muon_pdgId',
    'Muon_tightCharge',
    'Muon_highPtId',
    'Pileup_nPU',
#    'Pileup_nTrueInt',
    'PuppiMET_phi',
    'PuppiMET_pt',
    'PuppiMET_sumEt',
    'PV_ndof',
    'PV_x',
    'PV_y',
    'PV_z',
#    'PV_chi2',
#    'PV_score',
    'PV_npvs',
    'Electron_genPartIdx',
    'Electron_genPartFlav',
    'GenJetAK8_partonFlavour',
    'GenJetAK8_hadronFlavour',
    'GenJet_partonFlavour',
    'GenJet_hadronFlavour',
    'Jet_genJetIdx',
    'Jet_hadronFlavour',
    'Jet_partonFlavour',
    'Muon_genPartIdx',
    'Muon_genPartFlav',
    'MET_fiducialGenPhi',
    'MET_fiducialGenPt',
#    'Electron_cleanmask',
#    'Jet_cleanmask',
#    'Muon_cleanmask',
]

main1=[
    'Electron_genPartIdx',
    'Electron_genPartFlav',
    'GenJetAK8_partonFlavour',
    'GenJetAK8_hadronFlavour',
    'GenJet_partonFlavour',
    'GenJet_hadronFlavour',
    'Jet_genJetIdx',
    ]

globo=[
    'HLT_Ele25_WPTight_Gsf',
    'HLT_Ele27_eta2p1_WPLoose_Gsf',
    'HLT_Ele105_CaloIdVT_GsfTrkIdT',
    'HLT_IsoMu22',
    'HLT_IsoMu22_eta2p1',
    'HLT_IsoMu24',
    'HLT_IsoTkMu22_eta2p1',
    'HLT_IsoTkMu24',
    'HLT_Mu45_eta2p1',
    'HLT_Mu50',
    #'HLT_PFMET170_NoiseCleaned',
    #'HLT_PFMET170_JetIdCleaned',
    #'HLT_PFMET100_PFMHT100_IDTight',
    #'HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned',
    #'HLT_PFMET110_PFMHT110_IDTight',
    #'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight',
    #'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight',
    #'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight',
    #'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight',
]

lobo= [
    'Muon_mediumId',
    'Muon_softId',
    'Muon_tightId',
#    'Muon_isPFcand',
#    'Electron_convVeto',
#    'Electron_cutBased_HEEP',
#    'Electron_isPFcand',
#    'Electron_mvaSpring16GP_WP80',
#    'Electron_mvaSpring16GP_WP90',
#    'Electron_mvaSpring16HZZ_WPL',
    'Electron_cutBased',
#    'Electron_cutBased_HLTPreSel',
]

def convetq(infile, outfile):

	    openFile= uproot.open("%s" %infile)
            eventTree=openFile["Events"]
	    print "STATUS: Processing root file ", file
            NAME=infile.split('/')[-1].split('.')[0]
            print "NAME = ", NAME
            df1=[]

            #Extract Main scheme
            print "STATUS: Extract Main scheme"
            start = timer()
            #for element in main:
            #            df1.append(pd.DataFrame(pd.Series([x for x in eventTree.arrays("%s" %element)["%s" %element]], name='%s' %element)))
            df1.append(pd.DataFrame(eventTree.arrays(main1)))
            end2 = timer(); print "Exhausted ", (end2 - start)/60, "mins"
            
            #Convert bools JaggedArray into int
            print "STATUS: Convert bools JaggedArray into int JaggedArray"
            for element in lobo:
                        event=[]
                        for jaggedElement in eventTree.arrays("%s" %element)["%s" %element]:
                            eventlet=[]
                            for num,eve in enumerate(jaggedElement):
                                eventlet.append(1*eve)
                            event.append(eventlet)
                        df1.append(pd.DataFrame(pd.Series([x for x in awkward.JaggedArray.fromiter(event)], name='%s' %element)))
            end3 = timer(); print "Exhausted ", (end3 - end2)/60, "mins"
            
            #Convert bools Array into int
            print "STATUS: Convert bools Array into int Array"
            for element in globo:
                df1.append(pd.DataFrame(pd.Series([1*x for x in eventTree.arrays("%s" %element)["%s" %element]], name='%s' %element)))
            end4 = timer(); print "Exhausted ", (end4 - end3)/60, "mins"
            
            #Concatenate all element in DF list
            print "STATUS: Concatenate all element in DF list"
            concat_df = pd.concat(df1)
            end5 = timer(); print "Exhausted ", (end5 - end4)/60, "mins"
            
            #Convert to table
            print "STATUS: Convert to table"
            table = pa.Table.from_pandas(concat_df)
            end6 = timer(); print "Exhausted ", (end6 - end5)/60, "mins"
            
            #SaveAs Parquet
            print "STATUS: SaveAs Parquet"
            pq.write_table(table, '%s/%s.parquet' %(outfile,NAME))
            end7 = timer(); print "Exhausted ", (end7 - end6)/60, "mins"


convetq(options.inFile,options.outFile)

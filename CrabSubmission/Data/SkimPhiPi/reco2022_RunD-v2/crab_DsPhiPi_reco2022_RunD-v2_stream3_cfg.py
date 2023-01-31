from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'SkimDsPhiPi_2022eraD-v2_stream3_Mini_v3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'


config.JobType.psetName = '/lustrehome/aruta/Tau3mu-Run3_Analysis_12_4_11_patch3/CMSSW_12_4_11_patch3/src/SkimTools/SkimPhiPi/test/run_Data2022A-D_DsPhiPiSkimAndTree_cfg.py'

config.Data.inputDataset = '/ParkingDoubleMuonLowMass3/Run2022D-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 50
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraD_357538_357900_Golden.json'
#config.Data.runRange = '193093-193999' # '193093-194075'
config.Data.publication = True
config.Data.outputDatasetTag = 'SkimDsPhiPi_2022eraD-v2_stream3_Mini_v3'
config.JobType.allowUndistributedCMSSW = True 
config.Site.storageSite = 'T2_IT_Bari'
config.Site.ignoreGlobalBlacklist  = True


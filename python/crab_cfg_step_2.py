# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SMS-T1tttt_mglu1500_mlsp100_full-sim_AOD'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-T1tttt_2_AODSIM_cfg.py'

config.JobType.maxJobRuntimeMin = 9*60
config.JobType.maxMemoryMB = 3000

config.section_("Data")


#config.Data.inputDBS = 'global'

#config.Data.userInputFiles = open('List_2_2.txt').readlines()

config.Data.inputDataset = '/T1tttt_mglu1500_mlsp100_full-sim_PREMIX/lwiens-T1tttt_mglu1500_mlsp100_full-sim_Premix-e9ee995e0f1bbd5d8fa8f360f5aa9516/USER'
config.Data.inputDBS = 'phys03'

#config.Data.outputPrimaryDataset = 'SMS-T1tttt_mini'


config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 1#number of files
config.Data.outLFNDirBase = '/store/user/lwiens/SMS-T1tttt_mglu1500_mlsp100_full-sim_AOD'
config.Data.publication = True
config.Data.outputDatasetTag = 'SMS-T1tttt_mglu1500_mlsp100_full-sim_AOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'

# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SMS-T1tttt_mglu1500_mlsp100_full-sim_MiniAOD'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-T1tttt_3_MiniAOD_cfg.py'

config.JobType.maxJobRuntimeMin = 9*60
config.JobType.maxMemoryMB = 3000

config.section_("Data")


#config.Data.inputDBS = 'global'

#config.Data.userInputFiles = open('List_2_2.txt').readlines()

config.Data.inputDataset = '/T1tttt_mglu1500_mlsp100_full-sim_PREMIX/lwiens-SMS-T1tttt_mglu1500_mlsp100_full-sim_AOD-fb69542e14c23bca91d480d54f5291ea/USER'
config.Data.inputDBS = 'phys03'

#config.Data.outputPrimaryDataset = 'SMS-T1tttt_mini'


config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 3
#config.Data.totalUnits = 1#number of files
config.Data.outLFNDirBase = '/store/user/lwiens/SMS-T1tttt_mglu1500_mlsp100_full-sim_MiniAOD'
config.Data.publication = True
config.Data.outputDatasetTag = 'SMS-T1tttt_mglu1500_mlsp100_full-sim_MiniAOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'

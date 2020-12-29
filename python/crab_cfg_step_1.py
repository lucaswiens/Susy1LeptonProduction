# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'T1tttt_mglu1500_mlsp100_full-sim'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SUS-T1tttt_1_PREMIXRAW_cfg.py'

config.JobType.maxJobRuntimeMin = 27*60
config.JobType.maxMemoryMB = 4000


config.section_("Data")
config.Data.inputDBS = 'global'
config.Data.outputPrimaryDataset = 'T1tttt_mglu1500_mlsp100_full-sim_PREMIX'
config.Data.splitting = 'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1000 #number of events per jobs
config.Data.totalUnits = 1000000 #number of event
#config.Data.totalUnits = 10#number of event for testing
config.Data.outLFNDirBase = '/store/user/lwiens/T1tttt_mglu1500_mlsp100_full-sim_PREMIX'
config.Data.publication = True
config.Data.outputDatasetTag = 'T1tttt_mglu1500_mlsp100_full-sim_Premix'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

import math

baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     %MGLU%           # ~g
   1000022     %MLSP%           # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays

DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
DECAY   1000021     1.00000000E+00   # gluino decays
    0.00000000E+00    3    1000022     -1    1 # dummy allowed decay, in order to turn on off-shell decays
    1.00000000E+00    3    1000022     -6    6
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.00000000E+00   # neutralino2 decays
DECAY   1000024     0.00000000E+00   # chargino1+ decays
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

model = "T1tttt"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.260

# Number of events: min(xfactor*xsec*ifb, maxEvents) (always in thousands)
ifb, xfactor, maxEvents, minLumi = 20, 40, 150, 45

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
    def __init__(self, xmin, xmax, xstep, ystep, maxDM, dstep, minEvents):
        self.xmin = xmin
        self.xmax = xmax
        self.xstep = xstep
        self.ystep = ystep
        self.maxDM = maxDM
        self.dstep = dstep
        self.minEvents = minEvents

# Fit to gluino cross-section in fb
def xsec(mass):
    return 4.563e+17*math.pow(mass, -4.761*math.exp(5.848e-05*mass))

def matchParams(mass):
    if   mass<799: return 118., 0.235
    elif mass<999: return 128., 0.235
    elif mass<1199: return 140., 0.235
    elif mass<1399: return 143., 0.245
    elif mass<1499: return 147., 0.255
    elif mass<1799: return 150., 0.267
    elif mass<2099: return 156., 0.290
    elif mass<2301: return 160., 0.315
    elif mass<2601: return 162., 0.340
    elif mass<2851: return 168, 0.364
    else: return 160., 0.315

# Number of events for mass point, in thousands
def events(mass):
    xs = xsec(mass)
    nev = min(xfactor*xs*ifb, maxEvents*1000)
    if nev < xs*minLumi: nev = xs*minLumi
    nev = max(nev/1000, minEvents)
    return math.ceil(nev) # Rounds up

# Parameters to define the grid
ymin = 0
scanBlocks = []
scanBlocks.append(gridBlock(600,  1200, 100, 100, 1000, 50, 10))
scanBlocks.append(gridBlock(1200, 2801, 50, 100, 1000, 50, 20))
minDM = 225
ymin, ymed, ymax = 0, 300, 1600

cols = []
xmin, xmax = 9999, 0
for block in scanBlocks:
    minEvents = block.minEvents
    for mx in range(block.xmin, block.xmax, block.dstep):
        xmin = min(xmin, block.xmin)
        xmax = max(xmax, block.xmax)
        col = []
        my = 0
        begDiag = max(ymed, mx-block.maxDM)
        # Adding bulk points
        if (mx-block.xmin)%block.xstep == 0 :
            for my in range(ymin, begDiag, block.ystep):
                if my > ymax: continue
                nev = events(mx)
                col.append([mx,my, nev])
        # Adding diagonal points
        for my in range(begDiag, mx-minDM+1, block.dstep):
            if my > ymax: continue
            nev = events(mx)
            col.append([mx,my, nev])
        if(my !=  mx-minDM and mx-minDM <= ymax):
            my = mx-minDM
            nev = events(mx)
            col.append([mx,my, nev])
        cols.append(col)

mpoints = []
for col in cols: mpoints.extend(col)

for point in mpoints:
    mglu, mlsp = point[0], point[1]
    if mglu != 1500:
    	continue
    if mlsp != 100:
    	continue
    qcut, tru_eff = matchParams(mglu)
    wgt = point[2]*(mcm_eff/tru_eff)

    if mlsp==0: mlsp = 1
    slhatable = baseSLHATable.replace('%MGLU%','%e' % mglu)
    slhatable = slhatable.replace('%MLSP%','%e' % mlsp)

    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP2SettingsBlock,
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = %.0f' % qcut, #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            '6:m0 = 172.5',
            'Check:abortIfVeto = on',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP2Settings',
                                    'JetMatchingParameters'
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-GlGl/v1/SMS-GlGl_mGl-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % mglu),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mglu, mlsp)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )

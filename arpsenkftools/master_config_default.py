"""
master_config.py -- Contains parameters to configure an end-to-end ARPS-EnKF run
"""
import os
from datetime import datetime, timedelta

# Define needed directories and experiment names/tags
# Base project names and directories
scratch_base_dir = '/scratch/rice/d/dawson29'
depot_base_dir = '/depot/dawson29'
arpsenkftools_base_dir = os.path.join(depot_base_dir, 'apps/Projects/arpsEnKFtools')
project_dir = 'Projects/VORTEXSE/simulations/ARPS'
project_scr_dir = os.path.join(scratch_base_dir, project_dir)
project_depot_dir = os.path.join(depot_base_dir, 'data', project_dir)
IOP_name = '2017_IOP4C'
IOP_scr_dir = os.path.join(project_scr_dir, IOP_name, 'EnKF')
IOP_depot_dir = os.path.join(project_depot_dir, IOP_name, 'EnKF')
icbc_scr_dir = os.path.join(IOP_scr_dir, 'icbc')
ext_model_data_dir = os.path.join(depot_base_dir, 'data/Projects/VORTEXSE/model_data/nam_data',
                                  IOP_name)

# Experiment name and directories
exp_name_base = '6km303x303_043017'
exp_name_tag = '_NAM'
exp_name = exp_name_base + exp_name_tag
template_base_dir = os.path.join(arpsenkftools_base_dir, 'template')
template_exp_dir = os.path.join(template_base_dir, exp_name)

# Executable file names and directories
arps_base_dir = '/home/dawson29/arps5.4_main'
arps_bin_dir = os.path.join(arps_base_dir, 'bin')
arpstrn_exe_path = os.path.join(arps_bin_dir, 'arpstrn')
arpssfc_exe_path = os.path.join(arps_bin_dir, 'arpssfc')
ext2arps_exe_path = os.path.join(arps_bin_dir, 'ext2arps')
arps_exe_path = os.path.join(arps_bin_dir, 'arps_mpi')
arpsenkf_exe_path = os.path.join(arps_bin_dir, 'arpsenkf_mpi')
arpsenkfic_exe_path = os.path.join(arps_bin_dir, 'arpsenkfic')
wrf2arps_exe_path = os.path.join(arps_bin_dir, 'wrf2arps_mpi')
arpsintrp_exe_path = os.path.join(arps_bin_dir, 'arpsintrp_mpi')

# Experiment parameters (many of these are namelist parameters that will be inserted in the
# appropriate namelist input files for the various ARPS programs used in an experiment). See the
# documentation in the various namelist input files for details on their meanings.

# Basic experiment parameters
num_ensemble_members = 40
# Initial time of entire experiment
initial_time = '201704300600'
initial_datetime = datetime.strptime(initial_time, '%Y%m%d%H%M')
# Initial time in seconds from model start corresponding to initial_time (can be different from 0
# if ext2arps/wrf2arps/arpsintrp is run to produce IC's for several different times)
initial_time_sec = 0
external_run_name = '6km303x303_043017_NAM_icbc'

# ARPS comment_lines namelist parameters
nocmnt = 2
comments = ['ARPS 5.4', 'April 30th, 2017 VORTEX-SE IOP4C']

# Grid and map projection parameters
nx = 303
ny = 303
nz = 53
dx = 6000.0
dy = 6000.0
ctrlat = 34.80
ctrlon = -87.68
mapproj = 2
trulat1 = 33.0
trulat2 = 36.0

# ARPSTRN parameters (note that this is set to use the 30-s terrain data. Will add hooks
# for the other terrain data source options later)
trndataopt = 3
dir_trndata = os.path.join(depot_base_dir, 'data/arpstopo30.data')
nsmth = 2
lat_sample = 180
lon_sample = 180
trnanxopt = 2
arpstrn_output_dir = os.path.join(project_depot_dir, 'trndata')
terndmp = 3

# ARPSSFC parameters
nstyp = 3
sfcdmp = 3
schmopt = 3
sdatopt = 1
fstypfl = os.path.join(depot_base_dir, 'data/arpssfc.data/soil_1km.data')
bstypfl = os.path.join(depot_base_dir, 'data/arpssfc.data/whsoil_1deg.data')

vdatopt = 1
fvtypfl = os.path.join(depot_base_dir, 'data/arpssfc.data/naoge1_01l_1km.img')
bvtypfl = os.path.join(depot_base_dir, 'data/arpssfc.data/owe14d_10min.data')

ndatopt = 1
fndvifl = os.path.join(depot_base_dir, 'data/arpssfc.data/namar93ndl_1km.img')
bndvifl = os.path.join(depot_base_dir, 'data/arpssfc.data/ndvi9003_10min.data')

vfrcopt = 1
vfrcdr = os.path.join(depot_base_dir, 'data/arpssfc.data/')

nsmthsl = 3
stypout = 1
vtypout = 1
laiout = 1
rfnsout = 1
vegout = 1
ndviout = 1

arpssfc_output_dir = os.path.join(project_depot_dir, 'sfcdata')

# EXT2ARPS parameters
ext2arps_initime = initial_datetime.strftime('%Y-%m-%d.%H:%M:00')
dmp_out_joined = 1,
hdmpfmt = 3,
hdfcompr = 2,
exbcdmp = 3,
exbchdfcompr = 2
extdadmp = 1
qcexout = 1
qrexout = 1
qiexout = 1
qsexout = 1
qhexout = 1
qgexout = 1
nqexout = 1
zqexout = 1
ext2arps_output_dir = os.path.join(IOP_depot_dir, exp_name+'_icbc')
ternopt = 2
terndta = os.path.join(arpstrn_output_dir, exp_name + '.trndata')
ternfmt = 3
extdopt = 116
extdfmt = 3
dir_extd = ext_model_data_dir
extdname = 'nam_218'
nextdfil = 18
# Note, for now explicitly list each time string here. We can work on a more
# compact solution later
extdtimes = [
    '2017-04-30.06:00:00+000:00:00',
    '2017-04-30.06:00:00+001:00:00',
    '2017-04-30.06:00:00+002:00:00',
    '2017-04-30.06:00:00+003:00:00',
    '2017-04-30.06:00:00+004:00:00',
    '2017-04-30.06:00:00+005:00:00',
    '2017-04-30.12:00:00+000:00:00',
    '2017-04-30.12:00:00+001:00:00',
    '2017-04-30.12:00:00+002:00:00',
    '2017-04-30.12:00:00+003:00:00',
    '2017-04-30.12:00:00+004:00:00',
    '2017-04-30.12:00:00+005:00:00',
    '2017-04-30.18:00:00+000:00:00',
    '2017-04-30.18:00:00+001:00:00',
    '2017-04-30.18:00:00+002:00:00',
    '2017-04-30.18:00:00+003:00:00',
    '2017-04-30.18:00:00+004:00:00',
    '2017-04-30.18:00:00+005:00:00',
]
iorder = 3
intropt = 1
nsmooth = 1
exttrnopt = 2
extntmrg = 12
extsfcopt = 0
ext_lbc = 1
ext_vbc = 1
grdbasopt = 1
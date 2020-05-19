# The directory swift_bat has the Chandra and Swift/BAT pha, arf, rmf files for the following object:
[SWIFT J1708.6+2155](https://swift.gsfc.nasa.gov/results/bs105mon/862)
# The sherpa script is A2_wstat_pexmon.py and the same code is present in the fit_chandra_swift_bat notebook

You can set the following flags in the code to choose the model you want:

#Using Pexrav model 
use_pexrav=1

#Using Pexrav model with a gaussian line added at 6.4keV
use_pexrav_with_line=0

#Using Pexmon model with initial parameters obtained from fitting the Pexrav model
use_pexmon=0

#Using Pexmon model with no BB component and with initial parameters obtained from fitting the Pexrav model 
use_pexmon_no_bb_model=0

#Using Pexmon model with initial parameters obtained from fitting the Pexrav model with constraints on the BB temperature
use_pexmon_with_bb_constrained_values=0

#UUsing Pexmon model with no BB with initial parameters obtained from fitting the Pexrav model with constraints on the BB temperature
use_pexmon_with_no_bb_using_bb_constrained_values=0




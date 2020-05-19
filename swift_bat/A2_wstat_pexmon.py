
##load data
load_pha(1,"spec.pi")
group_counts(1,20) 
ignore(None, 0.3)
ignore(7, None)
subtract(1) 

##load data
load_pha(2,"bat_index_862.pha",use_errors=True)
er=get_data(2).staterror*get_exposure(2) 
get_data(2).staterror=er



load_rmf(2,"swiftbat_survey_full.rsp")
#subtract()   
#set_ylog()


set_method("simplex")

#
use_pexmon=0


#
use_pexmon_with_bb_constrained_values=0

#
use_pexrav=0

#
use_pexrav_no_line=1

#
use_pexmon_no_bb_model=0

#
use_pexmon_with_no_bb_using_bb_constrained_values=0

if((use_pexmon) or (use_pexmon_with_bb_constrained_values)):
	set_source(1,xsphabs.abs_gal  *xsconstant.chandra_const * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon + bbody.bb))
	set_source(2,xsphabs.abs_gal  *xsconstant.bat_const * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon + bbody.bb))

if((use_pexmon_no_bb_model) or (use_pexmon_with_no_bb_using_bb_constrained_values)):
	set_source(1,xsphabs.abs_gal  *xsconstant.chandra_const * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon))
	set_source(2,xsphabs.abs_gal  *xsconstant.bat_const * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon))

if(use_pexrav):
	set_source(1,xsphabs.abs_gal  *xsconstant.chandra_const * xscabs.cabs * xszphabs.abs_intr * (xspexrav.pexrav + bbody.bb + xszgauss.line))
	set_source(2,xsphabs.abs_gal  *xsconstant.bat_const * xscabs.cabs * xszphabs.abs_intr * (xspexrav.pexrav + bbody.bb + xszgauss.line))
	print ("Equi Width")
	print(eqwidth(abs_gal  * bat_const * cabs * abs_intr * (pexrav + bb),abs_gal  * bat_const * cabs * abs_intr * (pexrav + bb + line),lo=6.2,hi=6.6,id=1))


if(use_pexrav_no_line):
	set_source(1,xsphabs.abs_gal  *xsconstant.chandra_const * xscabs.cabs * xszphabs.abs_intr * (xspexrav.pexrav + bbody.bb))
	set_source(2,xsphabs.abs_gal  *xsconstant.bat_const * xscabs.cabs * xszphabs.abs_intr * (xspexrav.pexrav + bbody.bb))

print ("ORIGINAL MODEL!")
#show_model()

#set parameters
abs_gal.nH = 0.02
freeze(abs_gal.nH)
cabs.nH = 0.02
#freeze(cabs.nH)

#abs_intr.nH = 0.02
link(cabs.nH , abs_intr.nH)

#freeze(abs_intr.nH)
abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)

if(use_pexmon) or (use_pexmon_with_bb_constrained_values) or (use_pexmon_no_bb_model) or (use_pexmon_with_no_bb_using_bb_constrained_values):
        pexmon.redshift = 0.0728
        freeze(pexmon.redshift)
        pexmon.Incl = 30 # cos 30 deg
        freeze(pexmon.Incl)

if(use_pexmon):
	set_par(pexmon.PhoIndex, val =  1.40855, min = 0, max = 3, frozen=False)
	set_par(pexmon.foldE, val = 150.269, min = 60, max = 500, frozen=False)
	set_par(pexmon.rel_refl, val = 0.308955, min = 0, max = 20, frozen=False)
	set_par(pexmon.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)

if(use_pexmon_with_bb_constrained_values):
	set_par(pexmon.PhoIndex, val =  1.34105, min = 0, max = 3, frozen=False)
	set_par(pexmon.foldE, val = 60.0002, min = 60, max = 500, frozen=False)
	set_par(pexmon.rel_refl, val = 0.029912, min = 0, max = 20, frozen=False)
	set_par(pexmon.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
	set_par(bb.kT, val = 0.102192, min = 0, max = 2, frozen=False)

if(use_pexmon_no_bb_model):
	set_par(pexmon.PhoIndex, val =  1.40855, min = 0, max = 3, frozen=False)
	set_par(pexmon.foldE, val = 150.269 , min = 60, max = 500, frozen=False)
	set_par(pexmon.rel_refl, val = 0.308955, min = 0, max = 20, frozen=False)
	set_par(pexmon.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)

if(use_pexmon_with_no_bb_using_bb_constrained_values):
	set_par(pexmon.PhoIndex, val =  1.34105, min = 0, max = 3, frozen=False)
	set_par(pexmon.foldE, val = 60.0002, min = 60, max = 500, frozen=False)
	set_par(pexmon.rel_refl, val = 0.029912, min = 0, max = 20, frozen=False)
	set_par(pexmon.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)


if(use_pexrav) or (use_pexrav_no_line):
	pexrav.redshift = 0.0728
	freeze(pexrav.redshift)
	pexrav.cosIncl = 0.8660254 # cos 30 deg

if(use_pexrav):
	line.LineE = 6.4
	freeze(line.LineE)
	line.sigma = 0.1
	freeze(line.sigma)
	line.redshift = 0.0728
	freeze(line.redshift)
	set_par(line.norm, val = 1e-11, min = 0, max = 1e-2, frozen=False)
	
	set_par(pexrav.PhoIndex, val = 1.4085, min = 0, max = 3, frozen=True)
	set_par(pexrav.foldE, val = 150.269, min = 60, max = 500, frozen=True)
	set_par(pexrav.rel_refl, val = 0.308955, min = 0, max = 20, frozen=True)
	set_par(pexrav.norm, val = 0.00021, min = 0, max = 0.1, frozen=True)
	set_par(bb.kT, val = 0.1, min = 0, max = 2, frozen=False)

if(use_pexrav_no_line):
	set_par(pexrav.PhoIndex, val = 1.63, min = 0, max = 3, frozen=False)
	set_par(pexrav.foldE, val = 60, min = 60, max = 500, frozen=False)
	set_par(pexrav.rel_refl, val = 1, min = 0, max = 20, frozen=False)
	set_par(pexrav.norm, val = 0.001, min = 0, max = 0.1, frozen=False)
	#set_par(bb.kT, val = 0.1, min = 0, max = 2, frozen=False)

set_par(chandra_const.factor, val = 1,frozen=True)
set_par(bat_const.factor, val = 1.1, min = 1, max = 10000, frozen=False)


print ("AFTER FREEZE!")
#show_model()

if(use_pexmon) or (use_pexmon_with_bb_constrained_values) or (use_pexmon_no_bb_model) or (use_pexmon_with_no_bb_using_bb_constrained_values):
	guess(pexmon)
if(use_pexrav) or (use_pexrav_no_line):
	guess(pexrav)

print ("AFTER GUESS!")
#show_model()

#set_stat("wstat")
set_stat('chi2datavar')


fit(1,2)

print ("AFTER FIT!")
show_model()
#conf()
#print("CALC CHI SQUARE")
#calc_chisqr(1,2)
#show_stat()




gen_together = 0
data2_fit = 0


if(gen_together == 0):
	plot_fit_delchi(1)
	#plot("fit",1,"fit",2)



if(gen_together == 1):
	plot_fit(1)
	if(data2_fit == 1):
		plot_fit(2,overplot=True)
	else:
		plot_data(2,overplot=True)
		plot_model(2,overplot=True)




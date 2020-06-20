##load data
load_pha(1,"interval0pc_binned.pi")
#group_counts(1,10) 
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(1) 

##load data
load_pha(2,"bat_index_862.pha",use_errors=True)
er=get_data(2).staterror*get_exposure(2) 
get_data(2).staterror=er

load_rmf(2,"swiftbat_survey_full.rsp")  
#set_ylog()

#set_method("moncar")
set_method("simplex")

#Using Pexrav model 

set_source(1,xsphabs.abs_gal  * xsconstant.xrt_const *  xszphabs.abs_intr * xscabs.cabs * (xspexrav.pexrav + xsbbody.bb))
set_source(2,xsphabs.abs_gal  * xsconstant.bat_const *  xszphabs.abs_intr * xscabs.cabs * (xspexrav.pexrav + xsbbody.bb))

#set parameters
abs_gal.nH = 0.02
freeze(abs_gal.nH)
cabs.nH = 0.01
abs_intr.nH = 0.01
link(cabs.nH, abs_intr.nH)


abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)

pexrav.redshift = 0.0728
freeze(pexrav.redshift)
pexrav.cosIncl = 0.8660254 # cos 30 deg
freeze(pexrav.cosIncl)

set_par(pexrav.PhoIndex, val = 1.63, min = 0, max = 3, frozen=False)
set_par(pexrav.foldE, val = 60, min = 0, max = 500, frozen=False)
set_par(pexrav.rel_refl, val = 0.7, min = 0, max = 1, frozen=False)
set_par(pexrav.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
set_par(bb.kT, val = 0.09, min = 0, max = 2, frozen=False)
	
set_par(xrt_const.factor, val = 1,frozen=True)
set_par(bat_const.factor, val = 1.1, min = 1, max = 2, frozen=False)


guess(pexrav)

#set_stat("wstat")
set_stat('chi2datavar')

fit(1,2)


print ("AFTER FIT!")
show_model()
print(get_fit_results())
conf()
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


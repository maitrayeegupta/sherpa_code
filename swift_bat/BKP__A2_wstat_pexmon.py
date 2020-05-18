
##load data
load_pha(1,"spec.pi")
group_counts(1,20) 
subtract(1) 

##load data
load_pha(2,"bat_index_862.pha")

load_rmf(2,"swiftbat_survey_full.rsp")
#subtract()   
show_data(2)
set_ylog()


set_method("simplex")

Cbat=1.1
Cbat_large = 1.1
#A2
set_source(1,xsphabs.abs_gal  *Cbat * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon + bbody.bb))
set_source(2,xsphabs.abs_gal  *Cbat_large * xscabs.cabs * xszphabs.abs_intr * (xspexmon.pexmon + bbody.bb))
print ("ORIGINAL MODEL!")
#show_model()

##set parameters
abs_gal.nH = 0.02
freeze(abs_gal.nH)
cabs.nH = 0.02
freeze(cabs.nH)
abs_intr.nH = 0.02
freeze(abs_intr.nH)
abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)


pexmon.redshift = 0.0728
freeze(pexmon.redshift)
#pexmon.PhoIndex = 1.64


set_par(pexmon.PhoIndex, val = 1.64, min = 1, max = 2, frozen=False)
set_par(pexmon.foldE, val = 100, min = 50, max = 150, frozen=False)
set_par(pexmon.rel_refl, val = -1, min = -20, max = 0, frozen=False)

pexmon.norm = 0.0001
pexmon.Incl = 30 # cos 30 deg
freeze(pexmon.Incl)

print ("AFTER FREEZE!")
#show_model()

guess(pexmon)

print ("AFTER GUESS!")
#show_model()

#set_stat("wstat")
#set_stat("cstat")


fit(1,2)

print ("AFTER FIT!")
show_model()

#calc_chisqr()


gen_together = 0
data2_fit = 1

if(gen_together == 0):
	plot("fit",1,"fit",2)



if(gen_together == 1):
	plot_fit(1)
	if(data2_fit == 1):
		plot_fit(2,overplot=True)
	else:
		plot_data(2,overplot=True)
		plot_model(2,overplot=True)




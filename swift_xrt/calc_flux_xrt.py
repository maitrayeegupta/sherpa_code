load_pha(1,"interval0pc.pi")
group_counts(1,5) 
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(1) 

set_method("simplex")
#set_source(1,xsphabs.abs_gal  *powlaw1d.p1)
set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
#set_source(1,powlaw1d.p1)

#set_par(p1.gamma, val = 1.53535, min = 1.4851437, max = 1.5855563, frozen=False)
#set_par(p1.ampl, val = 0.000571162, min = 0.0005487586, max = 0.00057340234, frozen=False)

abs_gal.nH = 0.02
freeze(abs_gal.nH)

abs_intr.nH = 0.02
abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)

set_stat('chi2datavar')

fit(1)
energy = calc_energy_flux(0.3,7)  
print ("energy flux =",energy)
plot_fit_delchi(1)
#sample_flux(p1,0.3,7,num=1000)



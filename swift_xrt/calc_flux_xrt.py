load_pha(1,"interval0pc_binned.pi")
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(1) 

set_method("simplex")
#set_source(1,xsphabs.abs_gal * powlaw1d.p1)
#set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
set_source(1,powlaw1d.p1)

set_par(p1.gamma, val = 1.6509, min = 1.5973354, max = 1.7044646, frozen=False)
set_par(p1.ampl, val = 0.00072687, min = 0.000699047, max = 0.000754693, frozen=False)

#set_par(p1.gamma, val = 1.63, min = 0, max = 2, frozen=False)
#set_par(p1.ampl, val = 0.000166237, min = 0 , max = 0.2, frozen=False)

#abs_gal.nH = 0.053
#freeze(abs_gal.nH)


set_stat('chi2datavar')

fit(1)
conf()
energy = calc_energy_flux(0.3,7)  
print ("calc energy flux =",energy)
plot_fit_delchi(1)
sample_flux(p1,0.3,7,num=1000)






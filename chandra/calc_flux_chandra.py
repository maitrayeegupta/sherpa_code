load_pha(1,"spec_binned.pi")
#group_counts(1,5)
ignore(None, 0.3)
ignore(7, None)
subtract(1)


set_method("simplex")
#set_source(1,xsphabs.abs_gal  *powlaw1d.p1)
#set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
set_source(1,powlaw1d.p1)

set_pileup_model(1,jdpileup.jdp)

set_par(jdp.alpha, val = 0.5, min = 0, max = 1, frozen=False)
set_par(jdp.g0, val = 1, frozen=True)
set_par(jdp.f, val = 0.95, frozen=True)
set_par(jdp.n, val = 1, frozen=True)
set_par(jdp.ftime, val = 0.4, frozen=True)
set_par(jdp.fracexp, val = 1, frozen=True)
set_par(jdp.nterms, val = 30, frozen=True)


set_par(p1.gamma, val = 1.18874, min = 1.1589404, max = 1.2184707, frozen=False)
set_par(p1.ampl, val = 0.000166237, min = 0.0001616978 , max = 0.0001707812, frozen=False)

#abs_gal.nH = 0.02
#freeze(abs_gal.nH)

#abs_intr.nH = 0.02
#abs_intr.redshift = 0.0728
#freeze(abs_intr.redshift)

set_stat('chi2datavar')
#set_stat('cash')

fit(1)
conf()
energy = calc_energy_flux(0.3,7)  
sample_flux(p1,0.3,7,num=1000)
print ("calc_energy flux =",energy)
plot_fit_delchi(1)


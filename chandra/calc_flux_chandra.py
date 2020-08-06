load_pha(1,"spec_binned.pi")
#group_counts(1,5)
ignore(None, 0.3)
ignore(7, None)
subtract(1)


set_method("simplex")
#set_source(1,xstbabs.abs_gal  *powlaw1d.p1)
#set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
set_source(1,powlaw1d.p1)

set_pileup_model(1,jdpileup.jdp)

set_par(jdp.alpha, val = 1.98124e-06, frozen=True)
set_par(jdp.g0, val = 1, frozen=True)
set_par(jdp.f, val = 0.95, frozen=True)
set_par(jdp.n, val = 1, frozen=True)
set_par(jdp.ftime, val = 0.4, frozen=True)
set_par(jdp.fracexp, val = 1, frozen=True)
set_par(jdp.nterms, val = 30, frozen=True)


set_par(p1.gamma, val = 1.27783, min = 1.2462517, max = 1.313404, frozen=False)
set_par(p1.ampl, val = 0.000184645, min = 0.00017951203 , max = 0.00018981314, frozen=False)

#set_par(p1.gamma, val = 1.63, min = 0, max = 2, frozen=False)
#set_par(p1.ampl, val = 0.000166237, min = 0 , max = 0.2, frozen=False)

#abs_gal.nH = 0.053
#freeze(abs_gal.nH)



set_stat('chi2datavar')
#set_stat('cash')

fit(1)
conf()
energy = calc_energy_flux(0.3,7)  
sample_flux(p1,0.3,7,num=1000)
print ("calc_energy flux =",energy)
plot_fit_delchi(1)


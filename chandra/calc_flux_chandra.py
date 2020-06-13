load_pha(1,"spec.pi")
group_counts(1,5)
ignore(None, 0.3)
ignore(7, None)
subtract(1)


set_method("simplex")
#set_source(1,xsphabs.abs_gal  *powlaw1d.p1)
set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
#set_source(1,powlaw1d.p1)


#set_par(p1.gamma, val = 1.22827, min = 1.1982, max = 1.2583, frozen=False)
#set_par(p1.ampl, val = 0.000153303, min = 0.000149193, max = 0.0001574133, frozen=False)

abs_gal.nH = 0.02
freeze(abs_gal.nH)

abs_intr.nH = 0.02
abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)

set_stat('chi2datavar')
#set_stat('cash')

fit(1)
energy = calc_energy_flux(0.3,7)  
print ("energy flux =",energy)
plot_fit_delchi(1)


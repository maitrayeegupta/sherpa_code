load_pha(1,"extract_new/spec_binned.pi")
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(1) 

set_method("simplex")
set_source(1,xsphabs.abs_gal * powlaw1d.p1)
#set_source(1,xsphabs.abs_gal *xszphabs.abs_intr *powlaw1d.p1)
#set_source(1,powlaw1d.p1)

set_par(p1.gamma, val = 1.28, min = 1.25, max = 1.32, frozen=False)
set_par(p1.ampl, val = 1.84e-4, min = 1.7887e-4, max = 1.8917e-4, frozen=False)

#set_par(p1.gamma, val = 1.63, min = 0, max = 2, frozen=False)
#set_par(p1.ampl, val = 0.000166237, min = 0 , max = 0.2, frozen=False)

abs_gal.nH = 0.053
freeze(abs_gal.nH)

add_pileup_model=1
if(add_pileup_model):
    set_pileup_model(1,jdpileup.jdp)
    set_par(jdp.alpha, val = 0.5, min = 0, max = 1, frozen=False)
    set_par(jdp.g0, val = 1, frozen=True)
    set_par(jdp.f, val = 0.95, frozen=True)
    set_par(jdp.n, val = 1, frozen=True)
    set_par(jdp.ftime, val = 0.4, frozen=True)
    set_par(jdp.fracexp, val = 1, frozen=True)
    set_par(jdp.nterms, val = 30, frozen=True)


set_stat('chi2datavar')

fit(1)
conf()
energy = calc_energy_flux(0.3,7)  
print ("calc energy flux =",energy)
plot_fit_delchi(1)
sample_flux(p1,0.3,7,num=1000)






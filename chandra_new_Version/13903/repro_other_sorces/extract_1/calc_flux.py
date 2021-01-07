from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")


##load Chandra data
ui.load_pha(1,"spec_binned.pi")
#group_counts(1,5)
ui.ignore(None, 0.3)
ui.ignore(7, None)
#ui.ignore_bad()
ui.subtract(1)


ui.set_method("simplex")


#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))

ui.set_source(1,ui.xstbabs.abs_gal  * ui.powlaw1d.p1 )



#set parameters
abs_gal.nH = 0.053
ui.freeze(abs_gal.nH)
#cabs.nH = 0.0
#abs_intr.nH = 0.0


ui.set_par(p1.gamma, val = 1.63, min = 0, max = 5, frozen=False)
print("HERE!!1")


add_pileup_model=1
if(add_pileup_model):
    ui.set_pileup_model(1,ui.jdpileup.jdp)
    ui.set_par(jdp.alpha, val = 0.5, min = 0, max = 1, frozen=False)
    ui.set_par(jdp.g0, val = 1, frozen=True)
    ui.set_par(jdp.f, val = 0.95, frozen=True)
    ui.set_par(jdp.n, val = 1, frozen=True)
    ui.set_par(jdp.ftime, val = 0.4, frozen=True)
    ui.set_par(jdp.fracexp, val = 1, frozen=True)
    ui.set_par(jdp.nterms, val = 30, frozen=True)


print("HERE!!2")
ui.plot_data(1)

print("HERE!!3")
ui.set_stat('chi2datavar')
print("HERE!!4")
ui.fit(1)
print("HERE!!5")

#ui.show_model()

energy = ui.calc_energy_flux(0.3,7)  
print ("energy flux =",energy)


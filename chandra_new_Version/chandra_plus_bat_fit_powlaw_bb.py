from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")


##load Chandra data
ui.load_pha(1,"extract_new/spec_binned.pi")
#group_counts(1,5)
ui.ignore(None, 0.3)
ui.ignore(7, None)
#ui.ignore_bad()
ui.subtract(1)

##load BAT data
##load data
ui.load_pha(2,"bat_index_862.pha",use_errors=True)
er=ui.get_data(2).staterror*ui.get_exposure(2) 
ui.get_data(2).staterror=er
ui.load_rmf(2,"swiftbat_survey_full.rsp")

ui.set_method("simplex")


#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))

ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))
ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))


#set parameters
abs_gal.nH = 0.053
ui.freeze(abs_gal.nH)
#cabs.nH = 0.0
#abs_intr.nH = 0.0


ui.set_par(p1.gamma, val = 1.63, min = 0, max = 2, frozen=False)
ui.set_par(bb.kT, val = 0.09, min = 0, max = 1, frozen=False)
ui.set_par(bb.norm, val = 0.000001, min = 0, max = 1, frozen=False)
ui.set_par(chandra_const.factor, val = 1,frozen=True)
ui.set_par(bat_const.factor, val = 1.1, min = 1, max = 2, frozen=False)


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

ui.plot_data(1)

ui.set_stat('chi2datavar')
ui.fit(1,2)
conf()

#ui.show_model()

ui.plot_fit_delchi(1)

energy = ui.calc_energy_flux(0.3,7)  
print ("energy flux =",energy)


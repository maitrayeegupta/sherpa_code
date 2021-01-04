from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")


##load Chandra data
ui.load_pha(1,"extract_new/spec_binned.pi")
#group_counts(1,5)
ui.ignore(None, 0.3)
ui.ignore(7, None)
ui.subtract(1)

##load BAT data
##load data
ui.load_pha(2,"../swift_xrt/bat_index_862.pha",use_errors=True)
er=ui.get_data(2).staterror*ui.get_exposure(2) 
ui.get_data(2).staterror=er
ui.load_rmf(2,"../swift_xrt/swiftbat_survey_full.rsp")

ui.set_method("simplex")


#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))

ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))
ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))


#set parameters
abs_gal.nH = 0.053
ui.freeze(abs_gal.nH)
#cabs.nH = 0.0
#abs_intr.nH = 0.0

#ui.freeze(cabs.nH)
#ui.freeze(abs_intr.nh)

#abs_intr.redshift = 0.0728
#ui.freeze(abs_intr.redshift)

pexrav.redshift = 0.0728
ui.freeze(pexrav.redshift)
pexrav.cosIncl = 0.8660254 # cos 30 deg
ui.freeze(pexrav.cosIncl)

ui.set_par(pexrav.PhoIndex, val = 1.63, min = 0, max = 2, frozen=False)
ui.set_par(pexrav.foldE, val = 60, min = 0, max = 200, frozen=False)
ui.set_par(pexrav.rel_refl, val = 0.7, min = 0, max = 1, frozen=False)
ui.set_par(pexrav.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
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


#ui.show_model()
conf()
ui.plot_fit_delchi(1)

energy = ui.calc_energy_flux(0.3,7)  
print ("energy flux =",energy)


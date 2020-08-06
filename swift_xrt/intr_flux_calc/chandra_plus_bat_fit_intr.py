from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")


##load Chandra data
ui.load_pha(1,"../../chandra/spec_binned.pi")
#group_counts(1,5)
ui.ignore(None, 0.3)
ui.ignore(7, None)
ui.subtract(1)

##load BAT data
##load data
ui.load_pha(2,"../bat_index_862.pha",use_errors=True)
er=ui.get_data(2).staterror*ui.get_exposure(2) 
ui.get_data(2).staterror=er
ui.load_rmf(2,"../swiftbat_survey_full.rsp")

ui.set_method("simplex")


#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))

#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))

ui.set_source(1, ui.xsconstant.chandra_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))
ui.set_source(2, ui.xsconstant.bat_const * (ui.xspexrav.pexrav + ui.xsbbody.bb))


#set parameters
#abs_gal.nH = 0.053
#ui.freeze(abs_gal.nH)
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


ui.set_par(pexrav.PhoIndex, val =  1.22532, min= 1.22531 ,max = 1.22533 , frozen=False)
ui.set_par(pexrav.foldE, val = 49.3027, frozen=True)
ui.set_par(pexrav.rel_refl, val = 4.69068e-07, frozen=True)
ui.set_par(pexrav.norm, val = 0.000183665, frozen=True)
ui.set_par(bb.kT, val = 0.0461419, frozen=True)
ui.set_par(bb.norm, val = 3.07098e-06, frozen=True)
ui.set_par(chandra_const.factor, val =1,  frozen=True)
ui.set_par(bat_const.factor, val = 1.01017,  frozen=True)


add_pileup_model=1
if(add_pileup_model):
    ui.set_pileup_model(1,ui.jdpileup.jdp)
    ui.set_par(jdp.alpha, val = 1.86496e-06, min = 0, max = 1, frozen=True)
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

ui.plot_fit_delchi(1)

energy = ui.calc_energy_flux(0.3,7)  
print ("energy flux =",energy)






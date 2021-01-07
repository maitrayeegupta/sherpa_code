from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")


load_pha(1,"extract_new/spec_binned.pi")
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(1) 

##load BAT data
ui.load_pha(2,"bat_index_862.pha",use_errors=True)
er=ui.get_data(2).staterror*ui.get_exposure(2) 
ui.get_data(2).staterror=er
ui.load_rmf(2,"swiftbat_survey_full.rsp")

ui.set_method("simplex")



ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.xrt_const * (ui.powlaw1d.p1  + ui.xsbbody.bb))
ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))

#ui.set_source(1,ui.xsconstant.xrt_const * (ui.powlaw1d.p1  + ui.xsbbody.bb))
#ui.set_source(2,ui.xsconstant.bat_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))

#set parameters
abs_gal.nH = 0.053
ui.freeze(abs_gal.nH)




ui.set_par(p1.gamma, val = 1.27, min = 1.27-0.05, max = 1.27+0.04, frozen=False)
ui.set_par(p1.ampl, val = 1.72e-4, min = (1.72e-4 - 6.28e-6 ) , max = (1.72e-4 + 5.87e-6), frozen=False)
ui.set_par(bb.norm, val = 1.7e-5, min = 0, max = 4.2e-3 , frozen=False)
ui.set_par(bb.kT, val = 0.04, min = 0.04-0.02, max = 0.04+0.03, frozen=False)
ui.set_par(xrt_const.factor, val = 1,frozen=True)
ui.set_par(bat_const.factor, val = 1.99, min = 1.98, max = 2, frozen=False)



add_pileup_model=1
if(add_pileup_model):
    set_pileup_model(1,jdpileup.jdp)
    set_par(jdp.alpha, val = 0.27, frozen=True)
    set_par(jdp.g0, val = 1, frozen=True)
    set_par(jdp.f, val = 0.95, frozen=True)
    set_par(jdp.n, val = 1, frozen=True)
    set_par(jdp.ftime, val = 0.4, frozen=True)
    set_par(jdp.fracexp, val = 1, frozen=True)
    set_par(jdp.nterms, val = 30, frozen=True)

ui.plot_data(1)

ui.set_stat('chi2datavar')
ui.fit(1,2)
#conf()

#ui.show_model()

print(ui.get_fit_results())

ui.plot_fit_delchi(1)

energy = ui.calc_energy_flux(0.3,7)  
print ("energy flux =",energy)




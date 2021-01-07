from sherpa.astro import ui
#matplotlib inline

print("Read in Chandra and BAT data")

add_int_abs = 1


##load Chandra data
ui.load_pha(1,"extract_new/spec_binned.pi")
#group_counts(1,5)
ui.ignore(None, 0.3)
ui.ignore(7, None)
#ui.ignore_bad()
ui.subtract(1)



##load XRT data
ui.load_pha(3,"../swift_xrt/interval0pc_binned.pi")
ui.ignore(None, 0.3)
ui.ignore(7, None)
ui.ignore_bad(3)
ui.subtract(3) 


##load BAT data
##load data
ui.load_pha(2,"bat_index_862.pha",use_errors=True)
er=ui.get_data(2).staterror*ui.get_exposure(2) 
ui.get_data(2).staterror=er
ui.load_rmf(2,"swiftbat_survey_full.rsp")



##load BAT data
ui.load_pha(4,"bat_index_862.pha",use_errors=True)
er1=ui.get_data(4).staterror*ui.get_exposure(2) 
ui.get_data(4).staterror=er1
ui.load_rmf(4,"swiftbat_survey_full.rsp")

ui.set_method("simplex")


#ui.set_source(1,ui.xstbabs.abs_gal  * ui.xsconstant.chandra_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))
#ui.set_source(2,ui.xstbabs.abs_gal  * ui.xsconstant.bat_const *  ui.xszphabs.abs_intr * ui.xscabs.cabs * (ui.xspexrav.pexrav + ui.xsbbody.bb))

if(add_int_abs):
	ui.set_source(3,ui.xstbabs.abs_gal *  ui.xszphabs.abs_intr  * ui.xsconstant.xrt_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))
	ui.set_source(4,ui.xstbabs.abs_gal *  ui.xszphabs.abs_intr * ui.xsconstant.bat_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))
else:
	ui.set_source(3,ui.xstbabs.abs_gal *  ui.xsconstant.xrt_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))
	ui.set_source(4,ui.xstbabs.abs_gal *  ui.xsconstant.bat_const * (ui.powlaw1d.p1 + ui.xsbbody.bb))


#set parameters
abs_gal.nH = 0.053
ui.freeze(abs_gal.nH)

if(add_int_abs):
	ui.set_par(abs_intr.nH, val = 0.1, min = 0, max = 1000, frozen=False)
	abs_intr.redshift = 0.0728
	ui.freeze(abs_intr.redshift)


#ui.set_par(p1.gamma, val = 1.65, min = 1.65-0.05, max = 1.65+0.05, frozen=False)
ui.set_par(p1.gamma, val = 1.63, min = 0, max = 2, frozen=False)
ui.set_par(xrt_const.factor, val = 1,frozen=True)
ui.set_par(bat_const.factor, val = 1.1, min = 1, max = 2, frozen=False)
ui.set_par(bb.kT, val = 0.09, min = 0, max = 1, frozen=False)
ui.set_par(bb.norm, val = 0.000001, min = 0, max = 1, frozen=False)


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

#ui.plot_data(1)


ui.set_stat('chi2datavar')


print("pre fit")


ui.fit(3,4)

print("done fit 3,4")

#ui.show_model()
#conf()

#ui.plot_fit_delchi(3)

energy = ui.calc_energy_flux(0.3,7,3)  
print ("energy flux =",energy)
#plt.show()



if(add_int_abs):
	ui.set_source(1,ui.xstbabs.abs_gal1 *  ui.xszphabs.abs_intr1  * ui.xsconstant.chandra_const * (ui.powlaw1d.p12 + ui.xsbbody.bb1))
	ui.set_source(2,ui.xstbabs.abs_gal1 *  ui.xszphabs.abs_intr1 * ui.xsconstant.bat2_const * (ui.powlaw1d.p12 + ui.xsbbody.bb1))
else:
	ui.set_source(1,ui.xstbabs.abs_gal1  * ui.xsconstant.chandra_const * (ui.powlaw1d.p12 + ui.xsbbody.bb1))
	ui.set_source(2,ui.xstbabs.abs_gal1  * ui.xsconstant.bat2_const * (ui.powlaw1d.p12 + ui.xsbbody.bb1))

abs_gal1.nH = 0.053
ui.freeze(abs_gal1.nH)

if(add_int_abs):
	ui.set_par(abs_intr1.nH, val = 0.1, min = 0, max = 1000, frozen=False)
	abs_intr1.redshift = 0.0728
	ui.freeze(abs_intr1.redshift)


ui.set_par(chandra_const.factor, val = 1,frozen=True)
ui.set_par(bat2_const.factor, val = 1.1, min = 1, max = 2, frozen=False)
ui.set_par(bb1.kT, val = 0.09, min = 0, max = 1, frozen=False)
ui.set_par(bb1.norm, val = 0.000001, min = 0, max = 1, frozen=False)

ui.link(p12.gamma, p1.gamma)




ui.fit(1,2)


print("done fit 1,2")




#ui.show_model()

ui.plot_fit_delchi(1)




energy = ui.calc_energy_flux(0.3,7,1)  
print ("energy flux =",energy)
plt.show()


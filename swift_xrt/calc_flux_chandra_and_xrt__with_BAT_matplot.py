import matplotlib.pyplot as plt

load_pha(1,"../chandra/spec_binned.pi")
ignore(None, 0.3)
ignore(7, None)
subtract(1)

load_pha(2,"bat_index_862.pha",use_errors=True)
er=get_data(2).staterror*get_exposure(2) 
get_data(2).staterror=er
load_rmf(2,"swiftbat_survey_full.rsp")

set_method("simplex")

set_source(1,xstbabs.abs_gal  * xsconstant.chandra_const * (xspexrav.pexrav + xsbbody.bb))
set_source(2,xstbabs.abs_gal  * xsconstant.bat_const * (xspexrav.pexrav + xsbbody.bb))


#set parameters
abs_gal.nH = 0.053
freeze(abs_gal.nH)
#cabs.nH = 0.0
#abs_intr.nH = 0.0

#ui.freeze(cabs.nH)
#ui.freeze(abs_intr.nh)

#abs_intr.redshift = 0.0728
#ui.freeze(abs_intr.redshift)

pexrav.redshift = 0.0728
freeze(pexrav.redshift)
pexrav.cosIncl = 0.8660254 # cos 30 deg
freeze(pexrav.cosIncl)

set_par(pexrav.PhoIndex, val = 1.63, min = 0, max = 2, frozen=False)
set_par(pexrav.foldE, val = 60, min = 0, max = 200, frozen=False)
set_par(pexrav.rel_refl, val = 0.7, min = 0, max = 1, frozen=False)
set_par(pexrav.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
set_par(bb.kT, val = 0.09, min = 0, max = 1, frozen=False)
set_par(bb.norm, val = 0.000001, min = 0, max = 1, frozen=False)
set_par(chandra_const.factor, val = 1,frozen=True)
set_par(bat_const.factor, val = 1.1, min = 1, max = 2, frozen=False)


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
fit(1,2)

notice_id(1, 0.3, 7.0)

xx = get_fit_plot(1).dataplot.x
dd = get_fit_plot(1).dataplot.y
ee = get_fit_plot(1).dataplot.yerr
mm = get_fit_plot(1).modelplot.y

src = get_source(1)(xx)
scale = 1.60218e-9

plt.figure()
plt.errorbar(xx, dd*xx*xx*scale/mm*src, yerr=ee*xx*xx*scale/mm*src, c='red', marker="v",linestyle="None",markersize='3',label="Chandra")
plt.plot(xx,src*xx*xx*scale,c='red')
plt.xlabel('Energy (keV)')
plt.ylabel('ergs s$^{-1}$ cm$^{-2}$')
#plt.ylabel('Photons s$^{-1}$ cm$^{-2}$')
plt.xscale('log')
plt.yscale('log')
plt.xticks([0,0.5,1,2,7],['0', '0.5', '1','2','7'])

#############################

##load XRT data
load_pha(3,"interval0pc_binned.pi")
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(3) 


load_pha(4,"bat_index_862.pha",use_errors=True)
er=get_data(4).staterror*get_exposure(4) 
get_data(4).staterror=er
load_rmf(4,"swiftbat_survey_full.rsp")

set_source(3,xstbabs.abs_gal_2  * xsconstant.xrt_const_2 * (xspexrav.pexrav_2 + xsbbody.bb_2))
set_source(4,xstbabs.abs_gal_2  * xsconstant.bat_const_2 * (xspexrav.pexrav_2 + xsbbody.bb_2))

#set parameters
abs_gal_2.nH = 0.053
freeze(abs_gal_2.nH)
#cabs.nH = 0.0
#abs_intr.nH = 0.0

#ui.freeze(cabs.nH)
#ui.freeze(abs_intr.nh)

#abs_intr.redshift = 0.0728
#ui.freeze(abs_intr.redshift)

pexrav_2.redshift = 0.0728
freeze(pexrav_2.redshift)
pexrav_2.cosIncl = 0.8660254 # cos 30 deg
freeze(pexrav_2.cosIncl)

set_par(pexrav_2.PhoIndex, val = 1.63, min = 0, max = 2, frozen=False)
set_par(pexrav_2.foldE, val = 60, min = 0, max = 200, frozen=False)
set_par(pexrav_2.rel_refl, val = 0.7, min = 0, max = 1, frozen=False)
set_par(pexrav_2.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
set_par(bb_2.norm, val = 0.000001, min = 0, max = 1, frozen=False)
set_par(bb_2.kT, val = 0.09, min = 0, max = 1, frozen=False)
set_par(xrt_const_2.factor, val = 1,frozen=True)
set_par(bat_const_2.factor, val = 1.1, min = 1, max = 2, frozen=False)


fit(3,4)
notice_id(3, 0.3, 7.0)

xx2 = get_fit_plot(3).dataplot.x
dd2 = get_fit_plot(3).dataplot.y
ee2 = get_fit_plot(3).dataplot.yerr
mm2 = get_fit_plot(3).modelplot.y

src2 = get_source(3)(xx2)

plt.errorbar(xx2, dd2*xx2*xx2*scale/mm2*src2, yerr=ee2*xx2*xx2*scale/mm2*src2, c='blue', marker="*",linestyle="None",markersize='3',label="Swift-XRT")
plt.plot(xx2,src2*xx2*xx2*scale,c='blue')
plt.legend()
plt.show()

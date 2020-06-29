from sherpa_contrib.chart import *

load_pha(1,"spec_binned.pi")
#group_counts(1,5)
ignore(None, 0.3)
ignore(7, None)
subtract(1)


set_method("simplex")

set_source(1,xsphabs.abs_gal  * xsconstant.xrt_const *  xszphabs.abs_intr * xscabs.cabs * (xspexrav.pexrav + xsbbody.bb))


#set_source(1,xsphabs.abs_gal  * xsconstant.xrt_const * (xspexrav.pexrav + xsbbody.bb))
#set_source(2,xsphabs.abs_gal  * xsconstant.bat_const * (xspexrav.pexrav + xsbbody.bb))

#set parameters
abs_gal.nH = 0.053
freeze(abs_gal.nH)
cabs.nH = 0.0
abs_intr.nH = 0.0

freeze(cabs.nH)
freeze(abs_intr.nh)

abs_intr.redshift = 0.0728
freeze(abs_intr.redshift)

pexrav.redshift = 0.0728
freeze(pexrav.redshift)
pexrav.cosIncl = 0.8660254 # cos 30 deg
freeze(pexrav.cosIncl)

set_par(pexrav.PhoIndex, val = 1.63, min = 0, max = 2, frozen=False)
set_par(pexrav.foldE, val = 60, min = 0, max = 200, frozen=False)
set_par(pexrav.rel_refl, val = 0.7, min = 0, max = 1, frozen=False)
set_par(pexrav.norm, val = 0.00021, min = 0, max = 0.1, frozen=False)
set_par(bb.kT, val = 0.09, min = 0, max = 1, frozen=False)
	
set_par(xrt_const.factor, val = 1,frozen=True)


guess(pexrav)

#set_stat("wstat")
set_stat('chi2datavar')


set_pileup_model(1,jdpileup.jdp)

set_par(jdp.alpha, val = 0.5, min = 0, max = 1, frozen=False)
set_par(jdp.g0, val = 1, frozen=True)
set_par(jdp.f, val = 0.95, frozen=True)
set_par(jdp.n, val = 1, frozen=True)
set_par(jdp.ftime, val = 0.4, frozen=True)
set_par(jdp.fracexp, val = 1, frozen=True)
set_par(jdp.nterms, val = 30, frozen=True)


#abs_gal.nH = 0.02
#freeze(abs_gal.nH)

#abs_intr.nH = 0.02
#abs_intr.redshift = 0.0728
#freeze(abs_intr.redshift)

set_stat('chi2datavar')
#set_stat('cash')

fit(1)


set_analysis(1, "energy", "rate", factor=1)
plot_source()

save_chart_spectrum("source_flux_chart.dat", elow=0.3, ehigh=7.0)
	

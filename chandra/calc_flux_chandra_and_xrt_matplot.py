import matplotlib.pyplot as plt

load_pha(1,"spec.pi")
group_counts(1,5)
ignore(None, 0.3)
ignore(7, None)
subtract(1)

set_method("simplex")
set_source(1,xsphabs.abs_gal  *powlaw1d.p1)

abs_gal.nH = 0.02
freeze(abs_gal.nH)

set_stat('chi2datavar')
fit(1)

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

load_pha(2,"../swift_xrt/interval0pc.pi")

group_counts(2,5) 
ignore(None, 0.3)
ignore(7, None)
ignore_bad()
subtract(2) 

set_source(2,xsphabs.abs_gal_2  *powlaw1d.p1_2)
abs_gal_2.nH = 0.02
freeze(abs_gal_2.nH)


fit(2)
notice_id(2, 0.3, 7.0)

xx2 = get_fit_plot(2).dataplot.x
dd2 = get_fit_plot(2).dataplot.y
ee2 = get_fit_plot(2).dataplot.yerr
mm2 = get_fit_plot(2).modelplot.y

src2 = get_source(2)(xx2)

plt.errorbar(xx2, dd2*xx2*xx2*scale/mm2*src2, yerr=ee2*xx2*xx2*scale/mm2*src2, c='blue', marker="*",linestyle="None",markersize='3',label="Swift-XRT")
plt.plot(xx2,src2*xx2*xx2*scale,c='blue')
plt.legend()
plt.show()


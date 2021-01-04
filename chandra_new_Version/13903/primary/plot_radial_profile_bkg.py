from pycrates import read_file
import matplotlib.pylab as plt





tab_img = read_file("img_rprofile.fits")
tab = read_file("psf_rprofile.fits")

xx = tab.get_column("rmid").values
yy = tab.get_column("sur_bri").values
ye = tab.get_column("sur_bri_err").values




xx_img = tab_img.get_column("rmid").values
yy_img = tab_img.get_column("sur_bri").values
ye_img = tab_img.get_column("sur_bri_err").values

scale = yy_img[0] / yy[0]

yy = yy *scale
ye = ye *scale




it=0
for xx_it in xx:
	print("s_no = ",it,"x = ",xx[it]," yy = ",yy[it]," y_err = ",ye[it])
	it = it+1

xx = xx *60 * 0.00820042
xx_img = xx_img *60 * 0.00820042


plt.errorbar(xx,yy,yerr=ye, marker="o",label="PSF")
plt.errorbar(xx_img,yy_img,yerr=ye_img, marker="o",color='red',label="Image")


tab_bkg = read_file("bkg_rprofile.fits")


xx_bkg = tab_bkg.get_column("rmid").values
yy_bkg = tab_bkg.get_column("sur_bri").values
ye_bkg = tab_bkg.get_column("sur_bri_err").values



xx_bkg = xx_bkg *60 * 0.00820042

plt.errorbar(xx_bkg,yy_bkg,yerr=ye_bkg, marker="o",color='green',label="Background")

#plt.xscale("log")
plt.yscale("log")
plt.xlabel("R_MID (arcsec)")
plt.ylabel("SUR_BRI (photons/cm**2/pixel**2/s)")
plt.legend()

plt.show()

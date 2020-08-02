from pycrates import read_file
import matplotlib.pylab as plt


tab = read_file("img_rprofile.fits")
#tab = read_file("psf_rprofile.fits")

xx = tab.get_column("rmid").values
yy = tab.get_column("sur_bri").values
ye = tab.get_column("sur_bri_err").values

xx = xx *60 * 0.00820042

debug=False

if(debug):
	counts = tab.get_column("counts").values
	area = tab.get_column("area").values
	bg_counts = tab.get_column("bg_counts").values
	bg_area = tab.get_column("bg_area").values
 
	net_counts = counts - ((bg_counts/bg_area)*area)
	sur_bri = net_counts/area

	print(net_counts)
	print(sur_bri)


plt.errorbar(xx,yy,yerr=ye, marker="o")

#plt.xscale("log")
plt.yscale("log")
plt.xlabel("R_MID (arcsec)")
plt.ylabel("SUR_BRI (photons/cm**2/pixel**2/s)")

plt.show()

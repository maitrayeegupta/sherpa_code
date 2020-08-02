load_data(1,"img_rprofile.fits", 3, ["RMID","SUR_BRI","SUR_BRI_ERR"])
#load_data(1,"psf_rprofile.fits", 2, ["RMID","SUR_BRI"])

set_ylog()
set_source("beta1d.src")
src.r0 = 5
src.beta = 4
src.ampl = 0.00993448

freeze(src.xpos)

fit()
   

plot_fit()


load_data(1,"img_rprofile.fits", 2, ["RMID","SUR_BRI"])
load_data(2,"psf_rprofile.fits", 2, ["RMID","SUR_BRI"])

sur_bri = get_data(2).y * 8000
get_data(2).y=sur_bri

set_ylog()
set_source(1,"beta1d.src1")
set_par(src1.r0, val = 5, min = 1e-10, max = 4, frozen=False)
set_par(src1.beta, val = 4, min = 1e-10, max = 10, frozen=False)
src1.ampl = 1

freeze(src1.xpos)
fit(1)


set_source(2,"beta1d.src2")
set_par(src2.r0, val = 5, min = 1e-10, max = 3, frozen=False)
src2.beta = 10
src2.ampl = 1

freeze(src2.xpos)
fit(2)   

plot("fit",1,"fit",2)


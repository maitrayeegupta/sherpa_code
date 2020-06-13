#load sample RMFs and corresponding ARFs 
arf1 = unpack_arf("aciss_aimpt_cy22.arf")
rmf1 = unpack_rmf("aciss_aimpt_cy22.rmf")



#load model
set_source(1,bbody.bb)
set_par(bb.kT, val = 0.09, min = 0, max = 2, frozen=False)
	
exposure_time = 5000000

fake_pha(1, arf1 ,rmf1, exposure=exposure_time)

#display only till 7keV
group_counts(1) 
ignore(None, 0.3)
ignore(7, None)


#print model parameters
show_model()

#plotting parameters
prefs = get_data_plot_prefs()
prefs["yerrorbars"] = 0


plot_data(1)

#fit model
#fit(1)
#print("HERE!!!")
#
#plot_fit()


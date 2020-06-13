import sys
import re 
import csv
import math

E_low = 0.3
E_high =7

file_name = "flux_"+str(E_low)+"_"+str(E_high)+".csv"


fl = open(file_name, 'w')
fl.write("Name,T,norm,Calc_energy_flux,Sample_flux,plus_Error,minus_Error,log_energy_flux,log_sample_flux\n")
fl.close()



names=[]
Ts=[]
norms=[]
data = open('all_matches.csv')
print("opened file")
csv_f = csv.reader(data)
i=0
for row in csv_f:
	if (i != 0):
		names.append((row[1]))
		Ts.append(float(row[2]))
		norms.append(float(row[6]))
	i=i+1
data.close()

i=0
for tt in Ts:
	
	set_source(xsbbody.bb)            # set your model
	dataspace1d(0.01,10,0.01)      # you need a dataspace scale, which is usually taken from arf files for fitting spectra, but you can setup it up with dataspace1d as well
	name=names[i]
	kt_val = Ts[i]
	norm_val = norms[i]
	i=i+1
	print("working on: object(",i,") name =",name," T = ",kt_val," norm = ",norm_val)
	if((kt_val==-99) or (norm_val == -99)):
		fl = open(file_name, 'a')
		print("going to write :: -99,-99,-99\n")
		fl.write(str(name))
		fl.write(",")
		fl.write(str(kt_val))
		fl.write(",")
		fl.write(str(norm_val))
		fl.write(",-99,-99,-99,-99,-99,-99")
		fl.write("\n")
		fl.close()
		
	else :
		set_par(bb.kT, val = kt_val, min = kt_val-0.001, max = kt_val+0.001, frozen=False)
		set_par(bb.norm, val = norm_val, frozen=True)
		calc_energy =  (calc_energy_flux(E_low,E_high))

		orig_stdout = sys.stdout
		f1 = open('file', 'w')
		sys.stdout = f1
		flux_ = sample_flux(bb, E_low, E_high, num=5000)
		sys.stdout = orig_stdout
		f1.close()

		f = open("file", "r")
		line = f.readline()
		data = re.split(', |\n| +| -', line)
		f.close()

		fl = open(file_name, 'a')
		print("going to write ::", calc_energy, flux_[0][0],",",data[6],",",data[8],"\n")
		log_sample_flux = math.log10(flux_[0][0])
		log_calc_energy = math.log10(calc_energy)
		fl.write(str(name))
		fl.write(",")
		fl.write(str(kt_val))
		fl.write(",")
		fl.write(str(norm_val))
		fl.write(",")
		fl.write(str(calc_energy))
		fl.write(",")
		fl.write(str(flux_[0][0]))
		fl.write(",")
		fl.write(str(data[6]))
		fl.write(",")
		fl.write(str(data[8]))
		fl.write(",")
		fl.write(str(log_calc_energy))
		fl.write(",")
		fl.write(str(log_sample_flux))
		fl.write("\n")
		fl.close()


print("all done")


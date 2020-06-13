import sys
import re 
import csv

fl = open('flux.csv', 'w')
fl.write("Name,T,norm,Calc_energy_flux,Sample_flux,+Error,-Error\n")
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


print("need to process ",i," objcts")
i=0
for tt in Ts:
	
	set_source(xsbbody.bb)            # set your model
	dataspace1d(0.1,10,0.01)      # you need a dataspace scale, which is usually taken from arf files for fitting spectra, but you can setup it up with dataspace1d as well
	name=names[i]
	kt_val = Ts[i]
	norm_val = norms[i]
	i=i+1
	print("working on: object(",i,") name =",name," T = ",kt_val," norm = ",norm_val)
	if((kt_val==-99) or (norm_val == -99)):
		fl = open('flux.csv', 'a')
		print("going to write :: -99,-99,-99\n")
		fl.write(str(name))
		fl.write(",")
		fl.write(str(kt_val))
		fl.write(",")
		fl.write(str(norm_val))
		fl.write(",-99,-99,-99,-99")
		fl.write("\n")
		fl.close()
		
	else :
		set_par(bb.kT, val = kt_val, min = kt_val-0.001, max = kt_val+0.001, frozen=False)
		set_par(bb.norm, val = norm_val, frozen=True)
		calc_energy =  (calc_energy_flux(0.3,7))   
		print("going to write ::",calc_energy)
		fl = open('flux.csv', 'a')
		fl.write(str(name))
		fl.write(",")
		fl.write(str(kt_val))
		fl.write(",")
		fl.write(str(norm_val))
		fl.write(",")
		fl.write(str(calc_energy))
		fl.write(",-99,-99,-99")
		fl.write("\n")
		fl.close()
		#print(data[1])

print("all done")


# need this to wait
import time

# need this for command line arguments and for the path
import sys

# need this to make sensor output readable
from tabulate import tabulate

# need this to concatenate ranges for predictable sensor suite iteration
from itertools import chain

# need this to import sensors
sys.path.insert(0, '/home/atecce/OASIS/API/sensors')

# import sensors by category
from ADC      import *
from I2C      import *
from one_wire import *
from UART     import *
from USB      import camera

def main(argv):

	# read in arguments
	sensor_name =     argv[1]

	# get amount of readings, default is 1
	try: 		   readings = int(argv[2])
	except IndexError: readings = 1

	# doing it this way so not every sensor needs to be loaded every time the script is used
	if   sensor_name == "EC1":	   sensor = electrical_conductivity("electrical_conductivity",  0x66)
	elif sensor_name == "pH1":	   sensor =              I2C_sensor("ph_and_circuitry",         0x65)
	elif sensor_name == "temp1":       sensor =             temperature("liquid_temp",             "28-00000673a8a7")
	elif sensor_name == "DO":   	   sensor =              I2C_sensor("do_probe_and_circuitry",   0x61)
	elif sensor_name == "LL1": 	   sensor =            liquid_level("liquid_level",             0x80) 
	elif sensor_name == "LL2": 	   sensor =            liquid_level("liquid_level",             0xA0)
	elif sensor_name == "LL3": 	   sensor =            liquid_level("liquid_level",             0xC0)
	elif sensor_name == "LL4": 	   sensor =            liquid_level("liquid_level",             0xE0)
	elif sensor_name == "LL5": 	   sensor =            liquid_level("liquid_level",             0xD0)
	elif sensor_name == "flow_meter1": sensor =              flow_meter("flow_meter_and_circuitry", 1)
	elif sensor_name == "flow_meter2": sensor =              flow_meter("flow_meter_and_circuitry", 4)
	elif sensor_name == "LL6": 	   sensor =            liquid_level("liquid_level",             0xF0)
	elif sensor_name == "temp2":	   sensor =             temperature("liquid_temp",             "28-0000065f27cc") 
	elif sensor_name == "temp3":	   sensor =             temperature("liquid_temp",             "28-0000065eb57a")
	elif sensor_name == "temp4":	   sensor =             temperature("liquid_temp",             "28-000006747f7f")
	elif sensor_name == "EC2":	   sensor = electrical_conductivity("electrical_conductivity",  0x64)
	elif sensor_name == "pH2":	   sensor =              I2C_sensor("ph_and_circuitry",	        0x63)
	elif sensor_name == "MO1":	   sensor =                moisture("moisture",                 0x80)
	elif sensor_name == "MO2":	   sensor =                moisture("moisture",                 0xA0)
	elif sensor_name == "MO3":	   sensor =                moisture("moisture",                 0xC0)
	elif sensor_name == "MO4":	   sensor =                moisture("moisture",                 0xE0)
	elif sensor_name == "RHT1":	   sensor =             RH_and_temp("rh_and_air_temp",         'P8_8')
	elif sensor_name == "RHT2":	   sensor =             RH_and_temp("rh_and_air_temp",         'P8_9')
	elif sensor_name == "TP1":	   sensor =          total_pressure("total_pressure",           2)
	elif sensor_name == "O2":	   sensor =                  oxygen("O2")
	elif sensor_name == "CO2":	   sensor =                     CO2("CO2",                      5)
	elif sensor_name == "PAR1":	   sensor =                     PAR("light",                    0xF0)
	elif sensor_name == "RHT3":	   sensor =             RH_and_temp("rh_and_air_temp",         'P8_10')
	elif sensor_name == "TP2":	   sensor =          total_pressure("total_pressure",           1)
	elif sensor_name == "PAR2": 	   sensor =                     PAR("light",                    0xD0)

	elif sensor_name == "all":

		# populate sensor suite
		S = {101: electrical_conductivity("electrical_conductivity", 0x66),
		     102:              I2C_sensor("ph_and_circuitry",        0x65),
		     103:             temperature("liquid_temp", "28-00000673a8a7"),
		     104:              I2C_sensor("do_probe_and_circuitry",  0x61),
		     105:            liquid_level("liquid_level", 0x80), 
		     106:            liquid_level("liquid_level", 0xA0),
		     107:            liquid_level("liquid_level", 0xC0),
		     108:            liquid_level("liquid_level", 0xE0),
		     109:            liquid_level("liquid_level", 0xD0),
		     110:              flow_meter("flow_meter_and_circuitry", 1),
		     111:              flow_meter("flow_meter_and_circuitry", 4),
		     112:            liquid_level("liquid_level", 0xF0),

		     201: 	       temperature("liquid_temp", "28-0000065f27cc"), 
		     202: 	       temperature("liquid_temp", "28-0000065eb57a"),
		     203: 	       temperature("liquid_temp", "28-000006747f7f"),
		     205:  electrical_conductivity("electrical_conductivity", 0x64),
		     206:  		I2C_sensor("ph_and_circuitry",	   0x63),
		     208:  		  moisture("moisture", 0x80),
		     209:  		  moisture("moisture", 0xA0),
		     210:  		  moisture("moisture", 0xC0),
		     211:  		  moisture("moisture", 0xE0),

		     301:    RH_and_temp("rh_and_air_temp", 'P8_8'),
		     302:    RH_and_temp("rh_and_air_temp", 'P8_9'),
		     303: total_pressure("total_pressure", 2),
		     304:         oxygen("O2"),
		     305:            CO2("CO2", 5),
		     306:            PAR("light", 0xF0),

		     401:    RH_and_temp("rh_and_air_temp", 'P8_10'),
		     402: total_pressure("total_pressure", 1),
		     403: 	     PAR("light", 0xD0)}

		# set of ID's sensors take
		SysIDs = chain(range(101, 113), range(201, 204), range(205, 207), range(208, 212), range(301, 307), range(401, 404))

		# initialize table
		table = list()

		# for each system ID
		for SysID in SysIDs:

			# initalize entry
			entry = [repr(S[SysID]), "S" + str(SysID), S[SysID].table]

			# try to append reading to entry
			try:            entry.append(S[SysID].read())  
			except IOError: entry.append("IOError")

			# append the entry to table
			table.append(entry)

		# print the table
		print tabulate(table)

		# exit with success	
		sys.exit(0)

	# catch error (probably needs work)
	else: print "Invalid sensor name"

	# start timer
	start = time.time()

	# read the specified amount of times
	for i in range(readings): 

		# take reading
		reading = sensor.read()

		# calculate current time
		current_time = time.time() - start
		
		# print columns of readings indexed at 1
		print current_time, reading

		# wait a second
		time.sleep(1)

if __name__ == "__main__": main(sys.argv)
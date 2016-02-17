# need this to wait
import time

class actuator:

	# makes output more readable
	lookup_key = {45: {1: "off", 0: "on"},
		      44: {1: "off", 0: "on"},
		      26: {1: "off", 0: "on"},	
		      87: {1: "off", 0: "on"},
		      89: {1: "off", 0: "on"},
		      11: {1: "off", 0: "on"},
		      62: {0: "off", 1: "on"},
		      63: {0: "off", 1: "on"},
		      23: {0: "off", 1: "on"},
		      65: {0: "off", 1: "on"},
		      27: {0: "off", 1: "on"},
		      37: {0: "off", 1: "on"},
		      33: {0: "off", 1: "on"},
		      61: {0: "off", 1: "on"},
		      86: {0: "off", 1: "on"},
		      32: {0: "off", 1: "on"},
		      36: {0: "off", 1: "on"},
		      70: {0: "low", 1: "high"},
		      71: {0: "low", 1: "high"},	
		      51: {0: "off", 1: "on"}}	

	def __init__(self, pin):

		# assign pin
		self.pin = pin

		# set path for device file with pin
		self.path = "/sys/devices/virtual/gpio/gpio" + str(pin) + "/value" 

	def check_status(self): 

		# open up the device
		device = open(self.path)

		# read in the value as an integer
		value = int(device.read().rstrip())

		# close the device
		device.close()

		# look up the state
		state = self.lookup_key[self.pin][value]

		return state

	def toggle(self):

		# open the device for reading
		device = open(self.path)

		# read in the value as an integer
		value = int(device.read().rstrip())

		# close the device
		device.close()

		# flip the switch
		if   value == 0: value = 1
		elif value == 1: value = 0
		else: print "throw error"

		# open the device for writing
		device = open(self.path, 'w')

		# write the new value
		device.write(str(value))

		# close the device
		device.close()

A = {"heater":          actuator(45),
     "chiller":         actuator(44),
     "O2 concentrator": actuator(26),
     "Pump 1":          actuator(62),
     "Pump 2":          actuator(63),
     "Pump 3":          actuator(23),
     "Pump 4":          actuator(65),
     "Pump 5":          actuator(27),
     "Pump 6":          actuator(37),
     "Pump 7":          actuator(33),
     "Pump 8":          actuator(61),
     "Pump 9":          actuator(86),
     "Pump 10":         actuator(32),
     "Pump 11":         actuator(36),
     "Pump 12":         actuator(87),
     "Fan 1":           actuator(70),
     "Fan 2":           actuator(71),
     "LED":             actuator(51)}

# turn each actuator on and off
for actuator in A:

	print actuator, "is", actuator.check_status()

import smbus #import smbus library
import time

bus = smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number

#time.sleep(5)

# address, ascii r value
bus.write_byte(0x64, 0x52) #R

time.sleep(2)


results = bus.read_i2c_block_data(0x64,0x52) #read cal info

time.sleep(2)

print
print results #print data
print

for index, item in enumerate(results):
        if item == 0:
                end_val = index
                break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
print results_string #print data
Sensor_Temperature = 27
Temperature = 0

USB = 0

while True:
    Temperature = Sensor_Temperature
    if Temperature >= 30:
        USB = 1
    else:
        USB = 0
''' Grove lightsensor (v1.1)
  Ucc = 1.6 V
  Uout = Ucc (R/R+Rldr), R=10k
  Ucc is generated form another voltage divider, 2x R=10k
  Grove Lightsensor: https://github.com/Seeed-Studio/Light_Sensor/blob/master/examples/Light_Sensor/Light_Sensor.ino
#'''

import machine, time

_ADC_PIN = const(0)
_WARNING_LED_PIN = const(14)

# read ADC-value
adc = machine.ADC(_ADC_PIN)
#TEST: print('ADC reading:', adc.read())
alert = machine.Pin(_WARNING_LED_PIN, machine.Pin.OUT)

'''
Arduino program
int sensorValue = analogRead(LIGHT_SENSOR);
Rsensor = (float)(1023-sensorValue)*10/sensorValue;
Serial.println("the analog read data is ");
Serial.println(sensorValue);
Serial.println("the sensor resistance is ");
Serial.println(Rsensor,DEC);//show the ligth intensity on the serial monitor;
'''
def Rsensor(value):
    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    return (1023.0 - value)*10/value

# Ucc = 1.6 volt
_UREF = 1.6 # Ucc in circuit
def adc2voltage(value):
    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    return value * (_UREF / 1023.0)

# run readng T, Ctrl-C to abort
def run(dt=2.0):
    try:
        while True:
            reading = adc.read()
            voltage = adc2voltage(reading)
            rsensor = Resensor(reading)
            print('Photocell reading {0}\tvoltage {1:0.1f}\trsensor {2:0.1f}'.format(reading, voltage, rsensor))
            if reading > 1000:
                alertOn()
            else:
                alertOff()
            time.sleep(dt) #wait > s, see datasheet
    except:
        print('done')

run()

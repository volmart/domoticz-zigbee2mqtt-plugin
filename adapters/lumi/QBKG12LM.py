from adapters.lumi.ctrl_neutral2 import AqaraDoubleWiredSwitch
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.kwh import KwhSensor

# Xiaomi Mi power plug
class QBKG12LM(AqaraDoubleWiredSwitch):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        self.devices.append(KwhSensor(devices, 'kwh', 'power'))

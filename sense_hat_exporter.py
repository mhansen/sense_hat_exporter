import time
from sense_hat import SenseHat
from prometheus_client import start_http_server, Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY

sense = SenseHat()

class SenseHatCollector(object):
    def collect(self):
        yield GaugeMetricFamily(
            name='sense_hat_temperature_celsius',
            documentation='Temperature as measured by Raspberry Pi Sense Hat',
            value=sense.temperature)
        yield GaugeMetricFamily(
            name='sense_hat_pressure_pascals',
            documentation='Pressure (Pa) Measured by Raspberry Pi Sense Hat',
            value=sense.pressure*100)  # hPa to Pa
        yield GaugeMetricFamily(
            name='sense_hat_humidity',
            documentation='Measured by Raspberry Pi Sense Hat',
            value=sense.humidity)
        yield compass_metric()

def compass_metric():
    raw = sense.get_compass_raw()

    family = GaugeMetricFamily(
            name='sense_hat_compass_raw',
            documentation='Measured by Raspberry Pi Sense Hat',
            labels=["axis"])
    family.add_metric(["x"], raw["x"])
    family.add_metric(["y"], raw["y"])
    family.add_metric(["z"], raw["z"])
    return family

REGISTRY.register(SenseHatCollector())
start_http_server(8000)
while True:
  time.sleep(60)

# Sense Hat Exporter

A [Prometheus](https://prometheus.io/) exporter for Raspberry Pi [Sense-HAT add-on board](https://www.raspberrypi.org/products/sense-hat/).

End-to-end example showing prometheus text-format output:

```shell
$ python3 sense_hat_exporter.py

$ curl http://localhost:9607/metrics
...
# HELP sense_hat_temperature_celsius Temperature as measured by Raspberry Pi Sense Hat
# TYPE sense_hat_temperature_celsius gauge
sense_hat_temperature_celsius{source_sensor="humidity"} 41.965187072753906
sense_hat_temperature_celsius{source_sensor="pressure"} 39.14583206176758
# HELP sense_hat_pressure_pascals Pressure (Pa) Measured by Raspberry Pi Sense Hat
# TYPE sense_hat_pressure_pascals gauge
sense_hat_pressure_pascals 102169.482421875
# HELP sense_hat_humidity Measured by Raspberry Pi Sense Hat
# TYPE sense_hat_humidity gauge
sense_hat_humidity 37.825599670410156
# HELP sense_hat_compass_raw Measured by Raspberry Pi Sense Hat
# TYPE sense_hat_compass_raw gauge
sense_hat_compass_raw{axis="x"} -37.817047119140625
sense_hat_compass_raw{axis="y"} 35.46157455444336
sense_hat_compass_raw{axis="z"} -13.82213306427002
# HELP sense_hat_accelerometer_raw Measured by Raspberry Pi Sense Hat
# TYPE sense_hat_accelerometer_raw gauge
sense_hat_accelerometer_raw{axis="x"} 0.1903200000524521
sense_hat_accelerometer_raw{axis="y"} -0.24253599345684052
sense_hat_accelerometer_raw{axis="z"} 0.9464759826660156
# HELP sense_hat_gyroscope_raw radians/second
# TYPE sense_hat_gyroscope_raw gauge
sense_hat_gyroscope_raw{axis="x"} -0.0008594170212745667
sense_hat_gyroscope_raw{axis="y"} -0.0014123693108558655
sense_hat_gyroscope_raw{axis="z"} -0.0004970086738467216
```

Example `docker-compose.yml` config:

```yml
version: '3.4'
services:
  rtl_433_prometheus:
    image: markhnsn/rtl_433_prometheus
    restart: always
    ports:
    - "9607:9607"
    # Needed for driver access
    privileged: true
```

Example `prometheus.yml`:

```yml
scrape_configs:
  - job_name: 'sense_hat_exporter'
      static_configs:
            - targets: ['hostname:9607']
```

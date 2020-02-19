# Can be built on any x86_64 fine, without virtualization, thanks to cross-build-start!

# Tried this with alpine first, had a bad time.
FROM balenalib/raspberrypi3-debian

# https://www.balena.io/docs/reference/base-images/base-images/#building-arm-containers-on-x86-machines
RUN [ "cross-build-start" ]
RUN apt-get update && apt-get install python3-sense-hat python3-pip
RUN python3 -m pip install prometheus_client
# https://www.balena.io/docs/reference/base-images/base-images/#building-arm-containers-on-x86-machines
RUN [ "cross-build-end" ]

COPY sense_hat_exporter.py /root
# Registered at https://github.com/prometheus/prometheus/wiki/Default-port-allocations
EXPOSE 9607
ENTRYPOINT ["python3", "/root/sense_hat_exporter.py"]

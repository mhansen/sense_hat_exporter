# Tried this with alpine first, had a bad time.
FROM balenalib/raspberrypi3-debian

RUN apt-get update && apt-get install python3-sense-hat
RUN python3 -m ensurepip
RUN python3 -m pip install prometheus_client
COPY sense_hat_exporter.py /root
EXPOSE 8000
ENTRYPOINT ["python3", "/root/sense_hat_exporter.py"]

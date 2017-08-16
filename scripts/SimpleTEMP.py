from webiopi.devices.sensor import DS18S20
tmp0 = DS18S20(slave="10-000802dec1d3")
print tmp0.getCelsius()
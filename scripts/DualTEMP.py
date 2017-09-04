from webiopi.devices.sensor import DS18S20
tmp0 = DS18S20(slave="10-000802dec1d3")
tmp1 = DS18S20(slave="10-000802cb2f2c")
print tmp0.getCelsius()
print tmp1.getCelsius()

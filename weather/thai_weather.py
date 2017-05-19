#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,folium
r = requests.get('http://data.tmd.go.th/api/Weather3Hours/V1/')
doc = eval(r.text)
a = doc['Stations']
DateTime = doc['Header']['LastBuiltDate']
imap = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
i = 0

while i < len(a):
    c = a[i]
    Latitude = c['Latitude']['Value']
    Longitude = c['Longitude']['Value']
    c1 = c['Observe']
    BarometerTemperature = c1['BarometerTemperature']['Value']
    StationPressure = c1['StationPressure']['Value']
    MeanSeaLevelPressure = c1['MeanSeaLevelPressure']['Value']
    DewPoint = c1['DewPoint']['Value']
    RelativeHumidity = c1['RelativeHumidity']['Value']
    VaporPressure  = c1['VaporPressure']['Value']
    LandVisibility = c1['LandVisibility']['Value']
    WindDirection = c1['WindDirection']['Value']
    WindSpeed  = c1['WindSpeed']['Value']
    Rainfall  = c1['Rainfall']['Value']
    popup1= """สถานี : %s <br>
    วัน - เวลา : %s<br>
    อุณหภูมิบาโรมิเตอร์ : %s องศาเซลซียส <br>
    ความกดอากาศที่สถานี : %.2f มิลลิบาร์ <br>
    ความกดอากาศที่ระดับน้ำทะเล : %.2f มิลลิบาร์ <br>
    อุณหภูมิจุดน้ำค้าง : %s องศาเซลซียส <br>
    ความชื้นสัมพัทธ์ : %s  เปอร์เซ็นต์ <br>
    ความดันไอ : %.2f  มิลลิบาร์<br>
    ทัศนวิสัยทางบก : %.2f กิโลเมตร <br>
    ทิศทางลม : %s องศา <br>
    ความเร็วลม : %.2f กิโลเมตร/ชั่วโมง <br>
    ปริมาณฝน : %.2f มิลลิเมตร
    """ % (c['StationNameTh'],DateTime,BarometerTemperature,StationPressure,MeanSeaLevelPressure,DewPoint,RelativeHumidity,VaporPressure,LandVisibility,WindDirection,WindSpeed,Rainfall)
    imap.simple_marker(location=[Latitude,Longitude],popup=popup1)
    i+=1

imap.create_map(path='thai_weather3hours.html')
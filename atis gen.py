import pydub
from pydub import *
import datetime

def atis_gen(atis_data):
    icao=atis_data["icao"]
    icao=icao.lower()
    airport=AudioSegment.from_mp3("audio/"+icao[0]+".mp3")+AudioSegment.from_mp3("audio/"+icao[1]+".mp3")+AudioSegment.from_mp3("audio/"+icao[2]+".mp3")+AudioSegment.from_mp3("audio/"+icao[3]+".mp3")
    information=airport+AudioSegment.from_mp3("audio/airport_information.mp3")+AudioSegment.from_mp3("audio/"+atis_data["id"]+".mp3")
    

    time=str(datetime.datetime.utcnow())
    time=time[11:13]+time[14:16]
    h1=AudioSegment.from_mp3("audio/"+time[0]+".mp3")
    h2=AudioSegment.from_mp3("audio/"+time[1]+".mp3")
    m1=AudioSegment.from_mp3("audio/"+time[2]+".mp3")
    m2=AudioSegment.from_mp3("audio/"+time[3]+".mp3")
    time=h1+h2+m1+m2+AudioSegment.from_mp3("audio/z.mp3")

    
    wind_dir=str(atis_data["wind_dir"])
    wind_dir=AudioSegment.from_mp3("audio/"+wind_dir[0]+".mp3")+AudioSegment.from_mp3("audio/"+wind_dir[1]+".mp3")+AudioSegment.from_mp3("audio/"+wind_dir[2]+".mp3")
    wind_speed_input=str(atis_data["wind_speed"])
    wind_speed=AudioSegment.from_mp3("audio/"+wind_speed_input[0]+".mp3")
    if len(wind_speed_input)>1:
        for i in range(1,len(wind_speed_input)-1):
            wind_speed=wind_seed+AudioSegment.from_mp3("audio/"+wind_speed_input[i]+".mp3")
    wind=AudioSegment.from_mp3("audio/wind.mp3")+wind_dir+AudioSegment.from_mp3("audio/at.mp3")+wind_speed+AudioSegment.from_mp3("audio/knots.mp3")

    skycondition=AudioSegment.empty()
    for sc in atis_data["sky"]:
        condition=sc[0:3]
        if condition=="CLR":
            skycondition=skycondition+AudioSegment.from_mp3("audio/clear.mp3")
        else:
            alt=sc[3:6]
            if alt[0] != '0':
                fl=AudioSegment.from_mp3("audio/flight_level.mp3")+AudioSegment.from_mp3("audio/"+alt[0]+".mp3")+AudioSegment.from_mp3("audio/"+alt[1]+".mp3")+AudioSegment.from_mp3("audio/"+alt[2]+".mp3")
            elif alt[1] != '0':
                fl=AudioSegment.from_mp3("audio/"+alt[1]+".mp3")+AudioSegment.from_mp3("audio/thousand.mp3")
                if alt[2] != '0':
                    fl=fl+AudioSegment.from_mp3("audio/"+alt[2]+".mp3")+AudioSegment.from_mp3("audio/hundred.mp3")
                fl=fl+AudioSegment.from_mp3("audio/feet.mp3")
            else:
                fl=AudioSegment.from_mp3("audio/"+alt[2]+".mp3")+AudioSegment.from_mp3("audio/hundred.mp3")+AudioSegment.from_mp3("audio/feet.mp3")

            if condition=="FEW":
                skycondition=skycondition+AudioSegment.from_mp3("audio/few.mp3")+AudioSegment.from_mp3("audio/clouds.mp3")+AudioSegment.from_mp3("audio/at.mp3")+fl
            elif condition=="SCT":
                skycondition=skycondition+AudioSegment.from_mp3("audio/scattered.mp3")+AudioSegment.from_mp3("audio/at.mp3")+fl
            elif condition=="BRK":
                skycondition=skycondition+AudioSegment.from_mp3("audio/broken.mp3")+AudioSegment.from_mp3("audio/at.mp3")+fl
            elif condition=="OVC":
                skycondition=skycondition+AudioSegment.from_mp3("audio/overcast.mp3")+AudioSegment.from_mp3("audio/at.mp3")+fl
                

    temperature_input=str(atis_data["temp"])
    temperature=AudioSegment.from_mp3("audio/temperature.mp3")+AudioSegment.from_mp3("audio/"+temperature_input[0]+".mp3")
    if len(temperature_input)>1:
        for i in range(1,len(temperature_input)):
            temperature=temperature+AudioSegment.from_mp3("audio/"+temperature_input[i]+".mp3")

    pressure=str(atis_data["press"])
    pressure=AudioSegment.from_mp3("audio/altimeter.mp3")+AudioSegment.from_mp3("audio/"+pressure[0]+".mp3")+AudioSegment.from_mp3("audio/"+pressure[1]+".mp3")+AudioSegment.from_mp3("audio/"+pressure[2]+".mp3")+AudioSegment.from_mp3("audio/"+pressure[3]+".mp3")

    runway=AudioSegment.empty()
    for runway_input in atis_data["rwy"]:
        runway_input=runway_input.lower()
        runway=runway+AudioSegment.from_mp3("audio/runway.mp3")+AudioSegment.from_mp3("audio/"+runway_input[0]+".mp3")+AudioSegment.from_mp3("audio/"+runway_input[1]+".mp3")
        if len(runway_input)>2:
            s=runway_input[2]
            if s=='l':
                runway=runway+AudioSegment.from_mp3("audio/left.mp3")
            elif s=='c':
                runway=runway+AudioSegment.from_mp3("audio/centre.mp3")
            elif s=='r':
                runway=runway+AudioSegment.from_mp3("audio/right.mp3")
    runway=runway+AudioSegment.from_mp3("audio/in_use.mp3")
    

    atis=information+time+wind+skycondition+temperature+pressure+runway+AudioSegment.from_mp3("audio/advise_controller_on_initial_contact_you_have.mp3")+AudioSegment.from_mp3("audio/"+atis_data["id"]+".mp3")
    atis.export(atis_data["icao"]+".mp3", format="mp3")

#The function takes one arguement which should be a dictionary with the following elements:
#"icao": The icao code for the airport for example, 'EGKK'
#"id": The title of the information, for example 't'
#"temp": The temperature
#"wind_dir": The wind direction as a heading, for example '175'
#"wind_speed": The wind speed
#"press": The altimeter pressure without a decimal, for example 29.92 would be '2992'
#"sky": The sky conditions as they would be in a METAR formatted as an array, for example ('FEW100','OVC180')
#"rwy": The runways in use in an array, for example ('09R','09C','09L','13')

atis_data = {
            "icao": "EGKK",
            "id": "f",
            "temp": "20",
            "wind_dir": "000",
            "wind_speed": "2",
            "press": "2992",
            "sky": ("FEW006","SCT090","BKN150","OVC195"),
            "rwy": ("08L","08R"),
        }

atis_gen(atis_data)

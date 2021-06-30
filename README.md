# ATIS-generator
To be used to create a basic ATIS for flight simulating communities or other such purposes

The programme is one function with 65 associated sound files, if you wish to create your own voice for the function rerecord the mp3s with the same titles. Feel free to add to the code allowing the user to select from different voices.

This function requires the pydub and datetime modules

To use simply load the function with a dictionary, for example:
    information = {
      "icao": "KJFK",
      "id": "y",
      "temp": "15",
      "wind_dir": "248",
      "wind_speed": "7",
      "press": "2992",
      "sky": ("NCD", " "),
      "rwy": ("05", " "),
   }
   atis_gen(information)

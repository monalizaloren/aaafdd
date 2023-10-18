final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
  features_list = []
  gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except: pass

  try:
    if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
      features_list.append("planet_type")
  except: pass
  
  try:
    if float(planet_data[8].split(" ")[0]) > 0.38 and float(planet_data[8].split(" ")[0]) < 2:
      features_list.append("goldilock")
  except: 
    try:
      if planet_data[8] > 0.38 and planet_data[8] < 2:
        features_list.append("goldilock")
    except: pass
  try:
    distance = 2 * 3.14 * (planet_data[8] * 1.496e+8)
    time = planet_data[9] * 86400
    speed = distance / time
    if speed < 200:
      features_list.append("speed")
  except: pass
  final_dict[planet_data[1]] = features_list

print(final_dict)

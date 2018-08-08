def extract(geocode_result):
    x = geocode_result[0]
    sub_x = x["geometry"]
    coord = sub_x['location']
    return coord




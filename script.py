import pandas as pd 
import numpy as np
import pickle 
from recommendations.models import Places 
from glob import glob 

def get_final_dict():
    # first get the df
    rgb_df = pd.read_csv('rgb_data.csv')
    rgb_df.drop('rgb' , inplace = True, axis = 1)

    with open('rgb_data.pickle',"rb") as fr: 
        df = pickle.load(fr)
    s = df['rgb'] 
    count = 0
    for index, value in s.iteritems():
        if count==0: 
            # first row
            val = value[0]
            #print(val, type(value), len(val))
            count+=1
        else:
            break

    rgb_df['rgb'] = s
    df_records = rgb_df.to_dict('records') 
    return df_records

#rgb_df is a df with numpy type in column rgb

#df_records = rgb_df.to_dict('records') 

"""f_records = get_final_dict()
count = 0 
for record in df_records: 
    if count == 0: 
        name = record['galtitle']
        image_url= record['galwebimageurl']
        rgb = record['rgb']
        p = Places(name = name, image_url = image_url,rgb = rgb)
        p.save()
    else: 
        break"""
def place_images():
    places_list = Places.objects.order_by("id")
    
    count = 0
    for place in places_list: 
        if count <5:
            count_str = str(count)
            img = 'photo370(num)/' + count_str +".jpg"
            place.image = img
            count += 1
            place.save()
    

def list_image_names(): 
    count =0 
    for file in glob('photo370(num)/*'):
        if count < 10: 
            print(file, type(file))
            count+=1






from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from .models import Foot_Traffic, UploadedImage, Places



from . import recommend
import numpy as np
import pandas as pd

#import recommend
# Create your views here.

def homePageView(request):
    if request.method == "POST":
        uploadedimage_instance = UploadedImage()

        #save image into the system 
        img = request.FILES['image']
        img_name = img.name
        print(img_name)

        #save image to a database
        uploadedimage_instance.image = img
        uploadedimage_instance.name = img_name
        uploadedimage_instance.save()

        img = 'static/media/images/'+img.name
        all_places = Places.objects.all()
        
        #here, use destination API to search for number of ppl 
        similarity_dict_t10 = recommend.get_top_10_similarity(img,all_places)
        print('similarity_dict is '+str(similarity_dict_t10))

        traffic_dict = {}
        count = 0
        for name in similarity_dict_t10.keys():
            if count == 0: 
                foot_traffic_objects = Foot_Traffic.objects.filter(place__name = name)
                print('foot_traffic_objects are '+ str(foot_traffic_objects))
                mean_traffic = foot_traffic_objects.aggregate(Avg('traffic_level'))
                print('mean traffic is '+ str(mean_traffic))
                traffic_dict[name] = mean_traffic
                count+=1

        print('traffic_dict is ') + str(traffic_dict)
        #top_three = traffic_dict[:3]
        #print(top_three)



        # get the bottom3 


        #show the three here 
        #render on template
        


    return render(request,'home.html')




"""
#compare all similarity scores
        similiarty_list = []
        for place in all_places: 
            matrix_B = place.rgb 
            name = place.name 
            url = place.url
            

            similarity_rate = euclid_dist(matrix_A,matrix_B)
            similarity_dict = {'name' : name , 'similarity_rate' : similarity_rate }
            similiarty_list.append(similarity_dict)
        
"""
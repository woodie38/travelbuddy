from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import UploadedImage,Places

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

        #save image to a database
        uploadedimage_instance.image = img
        uploadedimage_instance.name = img_name
        uploadedimage_instance.save()

        all_places = Places.objects.get_all()
        recommend.comp

        matrix_A = get_rgb(img)
        
        #compare all similarity scores
        similiarty_list = []
        for place in all_places: 
            matrix_B = place.rgb 
            name = place.name 
            url = place.url
            

            similarity_rate = euclid_dist(matrix_A,matrix_B)
            similarity_dict = {'name' : name , 'similarity_rate' : similarity_rate }
            similiarty_list.append(similarity_dict)
        
        #top_10_list = get_top_10(similiarty_list)
        
        #get the top_10_list of query objects 

        #here, use destination API to search for number of ppl 


        # get the bottom3 


        #show the three here 
        #render on template
        


    return render(request,'home.html')





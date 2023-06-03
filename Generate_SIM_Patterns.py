# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:05:34 2022

@author: Forest Speed
"""
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import cv2

arr1 = np.zeros((1080,1920),np.uint8)
arr2 = np.zeros((1080,1920),np.uint8)
arr3 = np.zeros((1080,1920),np.uint8)
arr4 = np.zeros((1080,1920),np.uint8)

DD_arr1 = np.zeros((1080,1920),np.uint8)
DD_arr2 = np.zeros((1080,1920),np.uint8)
DD_arr3 = np.zeros((1080,1920),np.uint8)


line_Width = 40 



# Traditional OS Pats
j = 1
while j < 1891 :
    i = 0 
    while i < 18 :
        arr1[:,i+j] = 1
        arr2[:,i+j+18] = 1
        arr3[:,i+j+36] = 1
        i = i + 1 
    j = j + 54
    

   
h = 1080
w = 1920
center = (960,540) 
radius = 336   
Y,X = np.ogrid[:h,:w]   
dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
mask = dist_from_center <= radius

mask_Arr = np.ones((1080,1920),np.uint8)
mask_Arr[~mask]=0

arr1 = arr1*mask_Arr*256
arr2 = arr2*mask_Arr*256
arr3 = arr3*mask_Arr*256




"""
# DANDAN Pats 10
j = 1
while j < 1850 :
    i = 0 
    while i < 10 :
        arr1[:,i+j] = 1
        arr2[:,i+j+10] = 1
        arr3[:,i+j+20] = 1
        arr4[:,i+j+30] = 1
        
        i = i + 1 
    j = j + 40
    
"""    
    
# DANDAN Pats 10
j = 1
while j < 1700 :
        i = 0 
        while i < 40 :
            arr1[:,i+j] = 1
            arr2[:,i+j+40] = 1
            arr3[:,i+j+80] = 1
            arr4[:,i+j+120] = 1
            
            i = i + 1 
        j = j + 160

DD_arr1 = arr1 + arr2;
DD_arr2 = arr1 + arr4;
DD_arr3 = arr3 + arr4;



h = 1080
w = 1920
center = (960,540) 
radius = 336   
Y,X = np.ogrid[:h,:w]   
dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
mask = dist_from_center <= radius

mask_Arr = np.ones((1080,1920),np.uint8)
mask_Arr[~mask]=0

# DD
arr1 = DD_arr1*mask_Arr*256
arr2 = DD_arr2*mask_Arr*256
arr3 = DD_arr3*mask_Arr*256


"""
# p-TI

TI1 = np.array(mask_Arr)*256 #Bottom Hemi
TI2 = np.array(mask_Arr)*256 #Top Hemi
TI3 = np.array(mask_Arr)*256 #Right Hemi
TI4 = np.array(mask_Arr)*256 #Left Hemi
TI5 = np.array(mask_Arr)*256 #BR
TI6 = np.array(mask_Arr)*256 #TL
TI7 = np.array(mask_Arr)*256 #TR
TI8 = np.array(mask_Arr)*256 #BL


j = 1 
while j < 1920:
    if j < 960:
        TI3[:,j] = 0
        TI5[:,j] = 0
        TI7[:,j] = 0
    if j > 960:
        TI4[:,j] = 0
        TI6[:,j] = 0
        TI8[:,j] = 0
    i = 0
    while i < 1080:
        if i < 540:
            TI1[i,:] = 0
            TI5[i,:] = 0
            TI8[i,:] = 0
            
        if i > 540:
            TI2[i,:] = 0
            TI6[i,:] = 0
            TI7[i,:] = 0
            
        

        i = i + 1
    j = j + 1   
    
        
TI1_im = Image.fromarray(TI8)
plt.imshow(TI1_im) 
#plt.imshow(TI2) 
    

im_M = Image.fromarray(mask_Arr)
#plt.imshow(im_M)

im1 = Image.fromarray(TI1)
im1.save("ti_pat/TI1.tif")

im2 = Image.fromarray(TI2)
im2.save("ti_pat/TI2.tif")

im3 = Image.fromarray(TI3)
im3.save("ti_pat/TI3.tif")

im4 = Image.fromarray(TI4)
im4.save("ti_pat/TI4.tif")

im5 = Image.fromarray(TI5)
im5.save("ti_pat/TI5.tif")

im6 = Image.fromarray(TI6)
im6.save("ti_pat/TI6.tif")

im7 = Image.fromarray(TI7)
im7.save("ti_pat/TI7.tif")

im8 = Image.fromarray(TI8)
im8.save("ti_pat/TI8.tif")






"""

arr_all = arr1+arr2+arr3



im1 = Image.fromarray(arr1)
im1.save("DD40_Pat_11.tif")

im2 = Image.fromarray(arr2)
im2.save("DD40_Pat_22.tif")

im3 = Image.fromarray(arr3)
im3.save("DD40_Pat_33.tif")

im_all = Image.fromarray(arr1+arr2+arr3)

#plt.imshow(im1)
#plt.imshow(im2)
#plt.imshow(im3)
plt.imshow(im_all)


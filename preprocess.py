#!/usr/bin/env python
import os
import cv2

# Preprocess the pos and neg image files by cropping and recoloring 

def preprocess(input_dir, output_dir, name_prefix, size):
    try:
        pic_num = 1
        for filename in os.listdir(input_dir):
            img = cv2.imread(input_dir+"/"+filename, cv2.IMREAD_GRAYSCALE)
            resized = cv2.resize(img, size)
            cv2.imwrite(output_dir+"/"+name_prefix+str(pic_num)+".jpg", resized)
            pic_num += 1
    except Exception as e:
        print(str(e))

preprocess("wenda", "wenda_pos", "wenda", (50,50))
preprocess("negatives", "negatives_preprocessed", "negatives", (100, 100))

def create_bg_txt(neg_folders_list):
    f = open("bg.txt", "w+")
    for folder in neg_folders_list:
        for filename in os.listdir(folder):
            f.write(folder+"/"+filename+"\n") 

create_bg_txt(["negatives_preprocessed"])

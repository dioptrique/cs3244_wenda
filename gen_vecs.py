#!/usr/bin/env python
import os


def create_vecs(pos_dir, vec_dir):
    for filename in os.listdir(pos_dir):
        os.system("mkdir info")
        # Create artificial distortions of one positive sample
        cmd = "opencv_createsamples -img "+pos_dir+"/"+filename+" -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 100"
        os.system(cmd)
        # Create vector file of all aritificially generated distortions from postitive sample
        just_filename = filename.replace('.jpg', '')
        cmd = "opencv_createsamples -info info/info.lst -num 100 -w 20 -h 20 -vec "+vec_dir+"/"+just_filename+"_positives.vec"
        os.system(cmd)
        os.system("rm -r info")

create_vecs("wenda_pos", "wenda_vec")

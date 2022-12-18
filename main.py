from pickle import dump
from hashlib import sha512
from androguard.misc import AnalyzeAPK
import os

import json
appstore = "aurora"#name of appstore folder
category = "Social"#name of category folder which resides inside the appstore folder
directory_in_str = "D:/CNS/apk/"+appstore+"/"+category+"/"#actual directory structure->D:Path_To_Your_APK_Folder/appstore/category/YourAPKFile.apk
directory = os.fsencode(directory_in_str)
if not os.path.exists(directory_in_str+'dex'):
    os.makedirs(directory_in_str+ 'dex')
    print("debug1")
d = {}
if not os.path.isfile(directory_in_str+"check.txt"): 
    print("debug2")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".apk"):
            d[filename]=0
    json.dump(d, open(directory_in_str+"check.txt",'w'))
d2 = json.load(open(directory_in_str+"check.txt"))
try:
    print("debug3")
    print(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if filename.endswith(".apk"):
            print(filename)
            print(d2[filename])
            if d2[filename] != 1:
                a, d, dx = AnalyzeAPK(directory_in_str+filename)
                version = a.get_androidversion_name()
                txtfilename = a.get_app_name()
                print("here3")
                if not os.path.exists(directory_in_str+'dex/'+txtfilename+'_'+version+'.txt'):
                    getalldex = a.get_all_dex()
                    with open(directory_in_str+'dex/'+txtfilename+'_'+version+'.txt', 'w') as f:
                        for x in getalldex:
                            f.write(str(x))
            d2[filename]=1
            continue
    json.dump(d2, open(directory_in_str+"check.txt",'w'))
except Exception as e:
    print(e)
    json.dump(d2, open(directory_in_str+"check.txt",'w'))

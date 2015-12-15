
from os import listdir
from os.path import isfile, join, isdir
import subprocess
import sys
import numpy as np
import numpy as np
from glob import glob
import matplotlib.image as mpimg
from random import shuffle
import pickle


def run_process(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, shell=True)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

########### Parse train images features ####################

def parse_train_feature_files():
    train_features_folder = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/overfeat/train_overfeat_default/"
    
    
    features_files = [ f for f in listdir(train_features_folder) if isfile(join(train_features_folder,f)) ] 
    
    features_file_id_file_path_dict = {} 
    for feature_file in features_files:
        file_id = (feature_file.split(".")[0] + "." + feature_file.split(".")[1])
        features_file_id_file_path_dict[file_id] = feature_file
    
    print len(features_file_id_file_path_dict)
    
    file_ids = features_file_id_file_path_dict.keys()
    shuffle(file_ids)
            # Sort the files so they match the labels
    target = np.array([1. if 'dog' in f else 0.
                       for f in file_ids],
                      dtype='float32')
                      
#    print target[1:10]
    
    image_ids_order = file_ids
    data = np.zeros((len(file_ids), 4096), dtype='float32')
    for n, im in enumerate(file_ids):
        file_name = features_file_id_file_path_dict[im]
        f_in = open(train_features_folder + file_name)
        lines = f_in.readlines()
        if len(lines) < 2:
            print "Bad image: " + file_name
        else:
    #    print len(lines[1].strip().split(" "))
    
            if len(lines[1].strip().split(" ")) != 4096:
                print "Bad image: " + file_name
                
            data[n, :] = [float(feat) for feat in lines[1].strip().split(" ")]
            if n % 1000 == 0:
                print 'Reading in image', n
    return data, target, image_ids_order
    
########### Parse test images features ####################

def parse_test_feature_files():
    test_features_folder = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/overfeat/test1_overfeat_default/"
        
    features_files = [ f for f in listdir(test_features_folder) if isfile(join(test_features_folder,f)) ]   
     
    print len(features_files)
    print features_files[1:10]    
    
    features_files = sorted(features_files, key=lambda x: int(x.split(".")[0]))
    print features_files[0:10]
    
    data = np.zeros((len(features_files), 4096), dtype='float32')
    for n, im in enumerate(features_files):        
        f_in = open(test_features_folder + im)
        lines = f_in.readlines()
        
        if len(lines[1].strip().split(" ")) != 4096:
            print "Bad image: " + im
            
        data[n, :] = [float(feat) for feat in lines[1].strip().split(" ")]
        if n % 1000 == 0:
            print 'Reading in image', n
    return data
    
########### Pickle ####################


x, y, image_ids_order = parse_train_feature_files()
#tst = parse_test_feature_files()

#pickle.dump(x, open('overfeat_saved_x.pkl', 'wb'))
#pickle.dump(y, open('overfeat_saved_y.pkl', 'wb'))
#pickle.dump(tst, open('overfeat_saved_tst.pkl', 'wb'))

pickle.dump(x, open('saved_x_second.pkl', 'wb'))
pickle.dump(y, open('saved_y_second.pkl', 'wb'))
pickle.dump(image_ids_order, open('saved_image_ids_order_second.pkl', 'wb'))



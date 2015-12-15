
from os import listdir
from os.path import isfile, join, isdir
import subprocess
import pickle
import numpy as np
#
def merge_train_file():
    x_overfeat = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/scripts/overfeat_saved_x_second.pkl', 'rb'))
    y_overfeat = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/scripts/overfeat_saved_y_second.pkl', 'rb'))
    saved_image_ids_overfeat = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/scripts/overfeat_saved_image_ids_order_second.pkl', 'rb'))
    #
    x_decaf = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_x_second.pkl', 'rb'))
    #y_decaf = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_y_second.pkl', 'rb'))
    saved_image_ids_decaf = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_image_ids_order_second.pkl', 'rb'))
    
    image_ids_decaf = [x.split("/")[-1].split(".")[0] + "." + x.split("/")[-1].split(".")[1] for x in saved_image_ids_decaf]
    image_ids_overfeat = saved_image_ids_overfeat
    
    print image_ids_overfeat[0]
    print image_ids_decaf[0]
    
    merged_features = np.zeros((len(x_overfeat), 8192), dtype='float32')
    
    for index_overfeat, overfeat_image_id in enumerate(image_ids_overfeat):
        index_decaf = image_ids_decaf.index(overfeat_image_id)
    #    print len(x_overfeat[index_overfeat])
    #    print len(x_decaf[index_decaf])
        merged_vector = np.append(x_overfeat[index_overfeat] , x_decaf[index_decaf])
    #    print len(merged_vector)
        merged_features[index_overfeat, :] = merged_vector
    #    print len(merged_features[index_overfeat, :])
    
    pickle.dump(merged_features, open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_x.pkl', 'wb'))
    pickle.dump(y_overfeat, open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_y.pkl', 'wb'))
    
    
def merge_test_file():
    tst_overfeat = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/scripts/overfeat_saved_tst.pkl', 'rb'))
    #
    tst_decaf = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_tst.pkl', 'rb'))
    #y_decaf = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_y_second.pkl', 'rb'))
    
    merged_features = np.zeros((len(tst_overfeat), 8192), dtype='float32')
    
    for index, tst_overfeat_feature in enumerate(tst_overfeat):
        print index
    #    print len(x_overfeat[index_overfeat])
    #    print len(x_decaf[index_decaf])
        merged_vector = np.append(tst_overfeat[index] , tst_decaf[index])
    #    print len(merged_vector)
        merged_features[index, :] = merged_vector
    #    print len(merged_features[index_overfeat, :])
    
    pickle.dump(merged_features, open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_tst.pkl', 'wb'))
   
   
merge_test_file()



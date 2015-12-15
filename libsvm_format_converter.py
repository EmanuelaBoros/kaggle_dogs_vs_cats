
from os import listdir
from os.path import isfile, join, isdir
import subprocess
import pickle

#x = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_x.pkl', 'rb'))
#y = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_y.pkl', 'rb'))
#
##x = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_x.pkl', 'rb'))
##y = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_y.pkl', 'rb'))
#
#output_file_path = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/libsvm/overfeat+decaf_train.libsvm"
#f_out = open(output_file_path, "w")
#for i, instance in enumerate(x):
#    print i
#    label = y[i]
#    if label == 0:
#        label = -1.
#    line = str(label)
#    for index, value in enumerate(instance):
#        line += " " + str(index + 1) + ":" + str(value)
#    f_out.write(line + "\n")
#    if i > 50000:
#        break
#f_out.close()

####### Test file ############"

#tst = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/decaf_sollution/kaggle-dogs-vs-cats-master/saved_tst.pkl', 'rb'))

tst = pickle.load(open('/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/pickle/overfeat+decaf_saved_tst.pkl', 'rb'))

output_file_path = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/libsvm/overfeat+decaf_test.libsvm"
f_out = open(output_file_path, "w")
for i, instance in enumerate(tst):   
    print i
    label = 0.   
    line = str(label)
    for index, value in enumerate(instance):
        line += " " + str(index + 1) + ":" + str(value)
    f_out.write(line + "\n")
    if i > 50000:
        break
f_out.close()

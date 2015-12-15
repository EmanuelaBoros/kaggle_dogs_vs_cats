
from os import listdir
from os.path import isfile, join, isdir
import subprocess
import sys


def run_process(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, shell=True)
    while(True):
      retcode = p.poll() 
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break


overfit_path = "/home/ema/Workspace/Tools/overfeat/src/overfeat"
input_folder = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/train_resized/"
intermediate_folder = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/train_resized_overfeat/"
output_folder = "/home/ema/Workspace/Projects/Kaggle/Dogs_vs_Cats/data/overfeat/train_overfeat_default/"

image_files = [ f for f in listdir(input_folder) if isfile(join(input_folder,f)) ] 
existing_features_files = [ f for f in listdir(output_folder) if isfile(join(output_folder,f)) ] 
existing_extracted_image_ids = [(f.split(".")[0] + "." + f.split(".")[1]) for f in existing_features_files]

remaining_image_ids = [(f.split(".")[0] + "." + f.split(".")[1]) for f in image_files if (f.split(".")[0] + "." + f.split(".")[1]) not in existing_extracted_image_ids]
remaining_image_ids = set(remaining_image_ids)
print len(remaining_image_ids)

for image_file in image_files:

    image_id = (image_file.split(".")[0] + "." + image_file.split(".")[1])
    if image_id in remaining_image_ids:
        image_file_path = input_folder + image_file
        output_file_path = output_folder + image_file + ".prediction"
        intermediate_file = intermediate_folder + image_file +  ".ppm"
        command_1 = "convert " + image_file_path +  " -resize 231x231! ppm:- > " + intermediate_file
      
        for line in run_process(command_1):
             print intermediate_file
             
        command_2 = overfit_path + " -f " + intermediate_file + " > " + output_file_path
        
        for line in run_process(command_2):
             print output_file_path


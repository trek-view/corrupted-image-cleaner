# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Author: hq@trekview.org
# Created: 2020-06-10
# Copyright: Trek View
# Licence: GNU AGPLv3
# -------------------------------------------------------------------------------

import subprocess
import shlex
import os
import shutil
import sys
from subprocess import Popen, PIPE

def checkImage(image_file):

          proc = Popen(['magick identify', '-verbose', image_file], stdout=PIPE, stderr=PIPE)
          out, err = proc.communicate()
          exitcode = proc.returncode
          return exitcode, out, err

def main(argv):
      
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        #back_percentage = sys.argv[3] 
        if not os.path.exists(output_dir):
               os.makedirs(output_dir)
        images_files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(input_dir):
            for file in f:
                images_files.append(os.path.join(r, file))
                             
        for image_file in images_files:

              code, output, error = checkImage(image_file)
              if str(code) !="0" or str(error, "utf-8") != "":
                print("ERROR " + image_file)
              else:
                print("OK " + image_file)
                shutil.copy2(image_file, output_dir)
  
print('staring...')  

if __name__ == '__main__':
    
     main(sys.argv[1:])    
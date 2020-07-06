# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Author: hq@trekview.org
# Created: 2020-06-10
# Copyright: Trek View
# Licence: GNU AGPLv3
# -------------------------------------------------------------------------------

import os
import shutil
from subprocess import Popen, PIPE, STDOUT
import argparse


def checkImage(image_file):
    proc = Popen(['magick', 'identify', '-verbose', '-format', '"%[fx:255*mean]"', image_file], stdout=PIPE, stderr=STDOUT)
    out, err = proc.communicate()
    exitcode = proc.returncode
    try:
        return exitcode, float(out.decode('utf-8').replace("\"", "")), err
    except:
        return 1, 0, err


def main(argv):
    input_dir = os.path.abspath(argv.input_path)
    output_dir = os.path.abspath(argv.output_path)
    try:
        min_range = float(argv.min_range)
        max_range = float(argv.max_range)
    except:
        input('You should input float value for min range and max range of mean.\n\nPress any key to quit...')
        exit()
        return
    # back_percentage = sys.argv[3]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    images_files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.abspath(input_dir)):
        for file in f:
            images_files.append(os.path.join(r, file))

    for image_file in images_files:

        code, output, error = checkImage(image_file)
        if str(code) != "0"\
                or (error and str(error, "utf-8") != "") \
                or (output <= min_range and output >= max_range):
            print("ERROR " + image_file)
        else:
            print("OK " + image_file)
            shutil.copy2(image_file, output_dir)


print('staring...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter not corrupt image')
    parser.add_argument('input_path',
                        action='store',
                        help='Path to input folder.')

    parser.add_argument('output_path',
                        action="store",
                        help='Path to output folder.')

    parser.add_argument('-min', '--min-range',
                        default='55',
                        action='store',
                        help='min value for mean value')

    parser.add_argument('-max', '--max-range',
                        action='store',
                        default='200',
                        help='max value for mean value')

    input_args = parser.parse_args()
    main(input_args)

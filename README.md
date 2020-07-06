# Corrupted Image Cleaner

## In one sentence

Command line Python script that 1) takes photo file or directory of photo files, 2) analyses against image magick identify to detect corruption, and 3) copies non-corrupt images into specified output directory.

## Why we built this

It has become clear that there is potential for videos and images to be corrupted on the camera for whatever reason (stitching issues, heat issue, etc).

However, if user uploading timelapse photos, this check is not performed.

Corrupted Image Cleaner takes a directory of photos and automatically removes any photos classified as corrupt.

_If you're looking for an alternative for video files, check out: https://ffmpeg.org/ffmpeg-filters.html#blackdetect._

## How it works

1. You provide a photo or directory of photos and, optionally, mean boundaries for corruption
2. [Image magick identify analyses the image providing an analysis of the image](https://imagemagick.org/script/identify.php). 
3. Image magick returns a response in binary format if image is corrupt or not (1 = corrupt), and also information about the colour of the image
4. The script takes non-corrupt images (response = 0 and within defined upper and lower mean bounds) and copies them into output directory specified (with all original metadata preserved)

**About image colour mean values**

Image magick identify (`magick identify --verbose IMAGE_FILE`) returns statistics on an image:

```
Image statistics:
    Overall:
      min: 0  (0)
      max: 32 (0.12549)
      mean: 13.6515 (0.0535352)
      standard deviation: 5.70764 (0.0223829)
      kurtosis: -0.479415
      skewness: 0.754623
      entropy: 0.742424
```

The mean value reports the mean average of red (0,255), green () and blue () values of image.

The lower the mean, the darker the image (0 is 100% black). The higher the mean, the lighter the image (255 is 100% white).

By default, anything between 55 and 200 is considered valid. 

You can also pass the `-min` and `-max` arguments if you need to adjust these boundaries.

## Requirements

### OS Requirements

Works on Windows, Linux and MacOS.

### Software Requirements

* Python version 3.6+
* [Imagemagick](https://imagemagick.org/script/download.php)

## Quick start guide

_Note for MacOS / Unix users_

Remove the double quotes (`"`) around any directory path shown in the examples. For example `"OUTPUT_1"` becomes `OUTPUT_1`.


### Command Line Arguments

* -min: (optional: default is 55)
	- value between 0 (black) and 255 (white) for minimum mean colour of image. Any photos below this value will be discarded.
* -max: (optional: default is 200)
	- value between 0 (black) and 255 (white) for maximum mean colour of image. Any photos above this value will be discarded.

### Examples

**Take a directory of panoramic images (`INPUT`) check for corrupted images and copy non corrupted images to output directory (`OUTPUT_1`):**

```
python image-cleaner.py "INPUT" "OUTPUT_1"
```

**Take a panoramic image (`INPUT/MULTISHOT_9996_000135.jpg`) check it for corruption and if not corrupt copy it to output directory (`OUTPUT_2`):**

```
python image-cleaner.py "INPUT/MULTISHOT_9996_000135.jpg" "OUTPUT_2"
```

**Take a directory of panoramic images (`INPUT`) check for corrupted images (that are completely black only `-min 1`) and copy non corrupted images to output directory (`OUTPUT_3`):**

```
python image-cleaner.py -min 1 "INPUT" "OUTPUT_3"
```

**Take a directory of panoramic images (`INPUT`) check for corrupted images (but include images that are very dark `-min 15`) and copy non corrupted images to output directory (`OUTPUT_4`):**

```
python image-cleaner.py -min 15 "INPUT" "OUTPUT_4"
```

**Take a directory of panoramic images (`INPUT`) check for corrupted images (but include images that are very light `-max 240`) and copy non corrupted images to output directory (`OUTPUT_5`):**

```
python image-cleaner.py -max 240 "INPUT" "OUTPUT_5"
```

## Support 

We offer community support for all our software on our Campfire forum. [Ask a question or make a suggestion here](https://campfire.trekview.org/c/support/8).

## License

Corrupted Image Cleaner is licensed under a [GNU AGPLv3 License](/LICENSE.txt).
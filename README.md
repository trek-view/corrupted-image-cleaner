# Corrupted Image Cleaner

## In one sentence

Command line Python script that 1) takes photo file or directory of photo files, 2) analyses against image magick identify to detect corruption, and 3) , copies non-corrupt images into specified output directory.

## Why we built this

It has become clear that there is potential for videos and images to be corrupted on the camera for whatever reason (stitching issues, heat issue, etc).

We can extract these when breaking videos into frames using ffmpeg (https://ffmpeg.org/ffmpeg-filters.html#blackdetect).

However, if user uploading timelapse photos, this check is not performed.

Corrupted Image Cleaner takes a directory of photos and automatically removes any photos classified as corrupt.

## How it works

1. You provide a photo or directory of photos
2. Corrupted images are identified using [image magick identify functionality](https://imagemagick.org/script/identify.php). 
3. Image magick returns a response in binary format if image is corrupt or not (1 = corrupt)
4. The script takes non-corrupt images (response = 0) and copies them into output directory specified (with all original metadata preserved)

## Requirements

### OS Requirements

Works on Windows, Linux and MacOS.

### Software Requirements

* Python version 3.6+
* [Imagemagick](https://imagemagick.org/script/download.php)


## Quick start guide

_Note for MacOS / Unix users_

Remove the double quotes (`"`) around any directory path shown in the examples. For example `"OUTPUT_1"` becomes `OUTPUT_1`.

**Take a directory of panoramic images (`INPUT`) check for corrupted images and copy non corrupted images to output directory (`OUTPUT_1`):**

```
python image-cleaner.py "INPUT" "OUTPUT_1"
```

**Take a panoramic image (`INPUT/MULTISHOT_9996_000135.jpg`) check it for corruption and if not corrupt copy it to output directory (`OUTPUT_2`):**

```
python image-cleaner.py "INPUT/MULTISHOT_9996_000135.jpg" "OUTPUT_1"
```

## Support 

We offer community support for all our software on our Campfire forum. [Ask a question or make a suggestion here](https://campfire.trekview.org/c/support/8).

## License

Corrupted Image Cleaner is licensed under a [GNU AGPLv3 License](/LICENSE.txt).
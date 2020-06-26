# Corrupted Image Cleaner

It has become clear that there is potential for videos and images to be corrupted on the camera for whatever reason (stitching issues, heat issue, etc)

We can extract these when breaking videos into frames using ffmpeg.

However, if user uploading timelapse photos, this check is not performed.

Corrupted Image Cleaner takes a directory of photos and automatically removes any photos classified as corrupt.

Corrupted images are identified using the percentage of black in an image. This is done using ffmpeg https://ffmpeg.org/ffmpeg-filters.html#blackdetect

Default value is 0.98 (% black) in ffmpeg for detection. We should use this value as the default, but also allow user to enter their own variable for this value on script input.

Script should output new directory copying all valid photos (with all metadata preserved) but ignore files identified as corrupt (over the % black threshold).
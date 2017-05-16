# sheepscale
Change electricsheep flam3 files to different resolutions.

    ./resize.py electricsheep.247.16021.flam3 1920 1080 > output.flam3

The flam3 genome files used by electricsheep have a default render size of 800x592 pixels. This is kind of small, and it's nice to render sheep (or frames thereof) in much higher resolution. This script tweaks the parameters in flam3 files to change the resolution to anything you want while adjusting the scale to show roughly the same amount of the original frame, even in the face of aspect ratio changes.

## Known bugs

The XML parser will "helpfully" sort all the XML tag attributes by name, munging the file way more than necessary. In an ideal world, I would find an XML processor that didn't do this.

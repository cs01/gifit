# gif it

a single file python script to convert videos to gif

## install

```bash
curl https://raw.githubusercontent.com/cs01/gifit/main/gifit.py -o gifit.py
chmod +x gifit.py
```

## use
```
./gifit.py myvideo
# creates myvideo.gif
```

## api
```
> ./gifit.py --help
usage: gifit.py [-h] [--output OUTPUT] [--fps FPS] video

Convert a video to gif with ffmpeg

positional arguments:
  video            path to video

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  output path to gif (defaults to video name with .gif
                   extension)
  --fps FPS        frames per second
  ```

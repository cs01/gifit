#! python3

"""Convert a video to gif with ffmpeg"""

import argparse
import logging
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import Optional

purple = "\033[95m"
gray = "\033[90m"
end = "\033[0m"


FORMAT = (
    purple + "%(levelname)s %(asctime)s line %(lineno)s> " + gray + "%(message)s" + end
)
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main() -> Optional[str]:
    """Convert a video to gif with ffmpeg"""
    if not shutil.which("ffmpeg"):
        return "ffmpeg must be installed and on your PATH"

    parser = argparse.ArgumentParser(description="Convert a video to gif with ffmpeg")
    parser.add_argument("video", help="path to video")
    parser.add_argument(
        "--output",
        help="output path to gif (defaults to video name with .gif extension)",
    )
    parser.add_argument("--fps", help="frames per second", default="12")

    args = parser.parse_args()
    video = args.video

    if args.output:
        output = Path(args.output)
    else:
        output = Path(f"{Path(video).stem}.gif")

    if output.suffix != ".gif":
        return f"Output path must end in .gif (got {output.suffix})"
    try:
        logger.info(f"Creating {output}")
        cmd = [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-i",
            video,
            "-filter_complex",
            f"[0:v] fps={args.fps}, split [a][b];[a] palettegen=stats_mode=full [p];[b][p] paletteuse=new=1",
            f"{output}",
        ]
        logger.info(f"Running {shlex.join(cmd)}")
        subprocess.run(
            cmd,
            check=True,
        )
        logger.info(f"Created {output}")
    except subprocess.CalledProcessError as e:
        logger.info("ffmpeg failed")
        return e
    return None


if __name__ == "__main__":
    exit(main())

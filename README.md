# 📸 Dynamic Photo Sequence Generator (Crescendo Effect)

A Python script that turns a folder of images into a dynamic, high-speed video sequence. It features a "Crescendo" effect (accelerating speed), random zoom/pan movements ("Ken Burns" effect), and automatic aspect ratio filling to prevent black bars.

## ✨ Features

* **Crescendo Mode:** Images start displaying slowly and progressively accelerate to max speed.
* **High-Speed Loop:** Optionally continues looping images at maximum speed after the crescendo.
* **Smart Auto-Fill:** Automatically crops and scales images to fill the screen (1920x1080 default) without distortion or black bars.
* **Dynamic Zoom:** Applies random, organic zoom and pan movements to every image.
* **Random or Chronological:** Choose to shuffle images or keep them sorted by date.
* **Robust Rendering:** Generates individual clips to prevent FFmpeg command-line overflow errors on Windows.

## 🛠️ Requirements

1.  **Python 3.x**: [Download Python](https://www.python.org/downloads/)
    * *Note: No external `pip` packages are required. The script uses standard libraries.*
2.  **FFmpeg**: This script relies on FFmpeg for video processing.

## 📥 Installation

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

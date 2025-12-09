# Dynamic Photo Sequence Generator

A Python script that creates high-speed, dynamic video sequences from your photos. It features a "Crescendo" effect (accelerating speed), organic Zoom/Pan movements, and automatic screen filling (no black bars!).

## Features

* **Crescendo Effect:** Images start slow and progressively speed up to a frenzy.
* **High-Speed Loop:** Optionally keeps looping the images at max speed after the crescendo.
* **Smart Auto-Fill:** Automatically scales and crops images to fill the screen (1920x1080 default).
* **Dynamic Zoom:** Applies random "Ken Burns" style zoom and pan effects.
* **Shuffle:** Randomize the order of your photos or keep them chronological.
* **Beginner Friendly:** No complex installation required if you follow the guide below.

---

## Prerequisites (Read this first!)

If you are new to Python or command lines, don't worry. Follow these two steps to prepare your computer.

### 1. Install Python
You need Python to run the script.
1.  Go to [python.org/downloads](https://www.python.org/downloads/).
2.  Click the yellow **"Download Python"** button.
3.  **IMPORTANT:** When running the installer, make sure to check the box that says **"Add Python to PATH"** at the bottom of the window before clicking "Install".

### 2. Get the "Engine" (FFmpeg)
This script uses a tool called FFmpeg to build the video. You don't need to install it deeply, just download it.
1.  Download the "Essentials" build here: [FFmpeg Essentials (.zip)](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).
2.  Open the downloaded ZIP file.
3.  Go into the folder `ffmpeg-...` -> then into `bin`.
4.  Find the file named `ffmpeg.exe`.
5.  **Copy** that file and keep it ready to paste into your project folder later.

---

## Installation

1.  **Download this Code:**
    * Click the green **Code** button at the top of this GitHub page.
    * Select **Download ZIP**.
    * Extract the ZIP file into a new folder on your computer (e.g., on your Desktop).

2.  **Add FFmpeg:**
    * Paste the `ffmpeg.exe` file (from the Prerequisites step) into this same folder.

**Your folder should look like this:**
```text
MyProjectFolder/
│
├── ffmpeg.exe         <-- You put this here
├── video_maker.py     <-- The script
└── README.md
```

## How to Use (The Easy Way)
Step 1: Initialize

1. Open your project folder.
2. The "Address Bar" Trick: Click on the address bar at the top of the file explorer (where it says Desktop > MyProjectFolder).
3. Type cmd and press Enter. A black window (terminal) will open inside that folder.
4. Type the following command and press Enter:

```text
python video_maker.py
```
The script will tell you it created a new folder called input_images. You can close the window.

Step 2: Add Photos

1. Go into the newly created input_images folder.
2. Paste all the photos you want to use in the video (.jpg, .png, etc.).

Step 3: Make the Video

1. Do the "Address Bar Trick" again (Step 1.2) to open the black window.
2. Run the command again:

```text
python video_maker.py
```
3. Wait for the process to finish. Your new video will appear in the main folder! 🎉

## Configuration

Want to change the speed, resolution, or turn off the zoom? Right-click on video_maker.py and select "Edit with Notepad" (or any text editor).

Look for this section at the top:

# --- MAIN CONFIGURATION ---
TARGET_FPS = 30 
OUTPUT_RESOLUTION = '1920x1080' # You can change to '1080x1920' for TikTok/Shorts

# --- BEHAVIOR ---
RANDOM_ORDER = 1       # 1 = Shuffle images, 0 = Sort by Date
ENABLE_ZOOM = 1        # 1 = ON, 0 = OFF (Static images)
CRESCENDO_MODE = 1     # 1 = Speed up over time, 0 = Constant speed

# --- TIMING (Seconds) ---
CRESCENDO_DURATION = 10   # How long the accelerating part lasts
FINAL_LOOP_DURATION = 5   # How long the max-speed loop lasts at the end

Save the file after making changes and run the script again.
Troubleshooting

"python is not recognized...": This means you didn't check the "Add Python to PATH" box when installing Python. Reinstall Python and make sure to check that box.

"FileNotFoundError... ffmpeg": This means ffmpeg.exe is not in the same folder as the script. Make sure it's right next to video_maker.py.

Video has black bars? The script handles this automatically! It uses "Aspect Fill" to crop and fill the screen, so no black bars should appear.

## License
Free to use and modify!

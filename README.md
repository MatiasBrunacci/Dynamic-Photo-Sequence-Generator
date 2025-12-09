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

--- MAIN CONFIGURATION ---  
TARGET_FPS: Defines the smoothness (fluidity) of the video.
- 30: Standard for web video.
- 60: Very fluid movement (the file size will be larger).

OUTPUT_RESOLUTION: The size and shape of the video (Width x Height).
- '1920x1080': Horizontal Full HD (YouTube, TV).
- '1080x1920': Vertical Full HD (TikTok, Instagram Reels, Shorts).

--- BEHAVIOR ---  
RANDOM_ORDER: Decides the order in which the photos appear.
- 1: Random. Photos are shuffled.
- 0: Chronological. Photos appear by creation date.

ENABLE_ZOOM: Activates movement in the photos.
- 1: Activated. Applies a smooth zoom and pan ("Ken Burns Effect").
- 0: Deactivated. Images remain static (faster processing).

CRESCENDO_MODE: Controls the sequence speed.
- 1: Acceleration Mode. Starts slow and ends very fast.
- 0: Constant Speed. All photos last the same duration.

--- TIMING (Seconds) ---  
CRESCENDO_DURATION: (In seconds) How long the section of the video lasts where the photos are accelerating.  
FINAL_LOOP_DURATION: (In seconds) How much extra time the video spends looping images at maximum speed at the end. If you set 0, the video ends right when the crescendo finishes.

Save the file after making changes and run the script again.

## Troubleshooting

"python is not recognized...": This means you didn't check the "Add Python to PATH" box when installing Python. Reinstall Python and make sure to check that box.

"FileNotFoundError... ffmpeg": This means ffmpeg.exe is not in the same folder as the script. Make sure it's right next to video_maker.py.

Video has black bars? The script handles this automatically! It uses "Aspect Fill" to crop and fill the screen, so no black bars should appear.

## License
Free to use and modify!

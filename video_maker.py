import subprocess
import os
import glob
import random
import time
import shutil
import itertools 

# ----------------------------------------------------------------------
# --- MAIN CONFIGURATION ---
# ----------------------------------------------------------------------

# If 'ffmpeg' is installed in the system, leave as 'ffmpeg'. 
# Otherwise, point to the executable path (e.g., "./ffmpeg.exe")
FFMPEG_PATH = 'ffmpeg' 

INPUT_FOLDER = './input_images' 
BASE_FILENAME = 'memory_flashback' 
TARGET_FPS = 30 
OUTPUT_RESOLUTION = '1920x1080' # 1920x1080 is wide Full HD. Set to '1280x720' for HD or '1080x1920' for TikTok/Reels

# --- BEHAVIOR SETTINGS ---

# 1 = Random Order (Shuffle), 0 = Date Order (Chronological)
RANDOM_ORDER = 1

# 1 = Enable Zoom/Pan effect, 0 = Static images (faster processing)
ENABLE_ZOOM = 1    

# 1 = Progressive acceleration (Crescendo), 0 = Constant speed
CRESCENDO_MODE = 1    

# --- TIMING SETTINGS ---

# Phase 1: How long the crescendo sequence lasts (seconds)
CRESCENDO_DURATION = 10  

# Phase 2: How long to loop at max speed after crescendo (seconds)
FINAL_LOOP_DURATION = 5          

# Used only if CRESCENDO_MODE = 0 (Constant speed)
STATIC_PHOTO_DURATION = 2         

# Zoom Intensity
ZOOM_MIN = 1.0   
ZOOM_MAX = 1.5   

# ----------------------------------------------------------------------

def get_unique_filename(base_name, fps):
    filename_pattern = f"{base_name}_{fps}fps"
    counter = 1
    while True:
        output_name = f"{filename_pattern}_{counter}.mp4"
        if not os.path.exists(output_name):
            return output_name
        counter += 1

def calculate_crescendo_durations(num_images, total_time, fps):
    min_dur = 1.0 / fps
    start_dur = (2 * total_time / num_images) - min_dur
    
    if start_dur < min_dur:
        return [min_dur] * num_images
    
    if num_images > 1:
        step = (start_dur - min_dur) / (num_images - 1)
    else:
        step = 0

    durations = []
    for i in range(num_images):
        d = start_dur - (i * step)
        durations.append(max(d, min_dur))
    return durations

def create_video_sequence(input_folder, base_name, fps, resolution, ffmpeg_path, 
                          enable_zoom, crescendo_mode, randomize, crescendo_time, loop_time, static_dur):
    
    # --- 1. Setup ---
    try:
        W, H = resolution.split('x')
    except ValueError:
        print("❌ Error: Resolution must be in format 'WIDTHxHEIGHT' (e.g., 1920x1080)")
        return

    TEMP_FOLDER = os.path.join(input_folder, 'temp_clips')
    
    if os.path.exists(TEMP_FOLDER):
        try: shutil.rmtree(TEMP_FOLDER)
        except: pass
    os.makedirs(TEMP_FOLDER)
    
    print(f"🎬 Starting process. Target Resolution: {W}x{H} (Aspect Fill)")
    
    # Get images
    EXTENSIONS = ('*.jpg', '*.jpeg', '*.png', '*.tiff', '*.bmp')
    image_files = []
    for ext in EXTENSIONS:
        image_files.extend(glob.glob(os.path.join(input_folder, ext)))
    
    if not image_files:
        print(f"❌ Error: No images found in '{input_folder}'.")
        return

    # --- ORDERING LOGIC ---
    if randomize:
        print("🔀 Order: RANDOM (Shuffling images...)")
        images_to_process = image_files.copy()
        random.shuffle(images_to_process)
    else:
        print("📅 Order: CHRONOLOGICAL (By Date)")
        images_to_process = sorted(image_files, key=os.path.getmtime)

    num_imgs_orig = len(images_to_process)
    
    # --- 2. Build Render Queue ---
    render_queue = []

    # A) Crescendo Phase
    if crescendo_mode:
        crescendo_durs = calculate_crescendo_durations(num_imgs_orig, crescendo_time, fps)
        for i in range(num_imgs_orig):
            render_queue.append({'path': images_to_process[i], 'duration': crescendo_durs[i]})
    else:
        for i in range(num_imgs_orig):
            render_queue.append({'path': images_to_process[i], 'duration': static_dur})

    # B) Loop Phase (High Speed)
    if loop_time > 0:
        min_dur = 1.0 / fps
        loop_frame_count = int(loop_time * fps)
        print(f"   Generating extra frames for high-speed loop ({loop_time}s)...")
        img_iterator = itertools.cycle(images_to_process)
        for _ in range(loop_frame_count):
            render_queue.append({'path': next(img_iterator), 'duration': min_dur})

    total_clips = len(render_queue)
    print(f"🔨 Total clips to render: {total_clips}")

    # --- 3. Render Individual Clips ---
    clip_filenames = []
    
    for i, item in enumerate(render_queue):
        img_path = item['path']
        duration = item['duration']
        clip_name = os.path.join(TEMP_FOLDER, f"clip_{i:05d}.mp4")
        clip_filenames.append(clip_name)
        
        # Aspect Fill Filter: Scale to cover + Center Crop
        scale_crop_filter = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
                             f"crop={W}:{H}:(iw-ow)/2:(ih-oh)/2")

        if enable_zoom:
            z_start = random.uniform(ZOOM_MIN, ZOOM_MAX)
            z_end = random.uniform(ZOOM_MIN, ZOOM_MAX)
            x_pos = random.uniform(0, 1)
            y_pos = random.uniform(0, 1)
            frames_dur = int(duration * fps) + 5 
            
            zoom_expr = f"{z_start}+({z_end}-{z_start})*on/duration"
            
            # Apply crop first, then zoom
            vf = (f"{scale_crop_filter},"
                  f"zoompan=z='{zoom_expr}':"
                  f"x='iw/2*{x_pos}':y='ih/2*{y_pos}':"
                  f"d={frames_dur}:s={resolution}:fps={fps}")
        else:
            vf = scale_crop_filter

        cmd = [
            ffmpeg_path, '-y',
            '-loop', '1',
            '-i', os.path.abspath(img_path),
            '-vf', vf,
            '-c:v', 'libx264',
            '-t', f"{duration:.5f}",
            '-pix_fmt', 'yuv420p',
            '-r', str(fps),
            clip_name
        ]
        
        # Run FFmpeg silently
        try:
            subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
             print(f"\n❌ CRITICAL ERROR: FFmpeg executable not found at '{ffmpeg_path}'.")
             print("Please install FFmpeg or place 'ffmpeg.exe' in this folder.")
             return

        if i % 10 == 0 or i == total_clips - 1:
            percent = (i + 1) / total_clips * 100
            print(f"   Rendering... {percent:.1f}% ({i+1}/{total_clips})")

    # --- 4. Concatenate Clips ---
    print("🔗 Stitching clips together...")
    LIST_FILE = 'concat_list.txt'
    with open(LIST_FILE, 'w') as f:
        for clip in clip_filenames:
            clip_abs = os.path.abspath(clip).replace('\\', '/')
            f.write(f"file '{clip_abs}'\n")
    
    output_file = get_unique_filename(base_name, fps)
    
    cmd_concat = [
        ffmpeg_path, '-y', '-f', 'concat', '-safe', '0',
        '-i', LIST_FILE, '-c', 'copy', output_file
    ]
    
    try:
        subprocess.run(cmd_concat, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"\n✅ SUCCESS! Video created: {output_file}")
    except subprocess.CalledProcessError as e:
        print("\n❌ Error stitching video:")
        print(e.stderr.decode())

    # --- 5. Cleanup ---
    if os.path.exists(LIST_FILE): os.remove(LIST_FILE)
    try: shutil.rmtree(TEMP_FOLDER)
    except: pass
    print("🧹 Temporary files cleaned.")

if __name__ == "__main__":
    if not os.path.exists(INPUT_FOLDER):
        print(f"⚠️ Creating input folder '{INPUT_FOLDER}'...")
        os.makedirs(INPUT_FOLDER)
        print("👉 Please put your images inside the 'input_images' folder and run this script again.")
    else:
        create_video_sequence(
            INPUT_FOLDER, 
            BASE_FILENAME, 
            TARGET_FPS, 
            OUTPUT_RESOLUTION, 
            FFMPEG_PATH,
            ENABLE_ZOOM,
            CRESCENDO_MODE,
            RANDOM_ORDER,
            CRESCENDO_DURATION,
            FINAL_LOOP_DURATION,
            STATIC_PHOTO_DURATION
        )
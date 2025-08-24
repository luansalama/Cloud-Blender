#!/usr/bin/env python3
"""
Simple Blender Render Script for Saturn Cloud.
This script just opens a .blend file and renders it using all its saved settings.
"""

import bpy
import sys
import os

def main():
    print("=== Starting Blender Render ===")
    
    # The path to your .blend file is passed as the first argument after '--'
    # e.g., -- /home/saturn/.saturn/Cloud-Blender/my_animation.blend
    if len(sys.argv) > 5: # Blender's own arguments are first, ours come after
        blend_file_path = sys.argv[5] # This captures the first argument after '--'
    else:
        # If no argument was provided, try a default path for debugging
        blend_file_path = '/home/saturn/.saturn/Cloud-Blender/my_animation.blend'
        print(f"No file path provided. Using default: {blend_file_path}")

    # Check if the file exists before trying to open it
    if not os.path.exists(blend_file_path):
        print(f"ERROR: The blend file was not found at: {blend_file_path}")
        print("Current directory:", os.getcwd())
        print("Files here:", os.listdir('.'))
        sys.exit(1) # Exit with an error code

    # Print the file we are loading for the log
    print(f"Loading blend file: {blend_file_path}")
    
    # Clear the default scene and load your project file
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    
    # Your .blend file's settings (output path, frame range, resolution, etc.)
    # are already configured. We just need to start the render.
    scene = bpy.context.scene
    print(f"Rendering to: {scene.render.filepath}")
    print(f"Rendering frames: {scene.frame_start} to {scene.frame_end}")
    
    # Perform the render using the scene's settings
    print("Starting render...")
    bpy.ops.render.render(animation=True)
    print("=== Render Finished Successfully! ===")

if __name__ == "__main__":
    main()
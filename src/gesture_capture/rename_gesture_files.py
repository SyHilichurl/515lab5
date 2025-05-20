"""
Rename Gesture Files - CSV File Renamer

This script renames gesture CSV files from data/gesture/[o|v|z] directories
and moves them to data/gestures with appropriate labels.

Usage:
    python rename_gesture_files.py [options]

Options:
    --input DIR      Base input directory (default: "data/gesture")
    --output DIR     Output directory for renamed files (default: "data/gestures")
"""

import os
import argparse
from datetime import datetime
import shutil

def ensure_directory(directory):
    """
    Create directory if it doesn't exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def process_gesture_files(base_input_dir, output_dir):
    """
    Process gesture files from o, v, z subdirectories and move them to output directory.
    
    Args:
        base_input_dir (str): Base directory containing o, v, z subdirectories
        output_dir (str): Directory to move renamed files to
    """
    if not os.path.exists(base_input_dir):
        print(f"Error: Base input directory {base_input_dir} does not exist")
        return
    
    # Create output directory if it doesn't exist
    ensure_directory(output_dir)
    
    # Process each gesture type directory
    for gesture_type in ['o', 'v', 'z']:
        input_dir = os.path.join(base_input_dir, gesture_type)
        
        if not os.path.exists(input_dir):
            print(f"Warning: Directory {input_dir} does not exist, skipping...")
            continue
        
        # Get all CSV files in the directory
        files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
        
        if not files:
            print(f"No CSV files found in {input_dir}")
            continue
        
        # Sort files by creation time
        files.sort(key=lambda x: os.path.getctime(os.path.join(input_dir, x)))
        
        # Rename and move files
        for i, file in enumerate(files, 1):
            old_path = os.path.join(input_dir, file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"{gesture_type}_output_{i}_{timestamp}.csv"
            new_path = os.path.join(output_dir, new_name)
            
            try:
                # Move and rename the file
                shutil.move(old_path, new_path)
                print(f"Moved and renamed: {file} -> {new_name}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Rename gesture CSV files")
    parser.add_argument("--input", default="data/gesture", help="Base input directory containing o, v, z subdirectories")
    parser.add_argument("--output", default="data/gestures", help="Output directory for renamed files")
    args = parser.parse_args()
    
    # Process files
    process_gesture_files(args.input, args.output)

if __name__ == "__main__":
    main() 
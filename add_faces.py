# Updated add_faces.py with proper spacing and formatting

import cv2
import os

# Function to add faces

def add_faces(faces_dir):
    i = 0
    framesTotal = 51
    
    for filename in os.listdir(faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Process each file
            img_path = os.path.join(faces_dir, filename)
            image = cv2.imread(img_path)
            # Perform operations on the image
            i += 1
    
    return i

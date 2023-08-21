import tkinter as tk
from tkinter import filedialog
import CameraCalibration_FunctionaProgramming as func
import json
from datetime import datetime  # Import the datetime module for getting the current date and time
import glob
import os
import numpy as np


class ImageLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Loader App")
        self.calibration_images = []
        self.images_to_undistort = []
        self.camera_matrix = []
        self.distortion_coefficients = []
        self.new_camera_matrix = []
        
        # Create two sections in the grid layout
        self.create_widgets()
        
    def create_widgets(self):

        # Create a frame for each section
        section_frame = tk.Frame(self.root, padx=10, pady=10)
        section_frame.grid(row=0, column=0, padx=10, pady=10)

        #Cali_title
        self.calibration_title = tk.Label(section_frame, text="Calbration Images", font= ("helvetica",20) )
        self.calibration_title.grid(row=0, column=0, padx=10, pady=10)
        
        # Create buttons for loading images and running a function
        self.load_calibration_images_button = tk.Button(section_frame, text="Load Calibration Images", command=lambda: self.load_image('A'))
        #load_image_button_A.pack(pady=5)
        self.load_calibration_images_button.grid(row=1, column=0,padx=10, pady=10)

        self.run_calibration_button = tk.Button(section_frame, text="Calibrate", command=lambda: self.run_function('A'))
        self.run_calibration_button.grid(row=2, column=0,padx=10, pady=10)

        # Display the number of selected images
        self.num_calibration_images = tk.Label(section_frame, text="Number of Calibration Images Selected: 0")
        self.num_calibration_images.grid(row=3, column=0,padx=10, pady=10)

        #flatten_title
        self.flatten_title = tk.Label(section_frame, text="Flatten Images", font= ("helvetica",20) )
        self.flatten_title.grid(row=0, column=1, padx=10, pady=10)

        self.load_flatten_images_button = tk.Button(section_frame, text="Load Flatten Images", command=lambda: self.load_image('B'))
        self.load_flatten_images_button.grid(row=1, column=1,padx=10, pady=10)

        self.run_flatten_button = tk.Button(section_frame, text="Flatten", command=lambda: self.run_function('B'))
        self.run_flatten_button.grid(row=2, column=1,padx=10, pady=10)

        # Display the number of selected images
        self.num_flatten_images = tk.Label(section_frame, text="Number of Flatten Images Selected: 0")
        self.num_flatten_images.grid(row=3, column=1,padx=10, pady=10)
        
    def load_image(self, button):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_paths:
            if button == "A":
                # Add the selected images to the list
                self.calibration_images.extend(file_paths)
                num_selected = len(self.calibration_images)
                self.num_calibration_images.config(text=f"Number of Images Selected: {num_selected}")
                print(self.calibration_images)
            elif button == "B":
                # Add the selected images to the list
                self.images_to_undistort.extend(file_paths)
                num_selected = len(self.images_to_undistort)
                self.num_flatten_images.config(text=f"Number of Images Selected: {num_selected}")
                print(self.images_to_undistort)

            
    def run_function(self, function):
        
        if function == "A": 
            self.camera_matrix, self.distortion_coefficients, self.new_camera_matrix = func.get_camera_matrix_and_distortion_coefficients(self.calibration_images)
            
            # Save the variables to a JSON file
            calibration_data = {
                "Camera Matrix": self.camera_matrix.tolist(),
                "Distortion Coefficients": self.distortion_coefficients.tolist(),
                "New Camera Matrix": self.new_camera_matrix.tolist()
            }
                    
             # Create a filename with the current date and time
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
            calibration_data_filename = f"calibration_data_{date_string}.json"

            with open(calibration_data_filename, "w") as json_file:
                json.dump(calibration_data, json_file, indent=2, separators=(',',':'))
        elif function =="B":
            # Find the most recent calibration data JSON file to extract data and load into flatten function
            calibration_data_files = glob.glob("calibration_data_*.json")
            if calibration_data_files:
                most_recent_calibration_file = max(calibration_data_files, key=os.path.getctime)
                
                # Load calibration data from the JSON file
                with open(most_recent_calibration_file, "r") as json_file:
                    calibration_data = json.load(json_file)
                    flatten_camera_matrix = np.array(calibration_data["Camera Matrix"])
                    flatten_distortion_coefficients = np.array(calibration_data["Distortion Coefficients"])
                    flatten_new_camera_matrix = np.array(calibration_data["New Camera Matrix"])
                    # Pass the calibration data to the correct_images function
                    func.correct_images(self.images_to_undistort, flatten_camera_matrix, flatten_distortion_coefficients, flatten_new_camera_matrix)



            #func.correct_images(self.images_to_undistort,self.camera_matrix,self.distortion_coefficients, self.new_camera_matrix)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog
import CameraCalibration_FunctionaProgramming as func

class ImageLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Loader App")
        self.calibration_images = []
        self.images_to_undistort = []
        
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
        self.load_image_button_A = tk.Button(section_frame, text="Load Calibration Images", command=lambda: self.load_image('A'))
        #load_image_button_A.pack(pady=5)
        self.load_image_button_A.grid(row=1, column=0,padx=10, pady=10)

        self.run_function_button_A = tk.Button(section_frame, text="Calibrate", command=lambda: self.run_function('A'))
        self.run_function_button_A.grid(row=2, column=0,padx=10, pady=10)

        # Display the number of selected images
        self.num_selected_label_A = tk.Label(section_frame, text="Number of Calibration Images Selected: 0")
        self.num_selected_label_A.grid(row=3, column=0,padx=10, pady=10)

        #flatten_title
        self.flatten_title = tk.Label(section_frame, text="Flatten Images", font= ("helvetica",20) )
        self.flatten_title.grid(row=0, column=1, padx=10, pady=10)

        self.load_image_button_B = tk.Button(section_frame, text="Load Flatten Images", command=lambda: self.load_image('B'))
        self.load_image_button_B.grid(row=1, column=1,padx=10, pady=10)

        self.run_function_button_B = tk.Button(section_frame, text="Flatten", command=lambda: self.run_function('B'))
        self.run_function_button_B.grid(row=2, column=1,padx=10, pady=10)

        # Display the number of selected images
        self.num_selected_label_B = tk.Label(section_frame, text="Number of Flatten Images Selected: 0")
        self.num_selected_label_B.grid(row=3, column=1,padx=10, pady=10)
        
    def load_image(self, button):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_paths:
            if button == "A":
                # Add the selected images to the list
                self.calibration_images.extend(file_paths)
                num_selected = len(self.calibration_images)
                self.num_selected_label_A.config(text=f"Number of Images Selected: {num_selected}")
                print(self.calibration_images)
            elif button == "B":
                # Add the selected images to the list
                self.images_to_undistort.extend(file_paths)
                num_selected = len(self.images_to_undistort)
                self.num_selected_label_B.config(text=f"Number of Images Selected: {num_selected}")
                print(self.images_to_undistort)

            
    def run_function(self, function):
        # Replace this function with your own implementation
        if function == "A": 
            func.get_camera_matrix_and_distortion_coefficients(self.calibration_images)
        elif function =="B":
            func.correct_images(self.images_to_undistort)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()

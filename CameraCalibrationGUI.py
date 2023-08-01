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
        
        # Create buttons for loading images and running a function
        load_image_button_A = tk.Button(section_frame, text="Load Image A", command=lambda: self.load_image('A'))
        load_image_button_A.pack(pady=5)

        run_function_button_A = tk.Button(section_frame, text="Run Function A", command=lambda: self.run_function('A'))
        run_function_button_A.pack(pady=5)

        # Display the number of selected images
        self.num_selected_label_A = tk.Label(section_frame, text="Number of Images Selected: 0")
        self.num_selected_label_A.pack(pady=5)

        load_image_button_B = tk.Button(section_frame, text="Load Image B", command=lambda: self.load_image('B'))
        load_image_button_B.pack(pady=5)

        run_function_button_B = tk.Button(section_frame, text="Run Function B", command=lambda: self.run_function('B'))
        run_function_button_B.pack(pady=5)

        # Display the number of selected images
        self.num_selected_label_B = tk.Label(section_frame, text="Number of Images Selected: 0")
        self.num_selected_label_B.pack(pady=5)
        
    def load_image(self, function):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_paths:
            # Add the selected images to the list
            self.calibration_images.extend(file_paths)
            num_selected = len(self.calibration_images)
            self.num_selected_label.config(text=f"Number of Images Selected: {num_selected}")
            
    def run_function(self, function):
        # Replace this function with your own implementation
        func.get_camera_matrix_and_distortion_coefficients(self.calibration_images)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()

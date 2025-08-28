import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
from tkinter import ttk
import model

class YOLOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Senko/Shiro/Sora Sorter")
        
        # pathes
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input for folder with images
        ttk.Label(self.root, text="Folder with images:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(self.root, textvariable=self.input_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="View", command=self.browse_input).grid(row=0, column=2, padx=5, pady=5)
        
        # Input for results folder
        ttk.Label(self.root, text="Folder for results:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(self.root, textvariable=self.output_path, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="View", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)
        
        # Button "Launch"
        self.run_button = ttk.Button(self.root, text="Launch", command=self.start_processing)
        self.run_button.grid(row=2, column=1, pady=10)
        
        # Logs
        self.log_text = tk.Text(self.root, height=5, width=60)
        self.log_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    
    def browse_input(self):
        folder = filedialog.askdirectory(title="Choose folder with images")
        if folder:
            self.input_path.set(folder)
    
    def browse_output(self):
        folder = filedialog.askdirectory(title="Choose folder for results")
        if folder:
            self.output_path.set(folder)
    
    def log_message(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)
    
    def process_images(self):
        input_folder = self.input_path.get()
        output_folder = self.output_path.get()
        
        self.log_message("Starting...")
        self.log_message("My image processing speed is ~275 images per minute")
    
        model.main(input_folder, output_folder)
    
        self.log_message("Processing complete!")
    
    def start_processing(self):
        if not self.input_path.get() or not self.output_path.get():
            messagebox.showerror("ERROR", "Choose two folders!")
            return
        
        thread = threading.Thread(target=self.process_images)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOApp(root)
    root.mainloop()
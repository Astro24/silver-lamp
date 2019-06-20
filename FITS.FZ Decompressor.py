import os
import subprocess
import tkinter as tk
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 700, height = 700,)
canvas1.pack()

target_directory = 'C:/jah/' # change this as required
target_write_directory = 'C:/this/'

def begin_wombocombo(): #Is function for first button
    zipped_files = [x for x in os.listdir(target_directory)if x.lower().endswith('.fits.fz')]
    for filename in zipped_files:
        print(os.path.abspath(filename))
        subprocess.call([r'C:/SAOImageDS9/ds9.exe', os.path.abspath(filename), '-savefits', os.path.abspath(target_write_directory + filename[:-3]), '-exit'])

createBatButton = tk.Button (root, text = '          Create Bat              ', command = begin_wombocombo)
canvas1.create_window(350,320, window = createBatButton)

root.mainloop()

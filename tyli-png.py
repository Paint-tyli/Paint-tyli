import json
from PIL import Image, ImageDraw
from tkinter import Tk, filedialog, Button

def convert_tyli_to_png(tyli_path, png_path):
    with open(tyli_path, 'r') as file:
        lines = json.load(file)

    image = Image.new('RGB', (800, 600), 'white')
    draw = ImageDraw.Draw(image)

    for line in lines:
        draw.line(line[:4], fill=line[4])

    image.save(png_path)

def open_file_dialog():
    Tk().withdraw()
    tyli_path = filedialog.askopenfilename()
    png_path = filedialog.asksaveasfilename(defaultextension=".png")
    convert_tyli_to_png(tyli_path, png_path)

if __name__ == "__main__":
    root = Tk()
    Button(root, text="Konwertuj plik TYLI do PNG", command=open_file_dialog).pack()
    root.mainloop()

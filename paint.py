import json
import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.old_x = None
        self.old_y = None
        self.pen_color = 'black'
        self.pen_width = 5
        self.lines = []
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        color_button = tk.Button(self.root, text='Kolor', command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        erase_button = tk.Button(self.root, text='Gumka', command=self.use_eraser)
        erase_button.pack(side=tk.LEFT)

    def draw(self, event):
        if self.old_x and self.old_y:
            line = (self.old_x, self.old_y, event.x, event.y, self.pen_color)
            self.lines.append(line)
            self.canvas.create_line(*line[:4], width=self.pen_width, fill=line[4], capstyle=tk.ROUND, smooth=True)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

    def use_eraser(self):
        self.pen_color = 'white'

    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.tyli')
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.lines, file)

    def load_drawing(self):
        file_path = filedialog.askopenfilename(filetypes=[('TYLI files', '*.tyli')])
        if file_path:
            with open(file_path, 'r') as file:
                self.lines = json.load(file)
            self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.delete('all')
        for line in self.lines:
            self.canvas.create_line(*line[:4], width=self.pen_width, fill=line[4], capstyle=tk.ROUND, smooth=True)

    def run(self):
        save_button = tk.Button(self.root, text='Zapisz', command=self.save_drawing)
        save_button.pack(side=tk.LEFT)

        load_button = tk.Button(self.root, text='Wczytaj', command=self.load_drawing)
        load_button.pack(side=tk.LEFT)

        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    PaintApp(root).run()

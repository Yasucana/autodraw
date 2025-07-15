import tkinter as tk
from tkinter import filedialog
import random
from PIL import Image, ImageDraw, ImageTk

WIDTH, HEIGHT = 800, 600

class AbstractApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoAbstractor")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.style_var = tk.StringVar(value="Style A")
        tk.OptionMenu(root, self.style_var, "Style A", "Style B").pack(side=tk.LEFT, padx=5)

        tk.Button(root, text="Generate", command=self.generate).pack(side=tk.LEFT, padx=5)
        tk.Button(root, text="Save", command=self.save_image).pack(side=tk.LEFT, padx=5)

        self.image = Image.new("RGB", (WIDTH, HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

    def generate(self):
        self.image = Image.new("RGB", (WIDTH, HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

        style = self.style_var.get()
        self.canvas.delete("all")

        if style == "Style A":
            self.draw_geometric_lines()
        elif style == "Style B":
            self.draw_colored_polygons()

        self.display_image()

    def draw_geometric_lines(self):
        steps = 40
        for i in range(steps):
            self.draw.line([(0, i * HEIGHT // steps), (i * WIDTH // steps, HEIGHT)], fill="black", width=1)
            self.draw.line([(WIDTH, i * HEIGHT // steps), (WIDTH - i * WIDTH // steps, HEIGHT)], fill="black", width=1)

    def draw_colored_polygons(self):
        for _ in range(20):
            points = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
            color = tuple(random.choices(range(256), k=3))
            self.draw.polygon(points, fill=color, outline="black")

    def display_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def save_image(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
        if path:
            self.image.save(path)

if __name__ == "__main__":
    root = tk.Tk()
    app = AbstractApp(root)
    root.mainloop()

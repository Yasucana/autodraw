import tkinter as tk
from tkinter import filedialog
import random
import math
from PIL import Image, ImageDraw, ImageTk

WIDTH, HEIGHT = 800, 600

class AbstractApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoAbstractor")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.style_var = tk.StringVar(value="Style A")
        tk.OptionMenu(
            root,
            self.style_var,
            "Style A",
            "Style B",
            "Style C",
            "Style D",
            "Style E",
            "Style F",
            "Style G",
        ).pack(side=tk.LEFT, padx=5)

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
        elif style == "Style C":
            self.draw_modern_tribal()
        elif style == "Style D":
            self.draw_mandala()
        elif style == "Style E":
            self.draw_abstract_expressionism()
        elif style == "Style F":
            self.draw_dot_spiral()
        elif style == "Style G":
            self.draw_psychedelic_doodles()

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

    def draw_modern_tribal(self):
        for _ in range(15):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            r = random.randint(20, 80)
            color = tuple(random.choices(range(256), k=3))
            start = random.choice([0, 180])
            self.draw.arc([x - r, y - r, x + r, y + r], start, start + 180, fill=color, width=3)
            for i in range(3):
                offset = i * 5 - 5
                self.draw.line([(x - r, y + offset), (x + r, y + offset)], fill=color, width=2)
            for _ in range(5):
                dx = random.randint(-r // 2, r // 2)
                dy = random.randint(0, r // 2)
                self.draw.ellipse([x + dx - 2, y + dy - 2, x + dx + 2, y + dy + 2], fill=color)

    def draw_mandala(self):
        center = (WIDTH // 2, HEIGHT // 2)
        layers = 6
        for layer in range(1, layers + 1):
            radius = layer * 40
            color = tuple(random.choices(range(256), k=3))
            self.draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline=color, width=2)
            for i in range(12):
                angle = math.radians(i * 30)
                x = center[0] + radius * math.cos(angle)
                y = center[1] + radius * math.sin(angle)
                self.draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=color)

    def draw_abstract_expressionism(self):
        for _ in range(30):
            x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            color = tuple(random.choices(range(256), k=3))
            width = random.randint(5, 20)
            self.draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
            if random.random() < 0.3:
                drip_len = random.randint(10, 60)
                self.draw.line([(x2, y2), (x2, y2 + drip_len)], fill=color, width=max(1, width - 3))

    def draw_dot_spiral(self):
        center = (WIDTH / 2, HEIGHT / 2)
        angle = 0
        for i in range(150):
            radius = i * 2
            angle += 0.3
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            color = tuple(random.choices(range(256), k=3))
            self.draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=color)

    def draw_psychedelic_doodles(self):
        for _ in range(50):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            radius = random.randint(20, 100)
            start = random.randint(0, 360)
            end = start + random.randint(60, 300)
            color = tuple(random.randint(128, 255) for _ in range(3))
            self.draw.arc([x - radius, y - radius, x + radius, y + radius], start, end, fill=color, width=3)
            for _ in range(3):
                dx = random.randint(-radius, radius)
                dy = random.randint(-radius, radius)
                self.draw.line([(x, y), (x + dx, y + dy)], fill=color, width=2)

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

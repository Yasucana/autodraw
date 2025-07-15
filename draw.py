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

        # style selection and parameter controls
        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.LEFT, padx=5)

        self.style_vars = {}
        self.param_vars = {}

        style_configs = {
            "Style A": [("steps", 40), ("line_width", 1)],
            "Style B": [("polygons", 20)],
            "Style C": [("shapes", 15)],
            "Style D": [("layers", 6)],
            "Style E": [("strokes", 30)],
            "Style F": [("dots", 150)],
            "Style G": [("doodles", 50)],
            "Style H": [("segments", 40)],
        }

        for style, params in style_configs.items():
            self.style_vars[style] = tk.BooleanVar()
            self.param_vars[style] = {}
            row = tk.Frame(control_frame)
            row.pack(anchor="w")
            tk.Checkbutton(row, text=style, variable=self.style_vars[style]).pack(side=tk.LEFT)
            for name, default in params:
                var = tk.IntVar(value=default)
                self.param_vars[style][name] = var
                tk.Label(row, text=name).pack(side=tk.LEFT)
                tk.Entry(row, textvariable=var, width=5).pack(side=tk.LEFT)

        tk.Button(root, text="Generate", command=self.generate).pack(side=tk.LEFT, padx=5)
        tk.Button(root, text="Save", command=self.save_image).pack(side=tk.LEFT, padx=5)

        self.image = Image.new("RGB", (WIDTH, HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

    def generate(self):
        self.image = Image.new("RGB", (WIDTH, HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.delete("all")

        selected_styles = [s for s, v in self.style_vars.items() if v.get()]
        for style in selected_styles[:3]:
            params = {name: var.get() for name, var in self.param_vars[style].items()}
            if style == "Style A":
                self.draw_geometric_lines(**params)
            elif style == "Style B":
                self.draw_colored_polygons(**params)
            elif style == "Style C":
                self.draw_modern_tribal(**params)
            elif style == "Style D":
                self.draw_mandala(**params)
            elif style == "Style E":
                self.draw_abstract_expressionism(**params)
            elif style == "Style F":
                self.draw_dot_spiral(**params)
            elif style == "Style G":
                self.draw_psychedelic_doodles(**params)
            elif style == "Style H":
                self.draw_golden_spiral(**params)

        self.display_image()

    def draw_geometric_lines(self, steps=40, line_width=1):
        for i in range(steps):
            self.draw.line([(0, i * HEIGHT // steps), (i * WIDTH // steps, HEIGHT)], fill="black", width=line_width)
            self.draw.line([(WIDTH, i * HEIGHT // steps), (WIDTH - i * WIDTH // steps, HEIGHT)], fill="black", width=line_width)

    def draw_colored_polygons(self, polygons=20):
        for _ in range(polygons):
            points = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
            color = tuple(random.choices(range(256), k=3))
            self.draw.polygon(points, fill=color, outline="black")

    def draw_modern_tribal(self, shapes=15):
        for _ in range(shapes):
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

    def draw_mandala(self, layers=6):
        center = (WIDTH // 2, HEIGHT // 2)
        for layer in range(1, layers + 1):
            radius = layer * 40
            color = tuple(random.choices(range(256), k=3))
            self.draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline=color, width=2)
            for i in range(12):
                angle = math.radians(i * 30)
                x = center[0] + radius * math.cos(angle)
                y = center[1] + radius * math.sin(angle)
                self.draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=color)

    def draw_abstract_expressionism(self, strokes=30):
        for _ in range(strokes):
            x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            color = tuple(random.choices(range(256), k=3))
            width = random.randint(5, 20)
            self.draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
            if random.random() < 0.3:
                drip_len = random.randint(10, 60)
                self.draw.line([(x2, y2), (x2, y2 + drip_len)], fill=color, width=max(1, width - 3))

    def draw_dot_spiral(self, dots=150):
        center = (WIDTH / 2, HEIGHT / 2)
        angle = 0
        for i in range(dots):
            radius = i * 2
            angle += 0.3
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            color = tuple(random.choices(range(256), k=3))
            self.draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=color)

    def draw_psychedelic_doodles(self, doodles=50):
        for _ in range(doodles):
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

    def draw_golden_spiral(self, segments=40):
        phi = (1 + math.sqrt(5)) / 2
        center = (WIDTH / 2, HEIGHT / 2)
        angle = 0.0
        radius = 5
        for _ in range(segments):
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            color = tuple(random.choices(range(256), k=3))
            self.draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=color)
            angle += math.pi / 8  # small increment
            radius *= phi ** (1 / 8)

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

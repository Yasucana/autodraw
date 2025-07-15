# autodraw
Simple tool to generate abstract drawings in various styles.

## Available Styles

- **Style A:** Geometric Line Art
- **Style B:** Stained Glass Style
- **Style C:** Modern Tribal
- **Style D:** Colorful Mandala
- **Style E:** Abstract Expressionism
- **Style F:** Dot Spiral
- **Style G:** Psychedelic Doodles
- **Style H:** Golden Spiral (points follow the golden ratio)

## Usage

When launched, the application displays a checkbox for each style along with
numeric fields for their parameters. You can enable up to three styles at once
and adjust the values to change how many elements are drawn.

| Style | Parameter |
|-------|-----------|
| Style A | `steps` and `line_width` |
| Style B | `polygons` |
| Style C | `shapes` |
| Style D | `layers` |
| Style E | `strokes` |
| Style F | `dots` |
| Style G | `doodles` |
| Style H | `segments` |

Press **Generate** to render the selected styles in order. Use **Save** to
export the image as a PNG file.

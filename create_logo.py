import svgwrite


def create_islp_logo(filename="./images/logo.svg"):
    """
    Generates a stylized SVG logo for "ISLP {Solutions}".

    The logo is inspired by the Jupyter Book logo, with specific colors
    for each letter of "ISLP" and a different color for "{Solutions}".
    """

    # --- Configuration ---
    # Colors inspired by the ISLP book cover
    colors = {
        "I": "#30437e",  # Navy Blue
        "S": "#46aacb",  # Light Blue
        "L": "#cb4047",  # Red
        "P": "#83ae63",  # Green
        "Solutions": "#eab224",  # Yellow
        "bracket": "#a9a2a1",  # Off-white
    }

    # Font settings
    font_family = "Inter, Arial, sans-serif"
    font_size = 60
    islp_font_weight = "bold"
    solutions_font_weight = "normal"

    # Spacing and layout
    canvas_height = 100
    canvas_width = 430
    start_x = 20
    y_baseline = 70
    letter_spacing_islp = -5  # Negative value to bring letters closer
    spacing_after_p = 15

    # --- SVG Generation ---
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(filename, size=(canvas_width, canvas_height), profile="tiny")

    # Add the "ISLP" letters one by one to control color and spacing
    current_x = start_x
    islp_text = "ISLP"

    for char in islp_text:
        # Add each character with its specific color
        text_element = dwg.text(
            char,
            insert=(current_x, y_baseline),
            fill=colors[char],
            font_family=font_family,
            font_size=font_size,
            font_weight=islp_font_weight,
        )
        dwg.add(text_element)

        # "I" is pretty thin so we're cutting on its distance
        if char == "I":
            current_x += (font_size * 0.7) + letter_spacing_islp - 57

        # Adjust distance between letters
        current_x += (font_size * 0.7) + letter_spacing_islp

    # Add the "{Solutions}" text
    solutions_text = "Solutions"
    current_x += spacing_after_p  # Add extra space after "P"

    # Add "{"
    left_bracket = dwg.text(
        "{",
        insert=(current_x, y_baseline),
        fill=colors["bracket"],
        font_family=font_family,
        font_size=font_size,
        font_weight=solutions_font_weight,
    )
    dwg.add(left_bracket)
    current_x += (font_size * 0.4) + letter_spacing_islp

    # Add "Solutions"
    solutions_element = dwg.text(
        solutions_text,
        insert=(current_x, y_baseline),
        fill=colors["Solutions"],
        font_family=font_family,
        font_size=font_size - 10,
        font_weight=solutions_font_weight,
    )
    dwg.add(solutions_element)
    current_x += len(solutions_text) * (font_size * 0.4) + letter_spacing_islp + 5

    # Add "}"
    right_bracket = dwg.text(
        "}",
        insert=(current_x, y_baseline),
        fill=colors["bracket"],
        font_family=font_family,
        font_size=font_size,
        font_weight=solutions_font_weight,
    )
    dwg.add(right_bracket)

    # Save the SVG file
    dwg.save()
    print(f"Logo saved successfully as '{filename}'")


if __name__ == "__main__":
    create_islp_logo()

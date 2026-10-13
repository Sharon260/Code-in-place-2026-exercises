import tkinter as tk
import random

def generate_characteristics(topic):
    """
    Generate 3–5 simple characteristics based on the topic.
    In a real project, this could call GPT, but here we simulate.
    """
    sample_traits = {
        "forest": ["green trees", "wild animals", "mystical fog", "hidden paths", "ancient ruins"],
        "ocean": ["waves", "coral reefs", "ships", "sea creatures", "treasures"],
        "space": ["stars", "planets", "spaceships", "aliens", "galaxies"],
        "desert": ["sand dunes", "cacti", "sunset", "oasis", "nomads"]
    }
    if topic.lower() in sample_traits:
        return random.sample(sample_traits[topic.lower()], 3)
    else:
        # fallback: generate generic traits
        return [f"{topic} element {i}" for i in range(1, 4)]

def draw_canvas(characteristics):
    """
    Draw simple shapes on a canvas based on characteristics.
    """
    root = tk.Tk()
    root.title("World Builder Canvas")
    canvas = tk.Canvas(root, width=500, height=400, bg="white")
    canvas.pack()

    colors = ["green", "blue", "orange", "purple", "brown"]
    shapes = [canvas.create_oval, canvas.create_rectangle, canvas.create_polygon]

    for i, trait in enumerate(characteristics):
        x, y = random.randint(50, 400), random.randint(50, 300)
        size = random.randint(40, 100)
        color = random.choice(colors)
        shape = random.choice(shapes)

        if shape == canvas.create_polygon:
            shape([x, y, x+size, y, x+size//2, y-size], fill=color)
        else:
            shape(x, y, x+size, y+size, fill=color)

        canvas.create_text(x+size//2, y+size+15, text=trait, font=("Arial", 10))

    root.mainloop()

def generate_story(topic, characteristics):
    """
    Create a short story based on the topic and characteristics.
    """
    story = f"In a world shaped by {topic}, "
    story += f"you encounter {', '.join(characteristics[:-1])}, and finally {characteristics[-1]}. "
    story += "This place feels alive, waiting for new adventures to unfold."
    return story

def main():
    topic = input("🌍 Enter a topic to build your world: ")
    characteristics = generate_characteristics(topic)
    print("\n✨ Characteristics chosen:", characteristics)

    # Draw the canvas
    draw_canvas(characteristics)

    # Print the story
    story = generate_story(topic, characteristics)
    print("\n📖 Your Story:\n", story)

if __name__ == "__main__":
    main()

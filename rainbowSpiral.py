import turtle
import time


class LearnCodeSpiral:
    def __init__(self):
        self.setup_canvas()
        self.create_turtles()
        self.setup_variables()

    # Add this method to the LearnCodeSpiral class
    def reset(self):
        """Reset the spiral and lessons to initial state"""
        # Clear the drawing
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        # Reset variables
        self.current_path_index = 0
        self.direction = "forward"
        self.is_drawing = False
        self.current_lesson = 0
        self.lesson_start_time = time.time()
        self.lesson_pause = False

        # Reset display
        self.show_status()
        self.show_lesson()

        # Show reset message
        self.text.goto(-550, 100)
        self.text.clear()
        self.text.write("🔄 Program Reset! Press SPACE to start again!",
                        font=("Comic Sans MS", 16, "bold"))

    def setup_canvas(self):
        self.canvas = turtle.Screen()
        self.canvas.setup(1200, 800)
        self.canvas.bgcolor("black")
        self.canvas.title("🐍 Learn Python with Magic Spiral! 🎨")
        self.canvas.tracer(0)

    def create_turtles(self):
        # Main drawing turtle
        self.artist = turtle.Turtle()
        self.artist.width(3)
        self.artist.hideturtle()

        # Text display turtle
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.color("white")

        # Code display turtle
        self.code_display = turtle.Turtle()
        self.code_display.hideturtle()
        self.code_display.penup()
        self.code_display.color("yellow")

    def setup_variables(self):
        self.is_drawing = False
        self.direction = "forward"
        self.drawing_speed = 1
        self.current_path_index = 0
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "violet"]
        self.path = []
        self.lesson_pause = False  # For pausing during lessons
        self.lesson_start_time = time.time()
        self.lesson_duration = 8  # 8 seconds per lesson

        # Calculate the spiral path
        self.calculate_spiral_path()

        # Forward learning content
        self.forward_lessons = [
            {
                "title": "🚀 Welcome to Python Coding! 🚀",
                "code": """# This is a Python program
# It draws a colorful spiral!""",
                "explanation": "Lines starting with # are notes for humans to read."
            },
            {
                "title": "🌈 Colors in Python",
                "code": """colors = ['red', 'orange', 'yellow', 
        'green', 'blue', 'purple']""",
                "explanation": "We store colors in a list - like a box of crayons!"
            },
            {
                "title": "🔄 Loops in Python",
                "code": """for step in range(360):
    move_forward(step)
    turn_left(59)""",
                "explanation": "This repeats 360 times to make our spiral!"
            },
            {
                "title": "📏 Math in Coding",
                "code": """distance = step  # Gets bigger each time
angle = 59    # Turn amount""",
                "explanation": "The spiral grows because we increase the distance!"
            }
        ]

        # Backward learning content
        self.backward_lessons = [
            {
                "title": "⏮️ Moving Backwards",
                "code": """# Remembering our path
previous_position = path[step]
go_to(previous_position)""",
                "explanation": "The computer remembers where we've been!"
            },
            {
                "title": "💭 Computer Memory",
                "code": """# Like reading a story backwards
for step in reverse(path):
    return_to(step)""",
                "explanation": "We can go back because we saved each step!"
            },
            {
                "title": "🔍 Understanding Loops",
                "code": """while going_backward:
    previous_step = path.pop()
    move_to(previous_step)""",
                "explanation": "Moving backward uses the same steps in reverse!"
            }
        ]

        self.current_lesson = 0

    def calculate_spiral_path(self):
        temp_turtle = turtle.Turtle()
        temp_turtle.hideturtle()
        temp_turtle.penup()
        temp_turtle.goto(0, 0)

        for i in range(360):
            pos = temp_turtle.position()
            heading = temp_turtle.heading()
            color = self.colors[i % len(self.colors)]

            self.path.append({
                'position': pos,
                'heading': heading,
                'color': color,
                'distance': i
            })

            temp_turtle.forward(i)
            temp_turtle.left(59)

    def show_controls(self):
        controls = """
        🎮 Learning Controls 🎮

        SPACE = Start/Stop Drawing
        RIGHT = Move Forward ➡️
        LEFT = Move Backward ⬅️
        UP = Speed Up ⚡
        DOWN = Slow Down 🐌
        R = Reset Program 🔄
        P = Pause for Reading 📚
        """
        self.text.goto(-550, 300)
        self.text.clear()
        self.text.write(controls, font=("Comic Sans MS", 14, "bold"))

    def show_status(self):
        status = f"""
        ✨ Learning Progress ✨

        Mode: {'Forward ➡️' if self.direction == 'forward' else 'Backward ⬅️'}
        Speed: {'🌟' * self.drawing_speed}
        Step: {self.current_path_index}/360
        """
        self.text.goto(200, 300)
        self.text.clear()
        self.text.write(status, font=("Comic Sans MS", 12, "bold"))

    def show_lesson(self):
        lessons = self.forward_lessons if self.direction == "forward" else self.backward_lessons
        lesson = lessons[self.current_lesson % len(lessons)]

        # Clear previous lesson
        self.code_display.clear()

        # Show direction mode
        mode = "FORWARD LEARNING MODE ➡️" if self.direction == "forward" else "BACKWARD LEARNING MODE ⬅️"
        self.code_display.goto(-550, 50)
        self.code_display.color("cyan")
        self.code_display.write(mode, font=("Comic Sans MS", 20, "bold"))

        # Show lesson content
        self.code_display.goto(-550, 0)
        self.code_display.color("yellow")
        self.code_display.write(lesson["title"], font=("Comic Sans MS", 16, "bold"))

        # Show code
        self.code_display.goto(-550, -50)
        self.code_display.color("lightgreen")
        self.code_display.write(lesson["code"], font=("Courier New", 14, "normal"))

        # Show explanation
        self.code_display.goto(-550, -150)
        self.code_display.color("pink")
        self.code_display.write(lesson["explanation"], font=("Comic Sans MS", 14, "normal"))

        # Show reading time remaining
        time_left = max(0, self.lesson_duration -
                        (time.time() - self.lesson_start_time))
        self.code_display.goto(-550, -200)
        self.code_display.color("white")
        self.code_display.write(f"Time until next lesson: {int(time_left)} seconds",
                                font=("Comic Sans MS", 12, "normal"))

    def toggle_pause(self):
        self.lesson_pause = not self.lesson_pause
        if self.lesson_pause:
            self.text.goto(-550, 100)
            self.text.write("⏸️ PAUSED - Take your time to read! Press P to continue",
                            font=("Comic Sans MS", 16, "bold"))

    def draw_current_state(self):
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.setheading(0)
        self.artist.pendown()

        for i in range(self.current_path_index + 1):
            point = self.path[i]
            self.artist.color(point['color'])
            self.artist.goto(point['position'])
            self.artist.setheading(point['heading'])

        self.canvas.update()

    def animate_spiral(self):
        while self.is_drawing:
            if not self.lesson_pause:
                current_time = time.time()

                # Check if it's time for next lesson
                if current_time - self.lesson_start_time >= self.lesson_duration:
                    self.current_lesson = (self.current_lesson + 1) % (
                        len(self.forward_lessons) if self.direction == "forward"
                        else len(self.backward_lessons)
                    )
                    self.lesson_start_time = current_time
                    self.show_lesson()

                # Update spiral position
                if self.direction == "forward":
                    if self.current_path_index < len(self.path) - 1:
                        self.current_path_index += 1
                    else:
                        self.is_drawing = False
                else:
                    if self.current_path_index > 0:
                        self.current_path_index -= 1
                    else:
                        self.is_drawing = False

                self.draw_current_state()
                self.show_status()
                self.show_lesson()

                time.sleep(0.1 / self.drawing_speed)

            self.canvas.update()


def start_learning_spiral():
    print("🌟 Welcome to Python Learning with Magic Spiral! 🌟")
    print("Get ready to learn coding while having fun!")

    spiral = LearnCodeSpiral()

    # Set up controls
    spiral.canvas.listen()
    spiral.canvas.onkey(lambda: setattr(spiral, 'is_drawing',
                                        not spiral.is_drawing) or (spiral.animate_spiral()
                                                                   if spiral.is_drawing else None), "space")
    spiral.canvas.onkey(lambda: setattr(spiral, 'direction', "forward"), "Right")
    spiral.canvas.onkey(lambda: setattr(spiral, 'direction', "backward"), "Left")
    spiral.canvas.onkey(lambda: setattr(spiral, 'drawing_speed',
                                        min(spiral.drawing_speed + 1, 10)), "Up")
    spiral.canvas.onkey(lambda: setattr(spiral, 'drawing_speed',
                                        max(spiral.drawing_speed - 1, 1)), "Down")
    spiral.canvas.onkey(spiral.reset, "r")
    spiral.canvas.onkey(spiral.toggle_pause, "p")

    # Show initial screen
    spiral.show_controls()
    spiral.show_status()
    spiral.show_lesson()

    turtle.done()


if __name__ == "__main__":
    start_learning_spiral()

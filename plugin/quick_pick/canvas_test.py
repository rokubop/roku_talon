from talon import Module, Context, actions, ui, skia
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d
import time

mod = Module()
ctx = Context()

canvas: Canvas = None

def fps_number_axis(c: SkiaCanvas):
    c.paint.color = "bbbbbb"
    c.paint.style = c.paint.Style.STROKE
    c.paint.stroke_width = 1
    # Recalculating the increments for 26 letters, including all letters but creating a gap in the middle
    screen_width = 1920
    offset = 50
    usable_width = screen_width - 2 * offset
    num_letters = 26

    # Adjusting the step size to create a gap in the middle
    # Since we are effectively positioning 25 letters (26 letters with a gap for one), we calculate the step size accordingly
    step = usable_width / (num_letters - 1)

    # Generating positions for each letter
    positions = [10 + i * step for i in range(num_letters)]

    # Finding the middle position and adjusting the positions to create a gap
    middle_index = num_letters // 2
    gap_width = step  # Width of the gap is one step
    for i in range(middle_index, num_letters):
        positions[i] += gap_width

    # The complete alphabet
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    # Pairing each letter with its position
    letter_positions = list(zip(alphabet, positions))

    for letter, position in letter_positions:
        c.draw_text(letter, position, 540)

def blender_style_popup(c: SkiaCanvas):
    # round rectangle
    c.paint.color = "0f0f0f"
    c.paint.style = c.paint.Style.FILL
    c.draw_rrect(RoundRect.from_rect(Rect(200, 200, 150, 35), x=4, y=4))
    c.paint.stroke_width = 0.3
    c.paint.color = "000000"
    c.paint.style = c.paint.Style.STROKE
    c.draw_rrect(RoundRect.from_rect(Rect(200, 200, 150, 35), x=4, y=4))
    c.paint.color = "fefefe"
    c.paint.textsize = 15
    c.paint.text_align = c.paint.TextAlign.CENTER
    c.paint.style = c.paint.Style.FILL
    c.draw_text("Rendered", 275, 220)

    c.paint.color = "bbbbbb"
    c.paint.style = c.paint.Style.STROKE
    c.paint.stroke_width = 1
    c.draw_circle(960, 540, 300)

def on_draw_2(c: SkiaCanvas):
    blender_style_popup(c)

def on_draw(c: SkiaCanvas):
    global t
    # circle
    c.paint.style = c.paint.Style.STROKE
    c.draw_circle(100, 100, 100)

    # rectangle
    c.paint.color = "ff0000"
    c.draw_rect(Rect(100, 100, 100, 100))

    # round rectangle
    c.paint.color = "0000ff"
    c.paint.stroke_width = 4
    c.draw_rrect(RoundRect.from_rect(Rect(200, 200, 100, 100), x=10, y=10))

    # text
    c.paint.color = "ffffff"
    c.paint.style = c.paint.Style.FILL
    c.paint.textsize = 20
    c.draw_text("Hello, world!", 960, 580)

    # gradient fill
    c.paint.shader = skia.Shader.linear_gradient(
        (500, 300), (500, 700), ["ff0000", "0000ff"], None
    )
    c.paint.style = c.paint.Style.FILL
    c.draw_circle(500, 500, 100)

    # gradient stroke
    c.paint.shader = skia.Shader.linear_gradient(
        (500, 300), (500, 700), ["0000ff", "ff0000"], None
    )
    c.paint.style = c.paint.Style.STROKE
    c.draw_circle(500, 500, 100)
    print("Time taken: ", time.perf_counter() - t)
    t = time.perf_counter()

    # c.clip_path(skia.Path.circle(500, 500, 100))

    # gradient text
    # c.paint.shader = skia.linear_gradient(
    #     (500, 300), (500, 700), ["0000ff", "000000"], None
    # )
    # c.paint.style = c.paint.Style.STROKE
    # c.draw_text("C I R C L E", 500, 500)
    # c.draw_circle(500, 500, 100)

def on_draw_3(c: SkiaCanvas):
    # circle
    c.paint.style = c.paint.Style.STROKE
    c.draw_circle(100, 100, 100)

    # rectangle
    c.paint.color = "ff0000"
    c.draw_rect(Rect(100, 100, 100, 100))

    # round rectangle
    c.paint.color = "0000ff"
    c.paint.stroke_width = 4
    c.draw_rrect(RoundRect.from_rect(Rect(200, 200, 100, 100), x=10, y=10))

    # text
    c.paint.color = "ffffff"
    c.paint.style = c.paint.Style.FILL
    c.paint.textsize = 20
    c.draw_text("Hello, world!", 960, 580)

    # gradient fill
    c.paint.shader = skia.Shader.linear_gradient(
        (500, 300), (500, 700), ["ff0000", "0000ff"], None
    )
    c.paint.style = c.paint.Style.FILL
    c.draw_circle(500, 500, 100)

    # gradient stroke
    c.paint.shader = skia.Shader.linear_gradient(
        (500, 300), (500, 700), ["0000ff", "ff0000"], None
    )
    c.paint.style = c.paint.Style.STROKE
    c.draw_circle(500, 500, 100)

    # gradient text
    c.paint.shader = skia.linear_gradient(
        (500, 300), (500, 700), ["0000ff", "000000"], None
    )
    c.paint.style = c.paint.Style.STROKE
    c.draw_text("C I R C L E", 500, 500)
    c.draw_circle(500, 500, 100)

    # c.draw_path(skia.Path.add_rect(Rect(100, 100, 100, 100), c.p

t = None

@mod.action_class
class Actions:
    def canvas_test_one():
        """canvas_test_one"""
        global canvas, t
        t = time.perf_counter()
        # screen: Screen = ui.main_screen()
        # canvas = Canvas.from_screen(screen)
        canvas = Canvas.from_rect(Rect(0, 0, 1000, 500))
        canvas.register("draw", on_draw)
        # for step in canvas.dispatch_iter("draw"):
        #         print(f"Processing step: {step}")

        canvas.freeze()

    def canvas_test_two():
        """canvas_test_two"""
        global canvas
        if canvas:
            # canvas.resize(800, 900)
            for step in canvas.dispatch_iter("draw"):
                print(f"Processing step: {step}")
            canvas.freeze()
        # screen: Screen = ui.main_screen()
        # canvas = Canvas.from_screen(screen)
        # canvas.register("draw2", on_draw_2)

    def canvas_test_three():
        """canvas_test_three"""
        global canvas
        screen: Screen = ui.main_screen()
        canvas = Canvas.from_screen(screen)
        canvas.register("draw3", on_draw_3)

    def canvas_test_stop():
        """canvas_test_stop"""
        global canvas
        if canvas:
            canvas.unregister("draw", on_draw)
            canvas.unregister("draw2", on_draw_2)
            canvas.unregister("draw3", on_draw_3)
            canvas.hide()
            canvas.close()

    def canvas_test_freeze():
        """canvas_test_freeze"""
        global canvas
        if canvas:
            canvas.freeze()

import pyglet
from pyglet.image import Animation, AnimationFrame
from pyglet.window import key

__author__ = 'CP-12GSP'

window = pyglet.window.Window(fullscreen=True, resizable=True, vsync=True)
fps_display = pyglet.clock.ClockDisplay(format='%(fps).1f', color=(0.5, 0.5, 0.5, 1))

white = (1, 1, 1, 0)
black = (0, 0, 0, 0)
pyglet.gl.glClearColor(*black)

effects = []
use_effect = 1


def create_effect_animation(image_name, columns, rows):
    effect_seq = pyglet.image.ImageGrid(pyglet.image.load(image_name), rows, columns)
    # print(repr(effect_seq[1]))
    effect_frames = []
    # print(list(range(rows, 0, -1)))
    # Boucle qui créé l'animation
    for row in range(rows, 0, -1):
        end = row * columns
        start = end - (columns - 1) - 1
        # print("Start : " + repr(start) + " - End : " + repr(end))
        for effect_frame in effect_seq[start:end:1]:
            effect_frames.append(AnimationFrame(effect_frame, 0.05))

    effect_frames[(rows * columns) - 1].duration = None
    return Animation(effect_frames)


effect_animations = [create_effect_animation('effects/_LPE__Elemental_Burst.png', 5, 6),
                     create_effect_animation('effects/_LPE__Fire_Arrow.png', 5, 9),
                     create_effect_animation('effects/_LPE__Healing_Circle.png', 5, 10),
                     create_effect_animation('effects/_LPE__Flaming_Time.png', 5, 5),
                     create_effect_animation('effects/_LPE__Gale.png', 5, 8)]


class EffectSprite(pyglet.sprite.Sprite):
    def on_animation_end(self):
        self.delete()
        effects.remove(self)


@window.event
def on_mouse_motion(x, y, dx, dy):
    if pyglet.window.mouse.LEFT:
        effect = EffectSprite(effect_animations[use_effect - 1])
        effect.position = (x - effect.width / 2, y - effect.height / 2)
        effects.append(effect)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if modifiers & pyglet.window.key.MOD_SHIFT:
        pass
    if pyglet.window.mouse.LEFT == button:
        effect = EffectSprite(effect_animations[use_effect - 1])
        effect.position = (x - effect.width / 2, y - effect.height / 2)
        effects.append(effect)


@window.event
def on_key_press(symbol, modifiers):
    global use_effect
    if modifiers & pyglet.window.key.MOD_SHIFT:
        pass
    if symbol == key.B:
        pyglet.gl.glClearColor(*black)
    if symbol == key.W:
        pyglet.gl.glClearColor(*white)
    if symbol == key._1:
        use_effect = 1
    if symbol == key._2:
        use_effect = 2
    if symbol == key._3:
        use_effect = 3
    if symbol == key._4:
        use_effect = 4
    if symbol == key._5:
        use_effect = 5


@window.event
def on_draw():
    window.clear()
    for effect in effects:
        effect.draw()
    fps_display.draw()


def main():
    pyglet.app.run()

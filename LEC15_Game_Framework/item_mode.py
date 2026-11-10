from pathlib import Path

from pico2d import *
import game_framework
import game_world
import play_mode


def init():
    global image
    image = load_image(str(Path(__file__).with_name('item_select.png')))


def finish():
    global image
    del image


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if not getattr(event, 'repeat', 0):
                game_framework.pop_mode()
                return
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_1, SDLK_2):
            if not getattr(event, 'repeat', 0):
                play_mode.boy.ball_type = {
                    SDLK_0: 0, SDLK_1: 1, SDLK_2: 2
                }[event.key]
                game_framework.pop_mode()
                return


def update():
    pass


def pause():
    pass


def resume():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

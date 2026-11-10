from pathlib import Path
import os

from pico2d import *
import game_framework
import game_world
import play_mode
import title_mode


def init():
    global font
    font = load_font(str(Path(os.environ.get('WINDIR', 'C:/Windows')) /
                         'Fonts' / 'malgun.ttf'), 30)


def finish():
    global font
    del font


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if not getattr(event, 'repeat', 0):
                game_framework.pop_mode()
                return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYUP:
            # Remember released movement keys while the game is paused.
            play_mode.boy.handle_event(event)


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    x = get_canvas_width() // 2
    y = get_canvas_height() // 2
    font.draw(x - 85, y + 30, '일시정지 중', (255, 0, 0))
    font.draw(x - 190, y - 20, 'P 키를 누르면 다시 진행', (255, 0, 0))
    update_canvas()

""" Lab 7 - User Control """

import arcade
from arcade import Vec2
from arcade.types import Color

color_carne = Color(200, 150, 150)
color_esclera = Color(255, 255, 255)
color_pupila = Color(0, 0, 0)
color_boca = Color(200, 100, 100)
color_ropa = Color(50, 50, 200)

def dibujar_chaval(x: float, y: float, escala: float, brazos_abiertos: bool) -> None:
    # Cuerpo
    arcade.draw_lbwh_rectangle_filled(x - 25 * escala, y - 75 * escala, 50 * escala, 150 * escala, color_ropa)

    # Piernas
    # Pierna izquierda
    arcade.draw_lbwh_rectangle_filled(x - 25 * escala, y - 125 * escala, 10 * escala, 200 * escala, color_ropa)
    # Pierna derecha
    arcade.draw_lbwh_rectangle_filled(x + 15 * escala, y - 125 * escala, 10 * escala, 200 * escala, color_ropa)

    # Brazos
    if brazos_abiertos:
        # Brazo izquierdo
        arcade.draw_lbwh_rectangle_filled(x - 75 * escala, y + 15 * escala, 50 * escala, 10 * escala, color_carne)
        # Brazo derecho
        arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y + 15 * escala, 50 * escala, 10 * escala, color_carne)
    else:
        # Brazo izquierdo
        arcade.draw_lbwh_rectangle_filled(x - 35 * escala, y - 25 * escala, 10 * escala, 50 * escala, color_carne)
        # Brazo derecho
        arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y - 25 * escala, 10 * escala, 50 * escala, color_carne)

    # Mangas
    # Manga izquierda
    arcade.draw_lbwh_rectangle_filled(x - 35 * escala, y + 15 * escala, 10 * escala, 10 * escala, color_ropa)
    # Manga derecha
    arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y + 15 * escala, 10 * escala, 10 * escala, color_ropa)

    # Cabeza
    arcade.draw_circle_filled(x, y + 75 * escala, 50 * escala, color_carne)

    # Ojos
    # Esclera izquierda
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 15 * escala, color_esclera)
    # Pupila izquierda
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 8 * escala, color_pupila)
    # Esclera derecha
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 15 * escala, color_esclera)
    # Pupila derecha
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 8 * escala, color_pupila)

    # Boca
    arcade.draw_arc_outline(x, y + 75 * escala, 80 * escala, 60 * escala, color_boca, 200, 340, 10 * escala)

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ChavalTeclado:
    speed = 200

    def __init__(self, pos: Vec2):
        self.pos = pos
        self.dir = Vec2(0, 0)

    def update(self, delta_time: float):
        if self.pos.x <= 0 or self.pos.x >= SCREEN_WIDTH:
            self.dir = Vec2(-self.dir.x, self.dir.y)
        if self.pos.y <= 0 or self.pos.y >= SCREEN_HEIGHT:
            self.dir = Vec2(self.dir.x, -self.dir.y)

        self.pos += self.dir * self.speed * delta_time

    def cambiar_dir(self, delta: Vec2):
        self.dir = delta

    def draw(self):
        dibujar_chaval(self.pos.x, self.pos.y, 1, True)


class ChavalMouse:
    speed = 300

    def __init__(self, pos: Vec2):
        self.pos = pos
        self.target = pos
        self.dir = Vec2(0, 0)

    def update(self, delta_time: float):
        self.pos += self.dir * self.speed * delta_time
        if self.pos.distance(self.target) <= self.speed * delta_time:
            self.dir = Vec2(0, 0)

    def draw(self):
        dibujar_chaval(self.pos.x, self.pos.y, 1.5, False)

    def move(self, pos: Vec2):
        self.target = pos
        self.dir = (self.target - self.pos).normalize()


class ChavalMando:
    speed = 400

    def __init__(self, pos: Vec2):
        self.pos = pos
        self.dir = Vec2(0, 0)

        self.mando = None
        mandos = arcade.get_joysticks()
        print(mandos)
        if mandos:
            self.mando = mandos[0]
            self.mando.open()

    def update(self, delta_time: float):
        if self.mando:
            self.dir = Vec2(self.mando.x, -self.mando.y)
        self.pos += self.dir * self.speed * delta_time
        if self.pos.x < 0:
            self.pos = Vec2(0, self.pos.y)
        elif self.pos.x > SCREEN_WIDTH:
            self.pos = Vec2(SCREEN_WIDTH, self.pos.y)
        if self.pos.y < 0:
            self.pos = Vec2(self.pos.x, 0)
        elif self.pos.y > SCREEN_HEIGHT:
            self.pos = Vec2(self.pos.x, SCREEN_HEIGHT)

    def draw(self):
        dibujar_chaval(self.pos.x, self.pos.y, 2, True)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.chaval_teclado = ChavalTeclado(Vec2(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2))
        self.chaval_mouse = ChavalMouse(Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.chaval_mando = ChavalMando(Vec2(SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT / 2))

    def on_update(self, delta_time: float):
        self.chaval_teclado.update(delta_time)
        self.chaval_mouse.update(delta_time)
        self.chaval_mando.update(delta_time)

    def on_draw(self):
        self.clear()
        self.chaval_teclado.draw()
        self.chaval_mouse.draw()
        self.chaval_mando.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.chaval_teclado.cambiar_dir(Vec2(0, 1))
        elif symbol == arcade.key.S:
            self.chaval_teclado.cambiar_dir(Vec2(0, -1))
        elif symbol == arcade.key.A:
            self.chaval_teclado.cambiar_dir(Vec2(-1, 0))
        elif symbol == arcade.key.D:
            self.chaval_teclado.cambiar_dir(Vec2(1, 0))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.chaval_mouse.move(Vec2(x, y))


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
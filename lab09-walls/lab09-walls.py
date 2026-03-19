from typing import Any
import arcade


TILE_SIZE = 120


class Player(arcade.Sprite):
    speed = TILE_SIZE * 6

    def __init__(self, path: str, center_x: float, center_y: float):
        super().__init__(path, TILE_SIZE / 100, center_x=center_x, center_y=center_y)

    def update(self, delta_time: float) -> None:
        center_x, center_y = self.center_x, self.center_y

        if ventana.is_pressed(arcade.key.W):
            self.center_y += self.speed * delta_time
        if ventana.is_pressed(arcade.key.A):
            self.center_x -= self.speed * delta_time
        if ventana.is_pressed(arcade.key.S):
            self.center_y -= self.speed * delta_time
        if ventana.is_pressed(arcade.key.D):
            self.center_x += self.speed * delta_time

        if not self.collides_with_list(ventana.muros):
            ventana.muros.move(center_x - self.center_x, center_y - self.center_y)
            ventana.monedas.move(center_x - self.center_x, center_y - self.center_y)

        self.center_x, self.center_y = center_x, center_y

        monedas = self.collides_with_list(ventana.monedas)
        for moneda in monedas:
            moneda.remove_from_sprite_lists()


class Ventana(arcade.Window):
    mapa = [
        "##########",
        "#       o#",
        "#  ####  #",
        "#  # #o  #",
        "#     #  #",
        "#     #  #",
        "#     #  #",
        "#     #  #",
        "#        #",
        "##########"
    ]

    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)

        self.input = {}

        self.muros = arcade.SpriteList()
        self.monedas = arcade.SpriteList()

        for x, col in enumerate(self.mapa):
            for y, tile in enumerate(col):
                if tile == '#':
                    self.muros.append(arcade.Sprite(":resources:images/tiles/boxCrate.png", TILE_SIZE / 120,
                                                    x * TILE_SIZE + TILE_SIZE / 2, y * TILE_SIZE + TILE_SIZE / 2))
                elif tile == 'o':
                    self.monedas.append(arcade.Sprite(":resources:images/items/coinGold.png", TILE_SIZE / 120,
                                                    x * TILE_SIZE + TILE_SIZE / 2, y * TILE_SIZE + TILE_SIZE / 2))

        self.player = Player(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png",
                             self.width / 2, self.height / 2)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def on_update(self, delta_time: float):
        self.player.update(delta_time)

    def on_draw(self):
        self.clear()
        self.muros.draw()
        self.monedas.draw()
        self.player_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.input[symbol] = True

    def on_key_release(self, symbol: int, modifiers: int):
        self.input[symbol] = False

    def is_pressed(self, symbol: int) -> bool:
        return self.input.get(symbol, False)


if __name__ == "__main__":
    ventana = Ventana(600, 600, "Juego")
    arcade.run()
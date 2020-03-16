import arcade
import random
import os

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

GAME_TITLE = "coin game"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)


        self.palyer_list = None
        self.coin_list = None

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ALICE_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("cha.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("download.jpg", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(WINDOW_WIDTH)
            coin.center_y = random.randrange(WINDOW_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        def on_draw(self):
            """ Draw everything """
            arcade.start_render()
            self.coin_list.draw()
            self.player_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        def on_mouse_motion(self, x, y, dx, dy):
            """ Handle Mouse Motion """

            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

        def update(self, delta_time):
            """ Movement and game logic """

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.coin_list.update()

            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.kill()
                self.score += 1

def main():
            """ Main method """

            window = MyGame()
            window.setup()
            arcade.run()


if __name__ == "__main__":
    main()

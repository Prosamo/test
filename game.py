import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        # キーボードのEnterキーをゲームパッドのAボタンに置き換え
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 50, 8, 8, 11)
        
if __name__ == "__main__":
    App()



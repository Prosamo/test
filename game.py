import pyxel
import PyxelUniversalFont as puf
writer = puf.Writer("ipa_gothic.ttf")
class App:
    def __init__(self):
        pyxel.init(256, 256, title="テスト")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        pyxel.elli(128, 32, 64, 96, 8)
        writer.draw(32, 32, 'テスト', 16, 0)
        
if __name__ == "__main__":
    App()


import pyxel
class App:
    def __init__(self):
        pyxel.init(256, 256, title="テスト")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        pyxel.elli(128, 32, 64, 96, 8)
        
if __name__ == "__main__":
    App()


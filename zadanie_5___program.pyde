class Kolo(): # Dzień dobry, przez przypadek podesłałam swoje notatki. Poprawne zadanie podesłałam w następnym pliku, dlatego proszę nie brać tego pod uwagę :)
  
    kolor = 0 
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
    def rysowanie(self):
        if self.kolor:
            fill(125, 60, 152)
        circle(self.x, self.y, self.w)

def setup():                      
    size(400,400)
    global kolo1
    global kolo2
    kolo1 = Kolo(150,150, 100)                            
    kolo2 = Kolo(230, 260, 70)
 
def mouseClicked():
    a = (hex(get(mouseX, mouseY)))
    print(a)
    if a == "FF27AE60" or a == "FF7D3C98":
        kolo2.kolor = not kolo2.kolor
 
def keyPressed():
    if key == CODED:              
        if keyCode == RIGHT:
            kolo1.x = kolo1.x+5
        elif keyCode == LEFT:
            kolo1.x = kolo1.x-5
        if keyCode == UP:
            kolo1.y = kolo1.y-5
        elif keyCode == DOWN:
            kolo1.y = kolo1.y+5
 
def draw():
    background(0,0,0)
    fill(39, 174, 96)
    kolo2.rysowanie()
    fill(230, 126, 34)
    kolo1.rysowanie()

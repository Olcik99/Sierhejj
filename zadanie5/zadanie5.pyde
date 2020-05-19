class kolo():
    kolor = 0
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    def rysuj(self):
        if self.kolor:
            fill(94, 94, 94)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI+ radians(self.obrot+90), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI+ radians(self.obrot+270), PIE)
    def obroc(self, stopnie):
        self.obrot += stopnie


def setup():                      
    size(400,400)
    global kolop
    global kolot
    kolop = kolo(95, 230, 50)
    kolot = kolo(290, 230, 50)             
 
def mouseClicked():
    a = (hex(get(mouseX, mouseY)))
    print(a)
    if a == "FFD0D4D0" or a == "FF5E5E5E":
        kolop.kolor = not kolop.kolor
        kolot.kolor = not kolot.kolor    
 
def keyPressed():
    if key == CODED:              
        if keyCode == RIGHT:
            kolop.obroc(15)
            kolot.obroc(15)
        elif keyCode == LEFT:
            kolop.obroc(-15)
            kolot.obroc(-15)
 
def draw():
    background(113, 214, 255)
    fill(0,0,0,255)
    rect(0,170, 400, 130)
    fill(255,255,255,255)
    rect(0,220, 80, 10)
    rect(320,220, 80, 10)
    fill(5, 153, 14)
    rect(0,300, 400, 130)
    car = createShape()
    car.beginShape()
    car.fill(255,0,0,255)
    car.stroke(0,0,0,255)
    car.vertex(1, 90)
    car.vertex(1, 130)
    car.vertex(300, 130)
    car.vertex(300, 80)
    car.vertex(280, 80)
    car.vertex(250, 40)
    car.vertex(130, 40)
    car.vertex(80, 80)
    car.endShape(CLOSE) 
    shape(car, 40, 100)
    fill(208, 212, 208)
    kolop.rysuj()
    fill(208, 212, 208)
    kolot.rysuj()
    
# plus do aktywnosci za scenerię, jednak metody i atrybuty sa kalką tych z mojego programu, a to o twóczość i pomysły na ich polu chodziło
# 1,5pkt

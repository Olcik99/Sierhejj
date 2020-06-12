def setup():
    size(400,400)
    global obrazek
    obrazek=loadImage("zadanie.jpg")
    
def draw():
    background(53,53,53)
    global obrazek
    try:
        image(obrazek, 50, 50, 300, 300)
        stroke(80,130,220)
    except:
        fill(0,0,0)
        stroke(215,80,80)
        strokeWeight(5)
        fill(255,255,255)
        text("Nie znaleziono pliku", 150, 200)
        text("lub on nie jest plikiem graficznym", 120, 210)
    noFill()
    square(50, 50, 300)

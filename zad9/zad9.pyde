def setup():
    size(400,400)
    global obrazek
    obrazek=loadImage("zadanie.jpg")
    noFill() # nie ma sensu powtarzać co klatkę
    
def draw():
    background(53,53,53)
    global obrazek
    try:
        image(obrazek, 50, 50, 300, 300)
    except:
        stroke(215,80,80)
        strokeWeight(5)
        text("Nie znaleziono pliku", 150, 200)
        text("lub on nie jest plikiem graficznym", 120, 210)
    else:
       stroke(80,130,220) 
    finally:
        square(50, 50, 300)
        
# 1,5 pkt i plus za znalezienie noFill i wykonanie stetycznie (napis w srodku), bo wieksość sobie z tym nie poradziła

def setup():
    size(400, 400)
    textSize(70)
def draw():
    clear()
    background (220,150,110)
    
    s = createShape()
    s.beginShape()
    s.fill(20,80,160,255)
    s.stroke(15,60,157,255)
    s.vertex(70, 200)
    s.vertex(200, 150)
    s.vertex(330, 200)
    s.vertex(200, 250) 
    s.endShape(CLOSE)
     
    shape(s, 0, 0)
    s = createShape()
    s.beginShape()
    s.fill(0,0,0)
    s.stroke(15,60,157,255)
    s.vertex(81, 200)
    s.vertex(200, 111)
    s.vertex(321, 200)
    s.vertex(200, 241)
    s.endShape(CLOSE)
    shape(s, 0, 0)
    
    shape(s, 0, 0)
    s = createShape()
    s.beginShape()
    s.fill(0,0,255)
    s.stroke(15,60,157,255)
    s.vertex(80, 200)
    s.vertex(200, 110)
    s.vertex(320, 200)
    s.vertex(200, 240)
    s.endShape(CLOSE)
    shape(s, 0, 0)
    # ładny kształt, wyróżniający się, plus do aktywności
    
   
    fill(255, 0, 0)
    text("S", width/2+5, height/2)
    if keyPressed and key == "s": # warto by najpierw sprawdzić, czy coś zostało kliknięte, a później sprawdzać, czy jest literą s
        fill(70, 230, 10)
        text("S", width/2+5, height/2)
    # miało być też dodane zmienianie zaznaczenia między literami za pomocą strzałęk
        
    fill(255, 0, 0)
    text("A", width/2-45, height/2)
    a = (hex(get(mouseX, mouseY)))
    print(a)
    if a == "FFFF0000": # teraz zaznacza się rónież przy najechaniu na 's', trzeba dodać warnek czy koordynaty myszy znajdują się po lewej stronie okna programu
        fill(70, 230, 10)
        text("A", width/2-45, height/2)

# Pragnę zauważyć, że przedmiot nie wymaga wysokich umiejętności programistycznych, a dopiero naucza ich podstaw, co myśląc logicznie i poświęcając trochę czasu można opanować.
# 1,25p +

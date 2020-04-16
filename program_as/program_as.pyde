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
    
   
    fill(255, 0, 0)
    text("S", width/2+5, height/2)
    a = (hex(get(mouseX, mouseY)))
    if key == "s" and keyPressed:
        fill(70, 230, 10)
        text("S", width/2+5, height/2) 
        
    fill(255, 0, 0)
    text("A", width/2-45, height/2)
    a = (hex(get(mouseX, mouseY)))
    print(a)
    if a == "FFFF0000":
        fill(70, 230, 10)
        text("A", width/2-45, height/2)
# Witam ^^ Z racji tego, że moje zdolności, jaki Aleksandry Strzelczyk nie są na wysokim poziomie jeśli chodzi o programowanie, 
# więc proszę o wyrozumiałość, ponieważ nasze projekty w niektóych miejscach mogą być identyczne (dużo się nardzamy i analizujemy wszystko wspólnie).
# Życzę dużo cierpliwości do nas i zdrówka, szczególnie dla Janosika <3
        

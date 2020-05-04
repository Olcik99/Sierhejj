import random
add_library('pdf')
def setup():
    
    global img
    size(400, 400) # to nie są proporcje zdjęcia dokumentowego
    img = loadImage("zdj.jpg") # wartoby to zdjęcie załączyć...
    print(random.random())
    print(type(img)) 
    fill(0,0,0)
    background(0,0,0)
    
def draw():
    global img
    image(img, 100, 100, height/2, width/2) # wystarczy rysować raz na klatkę
    if (key == CODED):
        if (keyCode == 37): 
            clear()
            beginRecord(PDF, "foto1.pdf")
            #serduszka
            o = createShape()
            o.beginShape()
            o.fill(255,0,0,255)
            o.stroke(0,0,0,255)
            o.vertex(160, 190)
            o.vertex(170, 180)
            o.vertex(190, 180)
            o.vertex(200, 190)
            o.vertex(200, 200)
            o.vertex(160, 230)
            o.vertex(160, 190)
            o.vertex(150, 180)
            o.vertex(130, 180)
            o.vertex(120, 190)
            o.vertex(120, 200)
            o.vertex(160, 230)
            o.endShape(CLOSE) 
            shape(o, 0, 0)
                    
            h = createShape()
            h.beginShape()
            h.fill(255,0,0,255)
            h.stroke(0,0,0,255)
            h.vertex(240, 190)
            h.vertex(250, 180)
            h.vertex(270, 180)
            h.vertex(280, 190)
            h.vertex(280, 200)
            h.vertex(240, 230)
            h.vertex(240, 190)
            h.vertex(230, 180)
            h.vertex(210, 180)
            h.vertex(200, 190)
            h.vertex(200, 200)
            h.vertex(240, 230)
            h.endShape(CLOSE) 
            shape(h, 0, 0)
            endRecord()
            
    if (key == CODED):
        if (keyCode == 39): 
            clear()
            beginRecord(PDF, "foto2.pdf")
            
            s = createShape()
            s.beginShape()
            s.fill(20,80,160,200)
            s.stroke(15,60,157,255)
            s.vertex(130, 190)
            s.vertex(140, 195)
            s.vertex(152, 190) 
            s.vertex(160, 170)
            s.vertex(177, 190)
            s.vertex(200, 195)
            s.vertex(160, 215)
            s.endShape(CLOSE) 
            shape(s, 0, 0)
        
            z = createShape()
            z.beginShape()
            z.fill(20,80,160,200)
            z.stroke(15,60,157,255)
            z.vertex(270, 190)
            z.vertex(260, 195)
            z.vertex(248, 190) 
            z.vertex(245, 170)
            z.vertex(223, 190)
            z.vertex(200, 195)
            z.vertex(245, 215)
            z.endShape(CLOSE) 
            shape(z, 0, 0)
            endRecord()
                      
def mousePressed():
    exit()
    
#1,5p

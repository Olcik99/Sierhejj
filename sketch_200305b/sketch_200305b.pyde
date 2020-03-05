def setup():
    size(1000, 1000)
def draw():
    if mousePressed:
        circle(mouseX,mouseY,30)
    else:
        cursor(CROSS)
    rect(mouseX, mouseY,50, 40)
    
    

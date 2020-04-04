def setup():
    size(1000, 1000)
    cursor(CROSS) # jak ma wyglądać kursor ustawia się raz, to nie jest obiekt rysowany na cavasie programu
def draw():
    if mousePressed:
        circle(mouseX,mouseY,30)
    else:
        rect(mouseX, mouseY,width/20, height/25) # tam gdzie się da należy używać zmiennych zależnych
    # teraz będzie albo kółko albo prostokącik
# 1,75 p
    
    

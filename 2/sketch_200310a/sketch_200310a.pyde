def setup():
    dlugosc=0
    global zmienna
    zmienna=1
    global kierunek_zmiany
    kierunek_zmiany = 1
def draw():
    global natezenie
    global kierunek_zmiany
    natezenie = natezenie + kierunek_zmiany
    if natezenie == 225 or natezenie == 0:
        kierunek_zmiany *= -1 # dzięki temu zmiana natężenia będzie gładsza, dwustronna, bez skoku - jako ćwiczenie możesz to przeanalizować :)
#    line(mouseX,mouseY,width/3, height/3)
    fill(0,0,natezenie,120)
#    rect(20,30,120,140)
    if zmienna == 6:
        dlugosc =0
        szerokosc =0
        
# ciekawie napisane, ale ot nie do końca ta ścieżka, którą miał pokonywać obiekt ;)
    if index==3:
        index=0
    rect(szerokosc,dlugosc,100,100)
    slownik={"czerwony":(225,0,0), "niebieski":(0,0,225), "zielony":(0,225,0)} # mogłabyś zmienić kolory, byłoby ciekawiej i bardziej indywidualnie
    print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista=[]
    print(dlugosc, szerokosc)
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    # od definicji słownika dotąd lepiej byłoby wykonać raz w draw i udostępnić przez specyfikator global
    index += 1
    if index==3:
        index=0

    stroke(*lista[index])
    
def mousePressed():
    exit()
    
# 1,75 pkt
# dziwnym zbiegiem okoliczności u koleżanki Adamus program wygląda identycznie znaczek w znaczek...

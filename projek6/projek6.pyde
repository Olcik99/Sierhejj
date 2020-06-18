class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class WykwadratowanyKwadrat(Kwadrat):
    def sketchWykwadratowany(self, x, y, kwadratow):
        Kwadrat.sketch(self, x, y)
        space = self.bok/kwadratow
        _xKwadratow_ = 0
        for kropka in range(0, kwadratow):
            rect(x +_xKwadratow_ /2 , y +_xKwadratow_ /2 , self.bok - _xKwadratow_ , self.bok - _xKwadratow_)
            _xKwadratow_ +=space        
            
def setup():
    size(500, 500)
    fill(255,0,10)
    malyKwadrat = Kwadrat(50.0)
    malyKwadrat.sketch(200, 200) 
    fill(200,200,0)
    malyWykwadratowanyKwadrat = WykwadratowanyKwadrat(50.0)
    malyWykwadratowanyKwadrat.sketchWykwadratowany(300, 220, 4)
    fill(50,100,200)
    duzyWykwadratowanyKwadrat = WykwadratowanyKwadrat(150.0)
    duzyWykwadratowanyKwadrat.sketchWykwadratowany(30, 300, 10)

#2pkt

mode = 1 #Start screen, 2 == play screen, 3 == end screen



def setup():
    global mode
    size(800,900)
    
def draw():
    global mode
    if mode == 1:
        start_screen()
    elif mode == 2:
        background('#DDE1C7')
        
        
            
def mousePressed():
    global mode
    if (mouseX >= 170 and mouseX <= 670) and (mouseY >= 650 and mouseY <= 800):
        mode = 2
        
    
#def play_screen():
    
def start_screen():
    background('#DDE1C7')
    textSize(20)
    fill('#FFA500')
    rect(200, 425, 420, 150)
    fill(255)
    text("Instructions: tap the space bar to jump. \nPass through the pipes to score points. \nIf you hit the ground or hit the pipes, \nthe game is over.", 200, 450)
    fill('#FFA500')
    rect(170, 650, 500, 150)
    fill(0,0,0)
    textSize(100)
    text("- Play - ",230,750)

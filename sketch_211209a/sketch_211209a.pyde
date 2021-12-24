mode = 2 #Start screen, 2 == play screen, 3 == end screen
x = 0
y = 0
birdx = 400
birdy = 400 



def setup():
    global mode
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    play_screen_move_variables()
    size(675,900)

    
def draw():
    global mode, bird, birdx, birdy
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    if mode == 1:
        start_screen()
    elif mode == 2:
        moving_play_screen()
        bird = loadImage("character_bird.png")
        image(bird,birdx,birdy,110,80)
        birdy += 1
    elif mode == 3:
        end_screen()

     
        
              
            
def mousePressed():
    global mode
    if (mouseX >= 100 and mouseX <= 640) and (mouseY >= 640 and mouseY <= 852):
        mode = 2
    
def play_screen():
    global mode, bird, birdy
    if key == CODED:
        if keyCode == UP:
            birdy -= 100

def keyPressed():
    play_screen()

    
    
def start_screen():
    start_background = loadImage("Flappy_Bird_Start_Screen.png")
    background(start_background)
    
def end_screen():
    end_background = loadImage("Flappy_Bird_End_Screen.png")
    background(end_background)

def play_screen_move_variables():
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    Playscreen_Height = 900 
    Playscreen_Width = 1600  
    Play_Width_Size = 675 
    Increment = 1  
    image_PlayX = 0    
    image_PlayY = 0      
    Xcoor_play = 0 
    Ycoor_play = 0 
    canvasX = 675 
    canvasY = 900 
    play_screen_background = loadImage( "Flappy_Bird_Play_Screen.png" )
    
def moving_play_screen():
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    image_PlayX += Increment 
    if ( image_PlayX + Play_Width_Size ) >= Playscreen_Width: 
        image_PlayX = 0 
    copy(play_screen_background, image_PlayX, image_PlayY, Play_Width_Size, Playscreen_Height, Xcoor_play, Ycoor_play, canvasX, canvasY)'''
    

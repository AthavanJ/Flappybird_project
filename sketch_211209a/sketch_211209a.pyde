mode = 1 #Start screen, 2 == play screen, 3 == end screen
x = 0
y = 0
speed = 1
birdx = 100
birdy = 400 
start_game = False
switch = False
score = 0
highscore = 0


def setup():
    global mode
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    play_screen_move_variables()
    pipes_move_variables()
    size(675,900)

    
def draw():
    global mode, bird, birdx, birdy, score, start_game 
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    if mode == 1:
        start_screen()
        
    elif mode == 2:
        moving_play_screen()
        bird = loadImage("character_bird.png")
        image(bird,birdx,birdy,110,80)
        if start_game == True:
            birdy += 1.5
            pipes_move()
            check_lengths()
            reset_pipes()
        elif start_game == False:
            animation_playscreen()
            
    elif mode == 3:
        end_screen()
        score = 0
        start_game = False

             
def mousePressed():
    global mode
    if (mouseX >= 100 and mouseX <= 640) and (mouseY >= 640 and mouseY <= 852) and (mode == 1):
        mode = 2
    elif (mouseX >= 105 and mouseX <= 555) and (mouseY >= 415 and mouseY <= 577) and (mode == 3):
        mode = 2
    elif (mouseX >= 105 and mouseX <= 555) and (mouseY >= 635 and mouseY <= 795) and (mode == 3):
        mode = 1

def play_screen():
    global mode, bird, birdy, start_game
    if key == CODED:
        start_game = True
        
    if start_game == True:
        if keyCode == UP:
            birdy -= 60


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
    copy(play_screen_background, image_PlayX, image_PlayY, Play_Width_Size, Playscreen_Height, Xcoor_play, Ycoor_play, canvasX, canvasY)
    

def animation_playscreen():
    global switch
    stroke(255)
    fill(255, 0, 0)
    triangle(220, 400, 200, 420, 220, 420)
    rect(220, 395, 80, 30)
    fill(255)
    animation_font = createFont("animation", 20)
    textFont(animation_font)
    text(("Begin"), 235, 415)
    if switch == False:
        stroke(0)
        line(235, 385, 245, 375)
        line(275, 385, 285, 375)
        line(310, 405, 320, 415)
        line(235, 435, 245, 445)
        line(275, 435, 285, 445) 
        if frameCount % 25 == 0:
            switch = True
    elif switch == True:
        stroke(0)  
        line(235, 385, 225, 375)
        line(275, 385, 265, 375)
        line(310, 405, 320, 395)
        line(235, 435, 225, 445)
        line(275, 435, 265, 445)  
        if frameCount % 25 == 0:
            switch = False

    
def pipes_move_variables():
    global pipes, pipe1, pipe2, pipe3, topleftx1, toplefty1, bottomleftx1, bottomlefty1, topleftx2, toplefty2, bottomleftx2, bottomlefty2, topleftx3, toplefty3, bottomleftx3, bottomlefty3
    temp = 0
    pipes = [[300, 0, temp, temp, 350, 200],[ 300, 400, temp, temp, 400, 200], [1, 2, temp, temp,  5, 6],[ 3, 4, temp, temp, 5, 6], [1, 2, temp, temp, 5, 6],[3, 4, temp, temp, 5, 6]] #[topleftx,toplefty,bottomleftx, bottomlefty, length, width] 
 
    topleftx1 = pipes[0][0]
    toplefty1 = pipes[0][1] + pipes[0][4]
    topleftx2 = pipes[2][0]
    toplefty2 = pipes[2][1] + pipes[2][4]
    topleftx3 = pipes[4][0]
    toplefty3 = pipes[4][1] + pipes[4][4]

    bottomleftx1 = pipes[1][0]
    bottomlefty1 = pipes[1][1] + pipes[1][4]
    bottomleftx2 = pipes[3][0]
    bottomlefty2 = pipes[3][1] + pipes[3][4]
    bottomleftx3 = pipes[5][0]
    bottomlefty3 = pipes[5][1] + pipes[5][4]
    
    
    #[topleftx,toplefty,bottomleftx, bottomlefty, length, width] 
    #pipe1/2/3 = [[top], [bottom]]
    pipe1 = [[300, 0, topleftx1, toplefty1, 280, 100],[ 300, 483, bottomleftx1, bottomlefty1, 280, 100]]
    pipe2 = [[550, 0, topleftx2, toplefty2, 375, 100], [ 550, 563, bottomleftx2, bottomlefty2, 200, 100]]
    pipe3 = [[800, 0, topleftx3, toplefty3, 120, 100], [800, 363, bottomleftx3, bottomlefty3, 400, 100]]
     

    
def pipes_move():
    global pipe1, speed
    stroke('#228C22')
    fill('#228C22')
    #1st set of pipes
    #Top
    rect(pipe1[0][0],pipe1[0][1], pipe1[0][5], pipe1[0][4])
    pipe1[0][0] -= speed
    #bottom
    rect(pipe1[1][0],pipe1[1][1], pipe1[1][5], pipe1[1][4])
    pipe1[1][0] -= speed
         
    #2nd set of pipes
    #Top
    rect(pipe2[0][0],pipe2[0][1], pipe2[0][5], pipe2[0][4])
    pipe2[0][0] -= speed
    #Bottom
    rect(pipe2[1][0],pipe2[1][1], pipe2[1][5], pipe2[1][4])
    pipe2[1][0] -= speed
    
    #3rd set of pipes
    #Top
    rect(pipe3[0][0],pipe3[0][1], pipe3[0][5], pipe3[0][4])
    pipe3[0][0] -= speed
    #Bottom
    rect(pipe3[1][0],pipe3[1][1], pipe3[1][5], pipe3[1][4])
    pipe3[1][0] -= speed
    #3rd set of pipes

    
    
def reset_pipes():
    global pipe1, pipe2, pipe3
    #pipe1
    #check if top reached end
    if (pipe1[0][0] + pipe1[0][5]) <= 0:
            pipe1[0][0] = 675
            pipe1[0][4] += 10
    #check if bottom reached end
    if (pipe1[1][0] + pipe1[1][5]) <= 0:
            pipe1[1][0] = 675
    #pipe2
    #check if top reached end
    if (pipe2[0][0] + pipe2[0][5]) <= 0:
            pipe2[0][0] = 675
    #check if bottom reached end
    if (pipe2[1][0] + pipe2[1][5]) <= 0:
            pipe2[1][0] = 675  
            pipe2[1][4] += 10
            pipe2[1][1] = 763 - pipe2[1][4]
            
    #pipe3
    if (pipe3[0][0] + pipe3[0][5]) <= 0:
            pipe3[0][0] = 675
            pipe3[0][4] += 10
    #check if bottom reached end
    if (pipe3[1][0] + pipe3[1][5]) <= 0:
            pipe3[1][0] = 675

    
    
def check_lengths():
    global pipe1, pipe2, pipe3
    #check pipe 1
    if (pipe1[1][1] - pipe1[0][1]) <= 95:
        pipe1[0][4] = 350
    #check pipe 2
    if (pipe2[1][1] - pipe2[0][1]) <= 95:
        pipe2[1][4] = 200
        pipe2[1][1] = 700
    #check pipe 3
    if (pipe3[1][1] - pipe3[0][1]) <= 95:
        pipe3[1][4] = 500
        

    
    

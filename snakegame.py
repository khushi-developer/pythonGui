import pygame
import random
import os

pygame.mixer.init()


pygame.init()

# defining colors
white = (255,255,255)
red = (255,0,0)
black =(0,0,0)

screen_width = 900
screen_height = 600

#creating game window
game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snake gamewithkhushi")

bgimg1=pygame.image.load("back1.jpg")
bgimg1=pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()


clk = pygame.time.Clock()
font =  pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window, color , snk_list, snake_width, snake_height):
    for x,y in snk_list:
        pygame.draw.rect(game_window, black, [x, y, snake_width, snake_height]) #creating head of sanke

def welcome():
    game_exit = False
    while not game_exit:
        game_window.fill((201,229,213))
        text_screen("welcome to snake game",black,200,250)
        text_screen("Enter space bar to play game",black,200,290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('water.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clk.tick(60)




#game loop
def game_loop():

    #creating game specific variables
    game_exit = False
    game_over = False

    food_x = random.randint(20,screen_width/2) 
    food_y = random.randint(20, screen_height/2)

    snake_x = 45
    snake_y = 55
    snake_width = 10
    snake_height = 10
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score = 0

    snk_list=[]
    snk_length = 1

    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    while not game_exit:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            game_window.fill(white)
            text_screen("game over! press enter to continue",red,100,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x=  -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0


                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score = score + 10
                food_x = random.randint(20,screen_width/2) 
                food_y = random.randint(20, screen_height/2)
                snk_length+=5
                if score>int(hiscore):
                    hiscore=score


            game_window.fill(white)
            game_window.blit(bgimg1,(0,0))
            text_screen("score :"+str(score)+"   hiscore : "+str(hiscore),red,5,5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_width, snake_height]) #creating head of sanke

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            if head in snk_list[ :-1]:
                game_over = True
        
            # pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_width, snake_height]) #creating head of sanke
            plot_snake(game_window,black,snk_list,snake_width,snake_height)
        pygame.display.update()
        clk.tick(fps)

    pygame.quit()
    quit()

welcome()
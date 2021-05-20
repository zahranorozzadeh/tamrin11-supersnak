import pygame
import random
import sys
import time

pygame.init()

class Apple:
    def __init__(self):
        self.w = 18
        self.h = 18
        self.x = random.randrange(40, width - 40)
        self.y = random.randrange(40, height - 40)
        self.color = (138, 43, 226)
        self.image = pygame.image.load("apple.png")
        self.app = pygame.transform.scale(self.image, (20, 20))

    def show(self):
        d.blit(self.app, [self.x, self.y])

class Pear:
    def __init__(self):
        self.w = 18
        self.h = 18
        self.x = random.randrange(40, width - 40)
        self.y = random.randrange(40, height - 40)
        self.color = (138, 43, 226)
        self.image = pygame.image.load("pear.png")
        self.pe = pygame.transform.scale(self.image, (20, 20))

    def show(self):
        d.blit(self.pe, [self.x, self.y])


class Mine:
    def __init__(self):
        self.w = 18
        self.h = 18
        self.x = random.randrange(40, width - 40)
        self.y = random.randrange(40, height - 40)
        self.color = (138, 43, 226)
        self.image = pygame.image.load("mine.png")
        self.mi = pygame.transform.scale(self.image, (20, 20))

    def show(self):
        d.blit(self.mi, [self.x, self.y])



class Snake:
    def  __init__(self) :
        self.w = 10
        self.h = 10
        self.x = width / 2
        self.y = height / 2
        self.pos=[self.x,self.y] 
        self.name = "mohammad ali"
        self.color = (0,127,0)
        self.speed =2
        self.score = 0
        self.x_change=0
        self.y_change=0
        self.body = [[self.pos[0], self.pos[1]], [self.pos[0] - 5, self.pos[1]], [self.pos[0] - (2 * 5), self.pos[1]]]#***

    def eatApple(self):
        if apple.x - apple.w <= self.pos[0] <= apple.x + apple.w and apple.y - apple.h <= self.pos[1] <= apple.y + apple.h:
            self.score += 1
            self.body.append(self.pos)
            self.speed += 1
            return True
        else:
            return False

    def eatPear(self):
        if pear.x - pear.w <= self.pos[0] <= pear.x + pear.w and pear.y - pear.h <= self.pos[1] <= pear.y + pear.h:
            self.score += 2
            self.body.append(self.pos)
            self.body.append(self.pos)
            self.speed += 2
            return True
        else:
            return False


    def eatMine(self):
        if mine.x - mine.w <= self.pos[0] <= mine.x + mine.w and mine.y - mine.h <= self.pos[1] <= mine.y + mine.h:
            self.score -= 1
            self.body.remove(self.pos)
            self.speed -= 1
            return True
        else:
            return False

    def show(self):
        pygame.draw.rect(d, self.color, [self.pos[0], self.pos[1], self.w, self.h])
        for item in self.body:
            pygame.draw.rect(d, self.color, [item[0], item[1], self.w, self.h])#***

    def move(self):
        if self.x_change == -1:
            self.pos[0] -= self.speed
        elif self.x_change == 1:
            self.pos[0] += self.speed
        elif self.y_change == -1:
            self.pos[1] -= self.speed
        elif self.y_change == 1:
            self.pos[1] += self.speed

        self.body.append(list(self.pos))#***
        self.body.pop(0)#***    

    def Body(self):
        self.body.append(self.pos)

if __name__ == "__main__":
    width = 700
    height = 500

    d = pygame.display.set_mode((width, height))
    pygame.display.set_caption('snake game')
    font = pygame.font.SysFont('comicsansms', 40)
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()
    pear = Pear()
    mine = Mine()


    
    while 1:
        d.fill((0, 0, 0))
        main_menu_message = font.render('Press anywhere to start the game', True, (255, 255, 255))
        font_pos = main_menu_message.get_rect(center=(width // 2, height // 2))
        d.blit(main_menu_message, font_pos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                snake.x_change = -1
                                snake.y_change = 0
                            elif event.key == pygame.K_d:
                                snake.x_change = 1
                                snake.y_change = 0
                            elif event.key == pygame.K_w:
                                snake.y_change = -1
                                snake.x_change = 0
                            elif event.key == pygame.K_s:
                                snake.y_change = 1
                                snake.x_change = 0
                        elif event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()




        
                    snake.move()
                    if snake.eatApple():
                        snake.Body()
                        apple = Apple()

                    if snake.eatPear():
                        snake.Body()
                        pear = Pear()

                    if snake.eatMine():
                        snake.Body()
                        mine = Mine()

                    d.fill((0, 0, 0))

                    snake.show()
                    apple.show()
                    pear.show()
                    mine.show()

                    font = pygame.font.SysFont('comicsansms', 20)
                    score_font = font.render("Score: " + str(snake.score), True, (255, 255, 0))
                    font_pos = score_font.get_rect(center=(width // 2 - 40, 30))
                    d.blit(score_font, font_pos)

                    if snake.score < 0:
                        img = pygame.image.load('GameOver.png')
                        game_over = pygame.transform.scale(img, (width, height))
                        d.blit(game_over, [0, 0])
                        

                    if snake.pos[0] > width or snake.pos[0] < 0 or snake.pos[1] > height or snake.pos[1] < 0:
                        img = pygame.image.load('GameOver.png')
                        game_over = pygame.transform.scale(img, (width, height))
                        d.blit(game_over, [0, 0])
                     
        
                    pygame.display.update()
                    clock.tick(30)

            elif event.type == pygame.QUIT:
                pygame.quit()



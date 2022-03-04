import random
from random import randrange
import pygame


def block_moment(screen, agent, x, y):
    """
    :param screen: object of window
    :param agent: image object
    :param x , y: coordinates
    """
    screen.blit(agent, (x, y))
    pygame.display.flip()


def game():
    pygame.init()
    size = (500, 250)  # size (100 x 50) cells to (500 x 250) pixel aspect ratio of 1:5
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyGame Test")

    # Adding background
    screen.fill((240, 240, 240))

    x_coordinates = []
    y_coordinates = []

    # load resources
    # x = 470
    # y = 220
    # x = randrange(0, 490)
    # y = randrange(0, 240)

    agent = pygame.image.load("img\\x.png")
    target = pygame.image.load("img\\o.png")
    obstacle = pygame.image.load("img\\line.png")
    obstacle2 = obstacle3 = obstacle
    obstacle = pygame.transform.scale(obstacle, (randrange(30, 50), randrange(15, 25)))
    obstacle = pygame.transform.rotate(obstacle, random.choice(range(0, 360 + 45 - (360 % 45), 45)))
    obstacle2 = pygame.transform.scale(obstacle2, (randrange(30, 50), randrange(15, 25)))
    obstacle2 = pygame.transform.rotate(obstacle2, random.choice(range(0, 360 + 45 - (360 % 45), 45)))
    obstacle3 = pygame.transform.scale(obstacle3, (randrange(30, 50), randrange(15, 25)))
    obstacle3 = pygame.transform.rotate(obstacle3, random.choice(range(0, 360 + 45 - (360 % 45), 45)))


    # First obstacle coordinates
    obstaclex = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
    obstacley = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))

    for i in range(obstaclex, obstaclex + obstacle.get_width() + 1):
        x_coordinates.append(i)
    for i in range(obstacley, obstacley + obstacle.get_height() + 1):
        y_coordinates.append(i)
    # print("x_coordinates= " + str(x_coordinates))
    # print("obstaclex= " + str(obstaclex))
    # print("shape x's size= " + str(obstaclex + obstacle.get_width()))
    # print("obstacley= " + str(obstacley))
    # print("shape y's size= " + str(obstacley + obstacle.get_height()))
    # print("obstacle size= " + str(obstacle.get_size()))

    # Second obstacle coordinates
    check_obstacle2 = False
    while not check_obstacle2:
        obstacle2x = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
        obstacle2y = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))
        if not x_coordinates.__contains__(obstacle2x) and not y_coordinates.__contains__(obstacle2y):
            check_obstacle2 = True

    for i in range(obstacle2x, obstacle2x + obstacle2.get_width() + 1):
        x_coordinates.append(i)
    for i in range(obstacle2y, obstacle2y + obstacle2.get_height() + 1):
        y_coordinates.append(i)
    print("obstacle2x= " + str(obstacle2x))
    print("obstacle2y= " + str(obstacle2y))

    # Third obstacle coordinates
    check_obstacle3 = False
    while not check_obstacle3:
        obstacle3x = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
        obstacle3y = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))
        if not x_coordinates.__contains__(obstacle3x) and not y_coordinates.__contains__(obstacle3y):
            check_obstacle3 = True

    for i in range(obstacle3x, obstacle3x + obstacle3.get_width() + 1):
        x_coordinates.append(i)
    for i in range(obstacle3y, obstacle3y + obstacle3.get_height() + 1):
        y_coordinates.append(i)
    print("obstacle3x= " + str(obstacle3x))
    print("obstacle3y= " + str(obstacle3y))

    # Target coordinates
    check_target3 = False
    while not check_target3:
        targetx = random.choice(range(0, 470 + 5 - (470 % 5), 5))
        targety = random.choice(range(0, 220 + 5 - (220 % 5), 5))
        if not x_coordinates.__contains__(targetx) and not y_coordinates.__contains__(targety):
            check_target3 = True

    for i in range(targetx, targetx + target.get_width() + 1):
        x_coordinates.append(i)
    for i in range(targety, targety + target.get_height() + 1):
        y_coordinates.append(i)
    print("targetx= " + str(targetx))
    print("targety= " + str(targety))

    # Agent coordinates
    check_target3 = False
    while not check_target3:
        x = random.choice(range(0, 470 + 5 - (470 % 5), 5))
        y = random.choice(range(0, 220 + 5 - (220 % 5), 5))
        if not x_coordinates.__contains__(x) and not y_coordinates.__contains__(y):
            check_target3 = True

    # for i in range(x, x + agent.get_width() + 1):
    #     x_coordinates.append(i)
    # for i in range(y, y + agent.get_height() + 1):
    #     y_coordinates.append(i)
    print("x= " + str(x))
    print("y= " + str(y))

    screen.blit(obstacle, (obstaclex, obstacley))

    screen.blit(obstacle2, (obstacle2x, obstacle2y))
    screen.blit(obstacle3, (obstacle3x, obstacle3y))
    screen.blit(target, (targetx, targety))
    screen.blit(agent, (x, y))
    print(obstacle.get_size())
    # print(obstacle2.get_size())
    # print(obstacle3.get_size())
    print(agent.get_size())
    # print(target.get_size())

    running = True
    while running:
        #
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 30
                    block_moment(screen, agent, x, y)
                elif event.key == pygame.K_DOWN:
                    y += 30
                    block_moment(screen, agent, x, y)
                elif event.key == pygame.K_RIGHT:
                    x += 30
                    block_moment(screen, agent, x, y)
                elif event.key == pygame.K_LEFT:
                    x -= 30
                    block_moment(screen, agent, x, y)
            elif event.type == pygame.QUIT:
                running = False

        # Update the screen
        pygame.display.flip()


if __name__ == "__main__":
    game()

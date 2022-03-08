import math
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

    # Arrays to store the coordinates
    preserved_coordinates = []
    target_coordinates = []

    # Load resources
    agent = pygame.image.load("img\\x.png")
    target = pygame.image.load("img\\o.png")
    obstacle = pygame.image.load("img\\line.png")
    obstacle2 = obstacle3 = obstacle

    # Scaling and rotating the obstacles
    obstacle = pygame.transform.scale(obstacle, (randrange(30, 50), randrange(15, 25)))
    obstacle = pygame.transform.rotate(obstacle, random.choice(range(0, 360 + 45 - (360 % 45), 45)))
    obstacle2 = pygame.transform.scale(obstacle2, (randrange(30, 50), randrange(15, 25)))
    obstacle2 = pygame.transform.rotate(obstacle2, random.choice(range(0, 360 + 45 - (360 % 45), 45)))
    obstacle3 = pygame.transform.scale(obstacle3, (randrange(30, 50), randrange(15, 25)))
    obstacle3 = pygame.transform.rotate(obstacle3, random.choice(range(0, 360 + 45 - (360 % 45), 45)))

    # Give obstacles, target, and agent random coordinates and should cross each other
    # First obstacle coordinates
    obstaclex = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
    obstacley = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))
    # Add the objects coordinates to the preserved_coordinates array
    for i in range(obstaclex, obstaclex + obstacle.get_width() + 1):
        for j in range(obstacley, obstacley + obstacle.get_height() + 1):
            preserved_coordinates.append((i, j))
    print("obstaclex= " + str(obstaclex))
    print("obstacley= " + str(obstacley))

    # Second obstacle coordinates
    check_obstacle2 = False
    obstacle2_width = obstacle2.get_width() + 1
    obstacle2_height = obstacle2.get_height() + 1
    # Check if the generated random coordinates do exist in the preserved_coordinates array
    while not check_obstacle2:
        obstacle2x = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
        obstacle2y = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))
        if not preserved_coordinates.__contains__((obstacle2x, obstacle2y)) \
                and not preserved_coordinates.__contains__((obstacle2x + obstacle2_width, obstacle2y)) \
                and not preserved_coordinates.__contains__((obstacle2x, obstacle2y + obstacle2_height)) \
                and not preserved_coordinates.__contains__(
            (obstacle2x + obstacle2_width, obstacle2y + obstacle2_height)) \
                and not preserved_coordinates.__contains__((math.floor(obstacle2x + obstacle2_width / 2),
                                                            math.floor(obstacle2y + obstacle2_height / 2))):
            check_obstacle2 = True

    # Add the new  generated coordinates to the preserved_coordinates array
    for i in range(obstacle2x, obstacle2x + obstacle2_width):
        for j in range(obstacle2y, obstacle2y + obstacle2_height):
            preserved_coordinates.append((i, j))
    print("obstacle2x= " + str(obstacle2x))
    print("obstacle2y= " + str(obstacle2y))

    # Third obstacle coordinates
    check_obstacle3 = False
    obstacle3_width = obstacle3.get_width() + 1
    obstacle3_height = obstacle3.get_height() + 1
    # Check if the generated random coordinates do exist in the preserved_coordinates array
    while not check_obstacle3:
        obstacle3x = (random.choice(range(0, 470 + 5 - (470 % 5), 5)))
        obstacle3y = (random.choice(range(0, 220 + 5 - (220 % 5), 5)))
        if not preserved_coordinates.__contains__((obstacle3x, obstacle3y)) \
                and not preserved_coordinates.__contains__((obstacle3x + obstacle3_width, obstacle3y)) \
                and not preserved_coordinates.__contains__((obstacle3x, obstacle3y + obstacle3_height)) \
                and not preserved_coordinates.__contains__(
            (obstacle3x + obstacle3_width, obstacle3y + obstacle3_height)) \
                and not preserved_coordinates.__contains__((math.floor(obstacle3x + obstacle3_width / 2),
                                                            math.floor(obstacle3y + obstacle3_height / 2))):
            check_obstacle3 = True

    # Add the new  generated coordinates to the preserved_coordinates array
    for i in range(obstacle3x, obstacle3x + obstacle3_width):
        for j in range(obstacle3y, obstacle3y + obstacle3_height):
            preserved_coordinates.append((i, j))
    print("obstacle3x= " + str(obstacle3x))
    print("obstacle3y= " + str(obstacle3y))

    # Target coordinates
    check_target = False
    target_width = target.get_width() + 1
    target_height = target.get_height() + 1
    # Check if the generated random coordinates do exist in the preserved_coordinates array
    while not check_target:
        targetx = random.choice(range(0, 470 + 5 - (470 % 5), 5))
        targety = random.choice(range(0, 220 + 5 - (220 % 5), 5))
        if not preserved_coordinates.__contains__((targetx, targety)) \
                and not preserved_coordinates.__contains__((targetx + target_width, targety)) \
                and not preserved_coordinates.__contains__((targetx, targety + target_height)) \
                and not preserved_coordinates.__contains__((targetx + target_width, targety + target_height)) \
                and not preserved_coordinates.__contains__((math.floor(targetx + target_width / 2),
                                                            math.floor(targety + target_height / 2))):
            check_target = True

    # Add the new  generated coordinates to the preserved_coordinates array
    for i in range(targetx, targetx + target_width):
        for j in range(targety, targety + target_height):
            preserved_coordinates.append((i, j))
            target_coordinates.append((i, j))
    print("targetx= " + str(targetx))
    print("targety= " + str(targety))

    # Agent coordinates
    check_agent = False
    agent_width = agent.get_width() + 1
    agent_height = agent.get_height() + 1
    # Check if the generated random coordinates do exist in the preserved_coordinates array
    while not check_agent:
        agentx = random.choice(range(0, 470 + 5 - (470 % 5), 5))
        agenty = random.choice(range(0, 220 + 5 - (220 % 5), 5))
        if not preserved_coordinates.__contains__((agentx, agenty)) \
                and not preserved_coordinates.__contains__((agentx + agent_width, agenty)) \
                and not preserved_coordinates.__contains__((agentx, agenty + agent_height)) \
                and not preserved_coordinates.__contains__((agentx + agent_width, agenty + agent_height)) \
                and not preserved_coordinates.__contains__((math.floor(agentx + agent_width / 2),
                                                            math.floor(agenty + agent_height / 2))):
            check_agent = True

    print("x= " + str(agentx))
    print("y= " + str(agenty))
    print("0.5 x= " + str(math.floor((agentx + agent_width / 2))))
    print("0.5 y= " + str(math.floor(agenty + agent_height / 2)))
    print("x + agent_width= " + str(agentx + agent_width))
    print("y + agent_height= " + str(agenty + agenty + agent_height))
    print(preserved_coordinates)

    # Put the objects to the screen
    screen.blit(obstacle, (obstaclex, obstacley))
    screen.blit(obstacle2, (obstacle2x, obstacle2y))
    screen.blit(obstacle3, (obstacle3x, obstacle3y))
    screen.blit(target, (targetx, targety))
    screen.blit(agent, (agentx, agenty))

    # Create a circle to draw the path to the target
    agent_centerx = agentx + agent_width / 2
    agent_centery = agenty + agent_height / 2
    pygame.draw.circle(screen, (255, 0, 0), (agent_centerx, agent_centery), 5)

    distance_x = None
    distance_y = None
    if agentx < targetx and agenty < targety:
        # state 1
        print("state 1")
        distance_x = targetx - agentx
        distance_y = targety - agenty
        # goal_reached = False
        # while not goal_reached:
        for i in range(agentx + math.floor(agent_width / 2), (agentx + math.floor(agent_width / 2)) + distance_x, 15):
            pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)
        for j in range(agenty + math.floor(agent_height / 2), (agenty + math.floor(agent_height / 2)) + distance_y, 15):
            pygame.draw.circle(screen, (255, 0, 0), (agentx + math.floor(agent_width / 2) + distance_x, j), 5)
    elif agentx < targetx and agenty > targety:
        # state 2
        print("state 2")
        distance_x = targetx - agentx
        # while not goal_reached:
        for i in range(agentx + math.floor(agent_width / 2), (agentx + math.floor(agent_width / 2)) + distance_x, 15):
            pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)
        for j in range(agenty + math.floor(agent_height / 2), targety + math.floor(target_height / 2), -15):
            pygame.draw.circle(screen, (255, 0, 0), (agentx + math.floor(agent_width / 2) + distance_x, j), 5)
    elif agentx > targetx and agenty > targety:
        # state 3
        print("state 3")
        # goal_reached = False
        # while not goal_reached:
        for i in range(targetx + math.floor(target_width / 2), (agentx + math.floor(agent_width / 2)), +15):
            pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)
        for j in range(targety + math.floor(target_height / 2), agenty + math.floor(agent_height / 2), 15):
            pygame.draw.circle(screen, (255, 0, 0), (targetx + math.floor(target_width / 2), j), 5)
    elif agentx > targetx and agenty < targety:
        # state 4
        print("state 4")
        distance_x = targetx - agentx
        # while not goal_reached:
        for i in range(targetx + math.floor(target_width / 2), (agentx + math.floor(agent_width / 2)), 15):
            pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)
        for j in range(agenty + math.floor(agent_height / 2), targety + math.floor(target_height / 2), 15):
            pygame.draw.circle(screen, (255, 0, 0), (agentx + math.floor(agent_width / 2) + distance_x, j), 5)
    elif agentx == targetx:
        print("state 5")
        if agenty > targety:
            print("state 5 1")
            for j in range(targety + math.floor(target_height / 2), agenty + math.floor(agent_height / 2), 15):
                pygame.draw.circle(screen, (255, 0, 0), (agentx + math.floor(agent_width / 2), j), 5)
        elif agenty < targety:
            print("state 5 2")
            for j in range(agenty + math.floor(agent_height / 2), targety + math.floor(target_height / 2), 15):
                pygame.draw.circle(screen, (255, 0, 0), (agentx + math.floor(agent_width / 2), j), 5)
    elif agenty == targety:
        print("state 6")
        if agentx > targetx:
            print("state 6 1")
            for i in range(targetx + math.floor(target_width / 2), (agentx + math.floor(agent_width / 2)), 15):
                pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)
        elif agenty < targety:
            print("state 6 2")
            for i in range((agentx + math.floor(agent_width / 2)), targetx + math.floor(target_width / 2), 15):
                pygame.draw.circle(screen, (255, 0, 0), (i, agenty + math.floor(agent_height / 2)), 5)

    # Do action while the game is on
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the screen
        pygame.display.flip()


if __name__ == "__main__":
    game()

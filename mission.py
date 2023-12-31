'''
EN.640.635 Software Carpentry
Final project
This Python file defines a 2D simulation environment
for a mission involving a robot fish, balls, and goals within a bordered pool.
The script sets up the environment, objects within it,
and contains a function to determine the completion of a mission.
It uses custom classes such as Circle, RobotFish, Pool,
and goal to represent different entities in the simulation.
'''
from env import *

# Set up environment parameters
border_x = 1400
border_y = 800

# The distance between the balls
ball_dx = 60
ball_dy = 40
# Posistion of the balls
ball_x = int(border_x * 3 / 4 - ball_dx)
ball_y = int(border_y / 2)
# Radius of the balls
ball_r = 20
# Color of the balls
ball_color = (0, 100, 100)

# Posistion of the fish
fish_x = int(border_x / 6)
fish_y = int(border_y / 2)


# Posistion of the goals
goal1_x = int(border_x / 2)
goal1_y = int(border_y / 2)
# The distance between the goals
goal_dx = 90
goal_dy = 60
# Radius of the goals
goal_r = 30
# Color of the goals
goal_color = (100, 0, 100)
# Name of the task
task_name = "robotfish"
width = 100


def mission():
    """
    Define mission environment with circles and goals.
    """

    # Define balls
    Circle(
        name="ball",
        num=1,
        shape="circle",
        mass=1,
        n=1,
        relative_points={
            'p0': (
                0,
                0)},
        color=ball_color,
        x=ball_x,
        y=ball_y,
        x_dot=0,
        y_dot=0,
        radius=ball_r)

    # ball2 = Circle(name="ball", num=2, shape="circle",
    # mass=1, n=1, relative_points={'p0': (0, 0)},
    # color=ball_color, x=ball_x + ball_dx, y=ball_y + ball_dy, x_dot=0,
    # y_dot=0, radius=ball_r)

    # Define goals
    goal(
        name="goal",
        num=1,
        shape='circle',
        n=1,
        relative_points={
            'p0': (
                0,
                0)},
        color=goal_color,
        x=goal1_x,
        y=goal1_y,
        x_dot=0,
        y_dot=0,
        draw_radius=goal_r)

    # goal2 = goal(name="goal", num=2, shape='circle', n=1,
    # relative_points={'p0': (0, 0)}, color=goal_color,
    # x=goal1_x - goal_dx, y=goal1_y + goal_dy, x_dot=0, y_dot=0,
    # draw_radius=goal_r)

    # Define robot fish
    RobotFish(
        name='robotfish',
        num=1,
        shape='polygon',
        mass=10,
        n=6,
        relative_points={},
        color=ball_color,
        x=fish_x,
        y=fish_y,
        x_dot=0,
        y_dot=0,
        theta=0)

    # Define pools
    # top border
    Pool(name="pool", num=1, shape='polygon', n=4,
         relative_points={'p0': (-int(border_x / 2), -width),
                          'p1': (int(border_x / 2), -width),
                          'p2': (int(border_x / 2), width),
                          'p3': (-int(border_x / 2), width)},
         x=700, y=-100)
    # left border
    Pool(name="pool", num=1, shape='polygon', n=4,
         relative_points={'p0': (-width, -int(border_y / 2)),
                          'p1': (-width, int(border_y / 2)),
                          'p2': (width, int(border_y / 2)),
                          'p3': (width, -int(border_y / 2))},
         x=-100, y=400)
    # bottom border
    Pool(name="pool", num=1, shape='polygon', n=4,
         relative_points={'p0': (-int(border_x / 2), -width),
                          'p1': (-int(border_x / 2), width),
                          'p2': (int(border_x / 2), width),
                          'p3': (int(border_x / 2), -width)},
         x=700, y=900)
    # right border
    Pool(name="pool", num=1, shape='polygon', n=4,
         relative_points={'p0': (-width, -int(border_x / 2)),
                          'p1': (-width, int(border_x / 2)),
                          'p2': (width, int(border_x / 2)),
                          'p3': (width, -int(border_x / 2))},
         x=1500, y=400)


def win():
    """
    Check if a goal is reached by colliding with a ball.
    """
    ab_num = []
    for a in father_obj:
        if a.name == 'goal':
            for b in a.colliding_list:
                if b.name == 'ball':
                    if ab_num.count((a.num, b.num)) == 0:
                        ab_num.append((a.num, b.num))
                        return True
    return False

#https://github.com/AtsushiSakai/PythonRobotics/blob/master/AerialNavigation/drone_3d_trajectory_following/drone_3d_trajectory_following.py
from math import cos, sin
import numpy as np

show_animation = True

def calculate_position(c, t):
    """
    Calculates a position given a set of quintic coefficients and a time.

    Args
        c: List of coefficients generated by a quintic polynomial trajectory generator.
        t: Time at which to calculate the position

    Returns
        Position
    """

    return c[0] * t**5 + c[1] * t**4 + c[2] * t**3 + c[3] * t**2 + c[4] * t + c[5]





def calculate_velocity(c, t):
    """
    Calculates a velocity given a set of quintic coefficients and a time.

    Args
        c: List of coefficients generated by a quintic polynomial trajectory generator.
        t: Time at which to calculate the velocity

    Returns
        Velocity
    """

    return 5 * c[0] * t**4 + 4 * c[1] * t**3 + 3 * c[2] * t**2 + 2 * c[3] * t + c[4]





def calculate_acceleration(c, t):
    """
    Calculates an acceleration given a set of quintic coefficients and a time.

    Args
        c: List of coefficients generated by a quintic polynomial trajectory generator.
        t: Time at which to calculate the acceleration

    Returns
        Acceleration
    """

    return 20 * c[0] * t**3 + 12 * c[1] * t**2 + 6 * c[2] * t + 2 * c[3]

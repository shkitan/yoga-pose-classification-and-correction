import math
import pickle
import pandas as pd
import numpy as np


def b(data, x1, x2, y1, y2):
    """
    Calculate the value of 'b' in a linear equation (y = mx + b) given two
    points (x1, y1) and (x2, y2).

    inorder to prevent 0 derivation I add (math.e) ** (-10))
    :param data: Dictionary or list containing the data points.
    :param x1: Index or key of the first x-coordinate.
    :param x2: Index or key of the second x-coordinate.
    :param y1: Index or key of the first y-coordinate.
    :param y2: Index or key of the second y-coordinate.
    :return: The value of 'b' in the linear equation (y = mx + b).
    """
    b = (data[x1] * data[y2] - data[x2] * data[y1]) / (data[x1] - data[x2] +
                                                       (math.e) ** (-10))
    return b


def m(data, x1, x2, y1, y2):
    """
    Calculate the slope 'm' of a line passing through two points (x1, y1) and (x2, y2).
    :param data: Dictionary or list containing the data points.
    :param x1: Index or key of the first x-coordinate.
    :param x2: Index or key of the second x-coordinate.
    :param y1: Index or key of the first y-coordinate.
    :param y2: Index or key of the second y-coordinate.
    :return: The slope 'm' of the line passing through the two points.
    """
    if (data[x1] == data[x2]):
        return 0
    m = (data[y1] - data[y2]) / (data[x1] - data[x2])
    return m

def angle(data, m1_str, m2_str):
    """
    Calculate the angle between two lines represented by their slopes.
    :param data: Dictionary or list containing the data points.
    :param m1_str: String representation of the slope of the first line.
    :param m2_str: String representation of the slope of the second line.
    :return: The angle between the two lines in degrees.
    """
    m1 = data[m1_str]
    m2 = data[m2_str]
    if m1==0:
        a = math.degrees(np.abs(math.atan(((m2)))))
        return 90-a
    elif m2==0:
        a = math.degrees(np.abs(math.atan(((m1)))))
        return 90-a
    try:
        angle = math.degrees(np.abs(math.atan(((m1 - m2) / (1 + m1 * m2)))))
    except ZeroDivisionError:
        angle = math.degrees(np.abs(math.atan((m1 - m2) / 0.001)))
    if angle < 0:
        return angle + 180
    return angle

def get_the_small_angle(data, m1_str, m2_str):
    """
    Calculate the smaller angle between two lines represented by their slopes.
    :param data: Dictionary or list containing the data points.
    :param m1_str: String representation of the slope of the first line.
    :param m2_str: String representation of the slope of the second line.
    :return: The smaller angle between the two lines in degrees.
    """
    x=angle(data, m1_str, m2_str)
    return 180-x



###########################Joint calculation functions#########################
# In this section we have a calculati on the angle all joints in the human
# body based on certain conditions.


def right_arm_data_writing(data, apply_function):
    data['right_arm_top_m'] = data.apply(m, axis=1, args=('RIGHT_SHOULDER_x',
                                                          'RIGHT_ELBOW_x',
                                                          'RIGHT_SHOULDER_y',
                                                          'RIGHT_ELBOW_y'))
    data['right_arm_top_b'] = data.apply(b, axis=1, args=('RIGHT_SHOULDER_x',
                                                          'RIGHT_ELBOW_x',
                                                          'RIGHT_SHOULDER_y',
                                                          'RIGHT_ELBOW_y'))
    data['right_arm_bottom_m'] = data.apply(m, axis=1,
                                            args=('RIGHT_WRIST_x',
                                                  'RIGHT_ELBOW_x',
                                                  'RIGHT_WRIST_y',
                                                  'RIGHT_ELBOW_y'))
    data['right_arm_bottom_b'] = data.apply(b, axis=1,
                                            args=('RIGHT_WRIST_x',
                                                  'RIGHT_ELBOW_x',
                                                  'RIGHT_WRIST_y',
                                                  'RIGHT_ELBOW_y'))
    data["elbow_right_angle"] = data.apply(apply_function, axis=1,
                                           args=('right_arm_top_m',
                                                 'right_arm_bottom_m'))


def left_arm_data_writing(data, apply_function):
    data['left_arm_top_m'] = data.apply(m, axis=1, args=('LEFT_SHOULDER_x',
                                                         'LEFT_ELBOW_x',
                                                         'LEFT_SHOULDER_y',
                                                         'LEFT_ELBOW_y'))
    data['left_arm_top_b'] = data.apply(b, axis=1,args=('LEFT_SHOULDER_x',
                                                        'LEFT_ELBOW_x',
                                                        'LEFT_SHOULDER_y',
                                                        'LEFT_ELBOW_y'))
    data['left_arm_bottom_m'] = data.apply(m, axis=1, args=('LEFT_WRIST_x',
                                                            'LEFT_ELBOW_x',
                                                            'LEFT_WRIST_y',
                                                            'LEFT_ELBOW_y'))
    data['left_arm_bottom_b'] = data.apply(b, axis=1, args=('LEFT_WRIST_x',
                                                            'LEFT_ELBOW_x',
                                                            'LEFT_WRIST_y',
                                                            'LEFT_ELBOW_y'))
    data["elbow_left_angle"] = data.apply(apply_function, axis=1,
                                          args=('left_arm_top_m',
                                                'left_arm_bottom_m'))


def nose_sholder_right_data_writing(data):
    data['nose_sholder_right_m'] = data.apply(m, axis=1,
                                              args=('NOSE_x',
                                                    'RIGHT_SHOULDER_x',
                                                    'NOSE_y',
                                                    'RIGHT_SHOULDER_y'))
    data['nose_sholder_right_b'] = data.apply(b, axis=1,
                                              args=('NOSE_x',
                                                    'RIGHT_SHOULDER_x',
                                                    'NOSE_y',
                                                    'RIGHT_SHOULDER_y'))


def nose_sholder_left_data_writing(data):
    data['nose_sholder_left_m'] = data.apply(m, axis=1, args=('NOSE_x',
                                                              'LEFT_SHOULDER_x',
                                                              'NOSE_y',
                                                              'LEFT_SHOULDER_y'))
    data['nose_sholder_left_b'] = data.apply(b, axis=1, args=('NOSE_x',
                                                              'LEFT_SHOULDER_x', 'NOSE_y', 'LEFT_SHOULDER_y'))


def shoulders_data_writing(data):
    data['shoulders_m'] = data.apply(m, axis=1, args=(
        'RIGHT_SHOULDER_x', 'LEFT_SHOULDER_x', 'RIGHT_SHOULDER_y', 'LEFT_SHOULDER_y'))
    data['shoulders_b'] = data.apply(b, axis=1, args=(
        'RIGHT_SHOULDER_x', 'LEFT_SHOULDER_x', 'RIGHT_SHOULDER_y', 'LEFT_SHOULDER_y'))


def left_leg_data_writing(data, apply_function):
    data['left_leg_bottom_m'] = data.apply(m, axis=1,
                                           args=("LEFT_ANKLE_x", 'LEFT_KNEE_x', 'LEFT_ANKLE_y', 'LEFT_KNEE_y'))
    data['left_leg_bottom_b'] = data.apply(b, axis=1, args=("LEFT_ANKLE_x", 'LEFT_KNEE_x',
                                                            'LEFT_ANKLE_y', 'LEFT_KNEE_y'))
    data['left_leg_up_m'] = data.apply(m, axis=1, args=("LEFT_HIP_x",
                                                        'LEFT_KNEE_x',
                                                        'LEFT_HIP_y', 'LEFT_KNEE_y'))
    data['left_leg_up_b'] = data.apply(b, axis=1, args=("LEFT_HIP_x", 'LEFT_KNEE_x',
                                                        'LEFT_HIP_y', 'LEFT_KNEE_y'))
    data["knee_left_angle"] = data.apply(apply_function, axis=1,
                                         args=(
                                             'left_leg_up_m', 'left_leg_bottom_m'
                                         ))


def right_leg_data_writing(data, apply_function):
    data['right_leg_bottom_m'] = data.apply(m, axis=1, args=(
        "RIGHT_ANKLE_x", 'RIGHT_KNEE_x',
        'RIGHT_ANKLE_y', 'RIGHT_KNEE_y'))
    data['right_leg_bottom_b'] = data.apply(b, axis=1, args=("RIGHT_ANKLE_x", 'RIGHT_KNEE_x',
                                                             'RIGHT_ANKLE_y', 'RIGHT_KNEE_y'))
    data['right_leg_up_m'] = data.apply(m, axis=1, args=("RIGHT_HIP_x",
                                                         'RIGHT_KNEE_x',
                                                         'RIGHT_HIP_y', 'RIGHT_KNEE_y'))
    data['right_leg_up_b'] = data.apply(b, axis=1, args=("RIGHT_HIP_x", 'RIGHT_KNEE_x',
                                                         'RIGHT_HIP_y', 'RIGHT_KNEE_y'))
    data["knee_right_angle"] = data.apply(apply_function, axis=1,
                                          args=('right_leg_up_m',
                                                'right_leg_bottom_m'))

def right_shoulder_hip_data_writing(data):
    data['right_shoulder_hip_m'] = data.apply(m, axis=1,
                                              args=
                                              ('RIGHT_SHOULDER_x', 'RIGHT_HIP_x', 'RIGHT_SHOULDER_y', 'RIGHT_HIP_y'))
    data['right_shoulder_hip_b'] = data.apply(b, axis=1,
                                              args=
                                              ('RIGHT_SHOULDER_x', 'RIGHT_HIP_x', 'RIGHT_SHOULDER_y', 'RIGHT_HIP_y'))


def left_shoulder_hip_data_writing(data):
    data['left_shoulder_hip_m'] = data.apply(m, axis=1,
                                             args=('LEFT_SHOULDER_x', 'LEFT_HIP_x', 'LEFT_SHOULDER_y', 'LEFT_HIP_y'))
    data['left_shoulder_hip_b'] = data.apply(b, axis=1,
                                             args=('LEFT_SHOULDER_x', 'LEFT_HIP_x', 'LEFT_SHOULDER_y', 'LEFT_HIP_y'))


def head_angle(data):
    data["head_angle_left"] = data.apply(angle, axis=1,
                                         args=('nose_sholder_left_m',
                                               'left_arm_top_m'))
    data["head_angle_right"] = data.apply(angle, axis=1,
                                          args=('nose_sholder_right_m',
                                                'right_arm_top_m'))


def sholders_angle_data_writing(data, apply_function_left, apply_function_right):
    data["sholder_angle_left"] = data.apply(apply_function_left, axis=1,
                                            args=('left_shoulder_hip_m',
                                                  'left_arm_top_m'))
    data["sholder_angle_right"] = data.apply(apply_function_right, axis=1,
                                             args=('right_arm_top_m',
                                                   'right_shoulder_hip_m'))


def hip_angle_data_writing(data):
    data["hip_angle_left"] = data.apply(get_the_small_angle, axis=1,
                                        args=('left_leg_up_m',
                                              'left_shoulder_hip_m'))
    data["hip_angle_right"] = data.apply(get_the_small_angle, axis=1,
                                         args=('right_shoulder_hip_m',
                                               'right_leg_up_m'))


###########################Joint calculation functions#########################

def data_data_writing(name_posture, knee_left, knee_right, elbow_right,
                elbow_left, shoulders_left, shoulders_right):
    with open(name_posture, 'rb') as f:
        data = pickle.load(f)
    data = data
    left_leg_data_writing(data, knee_left)
    right_leg_data_writing(data, knee_right)
    right_arm_data_writing(data, elbow_right)
    left_arm_data_writing(data, elbow_left)
    nose_sholder_right_data_writing(data)
    nose_sholder_left_data_writing(data)
    shoulders_data_writing(data)
    right_shoulder_hip_data_writing(data)
    left_shoulder_hip_data_writing(data)
    sholders_angle_data_writing(data, shoulders_left, shoulders_right)
    hip_angle_data_writing(data)
    return data



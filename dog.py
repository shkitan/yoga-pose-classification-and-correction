from angle_comuptition import *


# #########################Test posture functions#########################
# In this section we have a calculate on the angle all joints in the human
# body based on certain conditions.

def right_shoulder(data, m1_str, m2_str):
    if data['RIGHT_SHOULDER_y'] > data['RIGHT_ELBOW_y']:
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def left_shoulder(data, m1_str, m2_str):
    if(data['LEFT_SHOULDER_y'] < data['LEFT_ELBOW_y'] and
            data['LEFT_SHOULDER_x'] < data['LEFT_ELBOW_x']):
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)
    else:
        if(data['LEFT_SHOULDER_y'] < data['LEFT_ELBOW_y'] and not
                data['LEFT_SHOULDER_x'] < data['LEFT_ELBOW_x']):
            if data['LEFT_HIP_x'] > data['LEFT_SHOULDER_x']:
                return get_the_small_angle(data, m1_str, m2_str)
            return angle(data, m1_str, m2_str)
        if data['LEFT_HIP_x'] > data['LEFT_SHOULDER_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


def right_elbow(data, m1_str, m2_str):
    if data['RIGHT_ELBOW_x'] > data['RIGHT_WRIST_x']:
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['RIGHT_ELBOW_y'] < data['RIGHT_SHOULDER_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        if data['RIGHT_ELBOW_y'] < data['RIGHT_WRIST_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def left_elbow(data, m1_str, m2_str):
    if data['LEFT_ELBOW_x'] > data['LEFT_WRIST_x']:
        if data['LEFT_ELBOW_y'] < data['LEFT_SHOULDER_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        if data['LEFT_ELBOW_y'] < data['LEFT_WRIST_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)
    else:
        if data['LEFT_ELBOW_y'] > data['LEFT_SHOULDER_y']:
            if data['LEFT_WRIST_y'] > data['LEFT_SHOULDER_y']:
                if data['LEFT_ELBOW_y'] > data['LEFT_WRIST_y']:
                    if data['LEFT_SHOULDER_x'] < data['LEFT_WRIST_x']:
                        return get_the_small_angle(data, m1_str, m2_str)
                    return angle(data, m1_str, m2_str)
                return get_the_small_angle(data, m1_str, m2_str)
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


def right_knee(data, m1_str, m2_str):
    if data['RIGHT_ANKLE_x'] > data['RIGHT_HIP_x']:
        if data['RIGHT_HIP_x'] > data['RIGHT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['RIGHT_HIP_x'] > data['RIGHT_KNEE_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def left_knee(data, m1_str, m2_str):
    if data['LEFT_ANKLE_x'] > data['LEFT_HIP_x']:
        if data['LEFT_HIP_x'] > data['LEFT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        elif data["LEFT_ANKLE_y"] < data['LEFT_KNEE_y']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data["LEFT_ANKLE_y"] < data['LEFT_KNEE_y']:
            return angle(data, m1_str, m2_str)
        if data['LEFT_HIP_x'] < data['LEFT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


# #########################Test posture functions#########################

def dog(name_posture, output_name, is_old=False):
    data = data_fixing(name_posture, left_knee, right_knee, right_elbow,
                       left_elbow, left_shoulder, right_shoulder)

    # clean outliers
    if len(data) > 1:
        data = data[(data['sholder_angle_left'] > 100)]
        data = data[(data['sholder_angle_right'] > 100)]
        data = data[(data['hip_angle_right'] < 160) & (data[
                                                          'hip_angle_right'] >
                                                       70)]
        data = data[(data['hip_angle_left'] < 160) & (data['hip_angle_left']
                                                      > 70)]
        data = data[(data['knee_left_angle'] > 165)]
        data = data[(data['knee_right_angle'] > 165)]

    if is_old:
        data["file_name"] = data["file_name"]
    data.to_pickle(output_name)

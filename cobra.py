from angle_comuptition import *


# #########################Test posture functions#########################


def shoulders_right(data, m1_str, m2_str):
    if data['RIGHT_SHOULDER_y'] > data['RIGHT_ELBOW_y']:
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)
    else:
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


def shoulders_left(data, m1_str, m2_str):
    if data['LEFT_SHOULDER_y'] < data['LEFT_ELBOW_y'] and \
            data['LEFT_SHOULDER_x'] < data['LEFT_ELBOW_x']:
        if data['LEFT_HIP_x'] > data['RIGHT_SHOULDER_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if (data['LEFT_SHOULDER_y'] < data['LEFT_ELBOW_y'] and not data[
                   'LEFT_SHOULDER_x'] < data['LEFT_ELBOW_x']):
            if data['LEFT_HIP_x'] > data['LEFT_SHOULDER_x']:
                return get_the_small_angle(data, m1_str, m2_str)
            return angle(data, m1_str, m2_str)
        if data['LEFT_HIP_x'] > data['LEFT_SHOULDER_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def elbow_right(data, m1_str, m2_str):
    if data['RIGHT_ELBOW_x'] > data['RIGHT_WRIST_x']:
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['RIGHT_ELBOW_y'] < data['RIGHT_SHOULDER_y']:
            return angle(data, m1_str, m2_str)
        if data['RIGHT_ELBOW_y'] < data['RIGHT_WRIST_y']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


def elbow_left(data, m1_str, m2_str):
    if data['LEFT_ELBOW_x'] > data['LEFT_WRIST_x']:
        if data['LEFT_ELBOW_y'] < data['LEFT_SHOULDER_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        if data['LEFT_ELBOW_y'] < data['LEFT_WRIST_y']:  # todoo!!!
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['LEFT_ELBOW_y'] > data['LEFT_SHOULDER_y']:
            if data['LEFT_WRIST_y'] > data['LEFT_SHOULDER_y']:
                if data['LEFT_ELBOW_y'] > data['LEFT_WRIST_y']:
                    if data['LEFT_SHOULDER_x'] < data['LEFT_WRIST_x']:
                        return angle(data, m1_str, m2_str)
                    return get_the_small_angle(data, m1_str, m2_str)
                return angle(data, m1_str, m2_str)
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def elbow_right_coordinates(data, m1_str, m2_str):
    if data['RIGHT_ELBOW_x'] > data['RIGHT_WRIST_x']:
        if data['RIGHT_ELBOW_y'] > data['RIGHT_SHOULDER_y']:
            if data['RIGHT_ELBOW_y'] > data['RIGHT_WRIST_y']:
                return get_the_small_angle(data, m1_str, m2_str)
            if data['RIGHT_ELBOW_x'] > data['RIGHT_SHOULDER_x']:
                return get_the_small_angle(data, m1_str, m2_str)
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)
    else:
        if data['RIGHT_ELBOW_y'] < data['RIGHT_SHOULDER_y']:
            return angle(data, m1_str, m2_str)
        if data['RIGHT_ELBOW_y'] < data['RIGHT_WRIST_y']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)


def elbow_left_coordinates(data, m1_str, m2_str):
    if data['LEFT_ELBOW_x'] > data['LEFT_WRIST_x']:
        if data['LEFT_ELBOW_y'] < data['LEFT_SHOULDER_y']:
            return angle(data, m1_str, m2_str)
        if data['LEFT_ELBOW_y'] < data['LEFT_WRIST_y']:  # todoo!!!
            if data['LEFT_ELBOW_x'] < data['LEFT_SHOULDER_x']:
                return get_the_small_angle(data, m1_str, m2_str)
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)
    else:
        if data['LEFT_ELBOW_y'] > data['LEFT_SHOULDER_y']:
            if data['LEFT_WRIST_y'] > data['LEFT_SHOULDER_y']:
                if data['LEFT_ELBOW_y'] > data['LEFT_WRIST_y']:
                    if data['LEFT_SHOULDER_x'] < data['LEFT_WRIST_x']:
                        return angle(data, m1_str, m2_str)
                    return get_the_small_angle(data, m1_str, m2_str)
                return get_the_small_angle(data, m1_str, m2_str)
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def knee_right(data, m1_str, m2_str):
    if data['RIGHT_ANKLE_x'] > data['RIGHT_HIP_x']:
        if data['RIGHT_HIP_x'] > data['RIGHT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data['RIGHT_HIP_x'] > data['RIGHT_KNEE_x']:
            return get_the_small_angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


def knee_left(data, m1_str, m2_str):
    if data['LEFT_ANKLE_x'] > data['LEFT_HIP_x']:
        if data['LEFT_HIP_x'] > data['LEFT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        return get_the_small_angle(data, m1_str, m2_str)
    else:
        if data["LEFT_ANKLE_y"] < data['LEFT_KNEE_y']:
            return get_the_small_angle(data, m1_str, m2_str)
        if data['LEFT_HIP_x'] < data['LEFT_KNEE_x']:
            return angle(data, m1_str, m2_str)
        return angle(data, m1_str, m2_str)


# #########################Test posture functions#########################

def cobra(name_posture, output_name, is_old=False):
    data = data_data_writing(name_posture, knee_left, knee_right, elbow_right,
                       elbow_left, shoulders_left, shoulders_right)

    if is_old:
        data["file_name"] = data["file_name"]

    data.to_pickle(output_name)

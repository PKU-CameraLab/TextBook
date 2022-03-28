import os
import numpy as np
import cv2 as cv

def main(path, input_id):
    depth = cv.imread(os.path.join(path, 'input', 'depth.png'), cv.IMREAD_UNCHANGED)
    depth = depth * 10.0 / 65535
    normal = cv.imread(os.path.join(path, 'input', 'normal.png'), cv.IMREAD_UNCHANGED)
    normal = normal * 2.0 / 65535 - 1.0
    diffuse = cv.imread(os.path.join(path, 'input', 'diffuse.png'), cv.IMREAD_UNCHANGED)
    diffuse = diffuse * 1.0 / 255
    specular = cv.imread(os.path.join(path, 'input', 'specular.png'), cv.IMREAD_UNCHANGED)
    specular = specular * 1.0 / 255
    shininess = cv.imread(os.path.join(path, 'input', 'shininess.png'), cv.IMREAD_UNCHANGED)
    shininess = shininess * 100.0 / 255
    image_target = cv.imread(os.path.join(path, 'input', 'task2-%d.png' % input_id), cv.IMREAD_UNCHANGED)
    cv.imshow('image_target', image_target)
    image_target = (image_target * 1.0 / 255) ** 2.2
    camera_matrix = np.array([
        [512.,   0., 512.],
        [  0., 512., 512.],
        [  0.,   0.,   1.],
    ])
    cv.imshow('depth', depth * 0.1)
    cv.imshow('normal', normal * 0.5 + 0.5)
    cv.imshow('diffuse', diffuse)
    cv.imshow('specular', specular)
    cv.imshow('shininess', shininess * 0.01)

    # Please fill in your code.
    # TA's reference answer has 45 lines. 18 lines are copied from the first task.
    # Your code generates `light_position` `light_intensity` as numpy arrays with shape of [2, 3].

    light = np.concatenate([light_position, light_intensity], axis=1)
    np.savetxt(os.path.join(path, 'output', 'task2-%d.txt' % input_id), light)

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(path, '..'))
    for input_id in range(4):
        main(path, input_id)

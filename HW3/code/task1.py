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
    light = np.loadtxt(os.path.join(path, 'input', 'task1-%d.txt' % input_id))
    light_position = light[:, :3]
    light_intensity = light[:, 3:]
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
    # TA's reference answer has 26 lines.
    # Your code generates `image` `shading_diffuse` `shading_specular` as numpy arrays with shape of [1024, 1024, 3].

    image = (np.clip(image ** (1.0 / 2.2), 0.0, 1.0) * 255).astype(np.uint8)
    shading_diffuse = (np.clip(shading_diffuse ** (1.0 / 2.2), 0.0, 1.0) * 255).astype(np.uint8)
    shading_specular = (np.clip(shading_specular ** (1.0 / 2.2), 0.0, 1.0) * 255).astype(np.uint8)
    cv.imshow('image', image)
    cv.imshow('shading_diffuse', shading_diffuse)
    cv.imshow('shading_specular', shading_specular)
    cv.imwrite(os.path.join(path, 'output', 'task1-%d.png' % input_id), image, [cv.IMWRITE_PNG_COMPRESSION, 0])
    cv.imwrite(os.path.join(path, 'output', 'task1-shading-diffuse-%d.png' % input_id), shading_diffuse, [cv.IMWRITE_PNG_COMPRESSION, 0])
    cv.imwrite(os.path.join(path, 'output', 'task1-shading-specular-%d.png' % input_id), shading_specular, [cv.IMWRITE_PNG_COMPRESSION, 0])
    cv.waitKey(0)

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(path, '..'))
    for input_id in range(4):
        main(path, input_id)

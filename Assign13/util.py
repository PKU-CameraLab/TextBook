import numpy as np
import matplotlib.pyplot as plt
import cv2

# 一般不应该修改本文件中的内容

def plot_figs(*args):
    fig, ax = plt.subplots(1, n:=len(args), figsize=(n*5, 5))
    if n == 1: ax = [ax]

    for i, (img, title) in enumerate(args):
        if "Event" in title:
            cmap = 'bwr_r'
            if "Warp" in title:
                vmin, vmax = -8, 8
            else:
                vmin, vmax = -3, 3
        else:
            cmap = 'gray'
            vmin, vmax = 0, 1

        ax[i].axis('off')
        ax[i].imshow(img, cmap=cmap, vmin=vmin, vmax=vmax)
        ax[i].set_title(title)


def load_event_npz(scene_name):
    with np.load(f'data/part_1/event/{scene_name}') as data:
        event = data['event']
        frame = data['frame']
    return event, frame


def load_spike_npz(scene_name):
    with np.load(f'data/part_1/spike/{scene_name}') as data:
        spike = data['spike']
    return spike


def get_flow_viz_map(flow_x, flow_y):
    rad = np.arctan2(-flow_y, -flow_x) / np.pi
    d = (flow_x**2 + flow_y**2)**(0.5)

    hsv = np.stack([(rad+1)*180, d/np.max(d), np.ones_like(d)], axis=-1)
    rgb = cv2.cvtColor(hsv.astype(np.float32), cv2.COLOR_HSV2RGB)
    return rgb


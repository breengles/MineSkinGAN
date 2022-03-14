import colorgram
import numpy as np
from colorgram import extract
from PIL import Image
from typing import List


def get_color_palette(colors: List[colorgram.Color], height=10, width_per_block=10, mode="rgb"):
    bar = np.zeros((height, width_per_block * len(colors), 3), dtype=np.uint8)
    proportions = []

    for block_idx, color in enumerate(colors):
        proportions.append(color.proportion * 100)

        to_iter = color.hsl if mode == "hsl" else color.rgb

        for channel, x in enumerate(to_iter):
            bar[:, width_per_block * block_idx : width_per_block * (block_idx + 1), channel] = x

    return bar, proportions


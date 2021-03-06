import matplotlib
import matplotlib.cm
import numpy as np
import time


def time_delta_now(ts: float) -> str:
    """
    Convert a timestamp into a human readable timestring (%H:%M:%S).
    Args:
        ts (float): Timestamp
    Returns:
        Human readable timestring
    """
    a = ts
    b = time.time()  # current epoch time
    c = b - a        # seconds
    days = round(c // 86400)
    hours = round(c // 3600 % 24)
    minutes = round(c // 60 % 60)
    seconds = round(c % 60)
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"


def DepthNorm(depth, maxDepth=256.0): 
    return maxDepth / depth

class AverageMeter(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def colorize(value, vmin=1, vmax=256, cmap='plasma'):
    value = value.cpu().numpy()[0,:,:]

    # normalize
    vmin = value.min() if vmin is None else vmin
    vmax = value.max() if vmax is None else vmax
    if vmin!=vmax:
        value = (value - vmin) / (vmax - vmin) # vmin..vmax
    else:
        # Avoid 0-division
        value = value*0.
    # squeeze last dim if it exists
    #value = value.squeeze(axis=0)

    cmapper = matplotlib.cm.get_cmap(cmap)
    value = cmapper(value,bytes=True) # (nxmx4)

    img = value[:,:,:1]

    return img.transpose((2,0,1))
import os
def clear(dir=r"media/chunks"):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
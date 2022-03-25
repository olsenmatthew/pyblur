import numpy as np
from pyblur.BoxBlur import BoxBlurRandom
from pyblur.DefocusBlur import DefocusBlurRandom
from pyblur.GaussianBlur import GaussianBlurRandom
from pyblur.LinearMotionBlur import LinearMotionBlurRandom
from pyblur.PsfBlur import PsfBlurRandom

blurFunctions = {"0": BoxBlurRandom, "1": DefocusBlurRandom, "2": GaussianBlurRandom, "3": LinearMotionBlurRandom,
                 "4": PsfBlurRandom}


def RandomizedBlur(img):
    blurToApply = blurFunctions[str(np.random.randint(0, len(blurFunctions)))]
    return blurToApply(img)

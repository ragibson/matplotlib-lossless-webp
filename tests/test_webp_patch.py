import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def check_webp_matches_png(pil_kwargs=None):
    """Check whether .webp and .png exports have identical image data."""
    plt.figure()
    plt.plot([1, 2, 3], [4, 5, 6])

    if pil_kwargs:
        plt.savefig('test_compare.webp', pil_kwargs=pil_kwargs)
    else:
        plt.savefig('test_compare.webp')
    plt.savefig('test_compare.png')
    plt.close()

    is_perfect_match = np.array_equal(
        np.array(Image.open('test_compare.webp')),
        # we need to ignore the (unused) PNG alpha layer here
        np.array(Image.open('test_compare.png').convert("RGB"))
    )

    os.remove('test_compare.webp')
    os.remove('test_compare.png')
    return is_perfect_match


def test_default_webp_does_not_match_png():
    """
    Test that matplotlib's default .webp exports are lower quality than .png.

    If this fails, matplotlib's default has been changed to lossless, so this package has no effect.
    """
    assert not check_webp_matches_png()


def test_patch_webp_matches_png():
    """Test that .webp and .png exports have identical image data after our patch."""
    import matplotlib_lossless_webp  # noqa, we actually depend on this test running second
    assert check_webp_matches_png()


def test_patch_webp_explicitly_lossy_does_not_match_png():
    """Test that this package does not override explicitly choosing lossy .webp."""
    import matplotlib_lossless_webp  # noqa
    assert not check_webp_matches_png(pil_kwargs={'lossless': False})

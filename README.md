# matplotlib-lossless-webp

A tiny Python package that forces lossless compression in matplotlib when saving WebP images.

Otherwise, matplotlib's `.webp` exports are somewhat low quality unless you set specific PIL parameters.

In this way, you can use `.webp` as a smaller, drop-in replacement for `.png` while maintaining perfect quality.

## Installation

This project is on [PyPI](https://pypi.org/project/matplotlib-lossless-webp/) and can be installed with

    pip install matplotlib-lossless-webp

## Usage

Importing the package will force all future `savefig()` calls to be lossless when the filename ends with `.webp`.

```python
import matplotlib.pyplot as plt
import matplotlib_lossless_webp  # noqa

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('test.webp')  # automatically saves as lossless / high quality
```

## Why?

This is mostly for convenience, but **scientific figures _should_ normally be lossless, so this is a reasonable
default!**

Matplotlib is a bit strange for `.webp` files in that you can't just pass something like `savefig(..., quality=100)`
or `savefig(..., lossless=True)`.

The (allegedly) intended invocation is to pass the lossless parameter through to PIL with
`savefig(..., pil_kwargs={'lossless': True})`, but that is cumbersome to add repeatedly.

If this needs to be disabled on a rare, case-by-case basis, this package will not override explicit usage like
`savefig(..., pil_kwargs={'lossless': False})`.
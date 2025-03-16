# matplotlib-lossless-webp

A tiny Python package that forces lossless compression in matplotlib when saving WebP images.

Otherwise, matplotlib's `.webp` exports are somewhat low quality unless you add specific PIL parameters.

## Installation

This project is on PyPI and can be installed with

    pip install matplotlib-webp-lossless

## Usage

Importing the package will force all future `savefig()` calls to be lossless when the filename ends with `.webp`.

```python
import matplotlib.pyplot as plt
import matplotlib_lossless_webp

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('test.webp')  # automatically saves as lossless / high quality
```
from setuptools import setup

setup(
    name="matplotlib-lossless-webp",
    version="0.1.0",
    description="Tiny Python package that forces lossless compression in matplotlib when saving WebP images",
    keywords="matplotlib lossless webp",
    license="MIT",
    url="https://github.com/ragibson/matplotlib-lossless-webp",
    author="Ryan Gibson",
    author_email="ryan.alex.gibson@gmail.com",
    py_modules=["matplotlib_lossless_webp"],
    install_requires=["matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
)

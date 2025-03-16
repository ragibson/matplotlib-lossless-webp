from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="matplotlib-lossless-webp",
    version="0.1.1",
    description="Tiny Python package that forces lossless compression in matplotlib when saving WebP images",
    long_description=readme,
    long_description_content_type="text/markdown",
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

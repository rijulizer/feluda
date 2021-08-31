import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="feluda",
    version="0.1.1",
    author="Riju Mukherjee",
    author_email="riju11.mukherjee@gmail.com",
    description="feluda package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rijulizer/feluda",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'pyspark'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

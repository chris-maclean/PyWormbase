import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pywormbase",
    version="0.0.0",
    author="Christopher Anna",
    author_email="canna12@gmail.com",
    description="An interface to the Wormbase REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c-anna/PyWormbase",
    packages=['pywormbase'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent"
    )
)
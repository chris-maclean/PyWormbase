import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wormbase_parasite",
    version="0.3.0",
    author="Christopher Anna",
    author_email="canna12@gmail.com",
    description="An interface to the Wormbase REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c-anna/PyWormbase",
    packages=['wormbase_parasite', 'wormbase_parasite.endpoint_groups'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    )
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aoc",
    version="0.0.1",
    author="Jon Schwartz",
    author_email="jalexan@gmail.com",
    description="Solving advent of code!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonschwa/aoc2020",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name = "trender-ilandovprais",
	version = "0.0.1",
	decscription = "3d graphic library",
	author = "Ilan Prais",
    author_email = "ilandovprais@gmail.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/ilanprais/trender-3D-Graphics-Library",
    packages = find_packages(),
    package_dir = {"": "src"},
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',

)
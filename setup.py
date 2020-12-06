from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='cubescrambler',
	version='0.0.1',
	description="Generate scrambles for Rubik's cube and other twisty puzzles",
	py_modules=["scramble"],
	author="Raghav Vishwanath",
	author_email="raghav.vish@gmail.com",
	classifiers=["Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.0",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent"],
	long_description = long_description,
	long_description_content_type = "text/markdown",
)
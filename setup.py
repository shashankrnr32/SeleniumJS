import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "seleniumjs",
    version = "1.0.3",
    author = "Shashank Sharma",
    author_email = "shashankrnr32@gmail.com",
    description = ("Python Package to run Javascript code snippets easily on Selenium"),
    license = "MIT",
    keywords = "seleniumjs",
    url = "https://github.com/shashankrnr32/SeleniumJS",
    packages=[],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
)
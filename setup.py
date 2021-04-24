import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="choice-composer",
    version="1.0.3",
    description="It will help you to make choice filed.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ImamHossainRoni/choice-composer",
    author="Imam Hossain Roni",
    author_email="imamhossainroni95@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["choice_composer"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": ["choice_composer=choice_composer.__main__:main",]
    },
)
import pathlib
from setuptools import setup
from mdprint import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mdprint",
    version=__version__,
    description="Python tools to print strings to markdown file with styles. "
                "Also allows printing dicts and lists to table",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/mdprint",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["mdprint"],
    include_package_data=True,
    install_requires=[]
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gistclient",
    version="0.0.1",
    author="boolman",
    author_email="boolman@gmail.com",
    description="GistClient",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boolman/gistclient",
    packages=setuptools.find_packages(),
    scripts=['bin/gistclient'],
    install_requires=[
      'oauth2client',
      'requests',
      'httplib2',
      'fire',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

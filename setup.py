import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SMSONAR",
    version="0.0.1",
    author="Mina Gabriel",
    author_email="minamaged113@gmail.com",
    description="Sound Metrics SONARs files software development kit \
    (SDK) for reading and writing SONAR files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minamaged113/SMSONAR",
    license="GNU GPLv3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)

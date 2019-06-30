import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SMSONAR",
    version="0.0.2",
    author="Mina Gabriel",
    author_email="minamaged113@gmail.com",
    description="Sound Metrics SONARs files software development kit \
    (SDK) for reading and writing SONAR files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minamaged113/SMSONAR",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

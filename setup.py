import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hx711_gpiozero",
    version="0.0.3",
    author="CyrusN",
    author_email="cyrusncy@gmail.com",
    description="A HX711 Driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyrusn/hx711_gpiozero",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

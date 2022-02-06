import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="malclient",
    version="1.0",
    author="ModerNews",
    author_email="",
    description=
    "Modified and rewritten using modern models version of James Fotherby malclient",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fotherbyy/MAL-API-Client",
    install_requires=['requests', 'pydantic'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="3.6"
)

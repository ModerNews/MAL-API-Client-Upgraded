import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="malclient-upgraded",
    version="1.4a3",
    author="ModerNews",
    author_email="polski.gruzin.biz@gmail.com",
    description=
    "Modified and rewritten using modern models version of James Fotherby malclient",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ModerNews/MAL-API-Client-Upgraded",
    project_urls={"Documentation": "https://mal-api-client-upgraded.readthedocs.io"},
    install_requires=['requests', 'pydantic'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

import json
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('gryphon_requirements.txt') as fr:
    requirements = fr.read().strip().split('\n')

with open('metadata.json') as fr:
    metadata = json.load(fr)

setuptools.setup(
    name="gryphon-basic-utilities",  # Name of the repository
    version="0.0.6",
    author=metadata.get("author", ""),
    author_email=metadata.get("author_email", ""),
    description=metadata.get("description", ""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ow-gryphon/gryphon-basic-utilities",  # Repository URL or externally maintained page
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
)

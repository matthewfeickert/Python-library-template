from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as readme_md:
    long_description = readme_md.read()

extras_require = {
    "develop": [
        "check-manifest",
        "pytest~=5.2",
        "pytest-cov~=2.8",
        "pytest-console-scripts~=0.2",
        "bumpversion~=0.5",
        "pyflakes",
        "pre-commit",
        "black",
        "twine",
    ],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    name="libname",
    version="0.0.1",
    description="A template repository for a modern Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthewfeickert/python-library-template",
    author="Author Name",
    author_email="author.name@email.com",
    license="Apache",
    keywords="python template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=["click>=6.0"],
    python_requires=">=3.6",
    extras_require=extras_require,
    entry_points={"console_scripts": ["libname=libname.commandline:libname"]},
)

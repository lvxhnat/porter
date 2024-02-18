import re
import pathlib
from setuptools import setup, find_packages

here = pathlib.Path.absolute(pathlib.Path(__file__).resolve().parent)

# get package version
with open(pathlib.Path(here, f"src/__init__.py"), encoding="utf-8") as f:
    package_name = re.search(
        r"__package_name__\s*=\s*['\"]([^'\"]+)['\"]", f.read()
    ).group(1)
    
with open(pathlib.Path(here, f"src/{package_name}/__init__.py"), encoding="utf-8") as f:
    version = re.search(
        r"__version__\s*=\s*['\"](.*?)['\"]", f.read(), re.DOTALL
    ).group(1)

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dev_requirements = { "black", "pre-commit" }

base_requirements = {
    "pandas",
    "streamlit",
}

setup(
    name=package_name,
    version=version,
    author="Loh Yi Kuang",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*tests"]),
    install_requires=list(base_requirements),
    extra_requires={
        "dev": list(dev_requirements)
    },
    entry_points={
        "console_scripts": [
            f"{package_name} = {package_name}.launchers.cli:main"
        ],
    },
    python_requires=">=3.9",
)

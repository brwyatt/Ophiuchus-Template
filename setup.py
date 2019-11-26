from setuptools import find_packages
from setuptools import setup


setup(
    name="ophiuchus-website",
    version="0.1.0",
    author="",
    author_email="",
    description=(""),
    license="",
    keywords="",
    url="https://github.com/brwyatt/Ophiuchus-Template",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={},
    python_requires="~=3.6",
    include_package_data=False,
    entry_points={
        "website": [
            "placeholder = website:Placeholder"
        ],
    },
    install_requires=["ophiuchus"],
)

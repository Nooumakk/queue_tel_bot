import pathlib
from setuptools import setup, find_packages


BASE_DIR = pathlib.Path(__file__).parent.absolute()


def get_version():
    with open(BASE_DIR / "version") as file:
        return file.readline().strip()


def get_license():
    with open(BASE_DIR / "LICENSE") as file:
        return file.read().strip()


def get_desc():
    with open(BASE_DIR / "README.md") as file:
        return file.read().strip()


def get_packages():
    with open(BASE_DIR / "reqiurements.txt") as file:
        return [
            packages.strip()
            for packages in file
            if packages or not packages.startswith("#")
        ]


setup(
    name="tele_bot",
    version=get_version(),
    author="Naumowich Daniel",
    author_email="mr.jazva@mail.ru",
    url="doc.site.com",
    packages=find_packages(".", include=["tele_bot"]),
    # package_dir={"":""},
    include_package_data=True,
    license=get_license(),
    description="A bot tracking queues at the botder",
    long_description=get_desc(),
    long_description_content_type="text/markdown",
    install_requeres=get_packages(),
    python_requires=">3.9",
    classifiers=[
        "Development status :: 3 - Alpha"
        if "dev" in get_version()
        else "Development status :: 4 - Beta"
        if "rc" in get_version()
        else "Development status :: 5 - Production/Stable"
    ],
    entry_points={
        "console_scripts": [
            "bot = tele_bot:start_bot",
        ]
    },
)

from setuptools import find_packages, setup

setup(
    name="demo-app",
    author="Nicholas Willhite,",
    version="2023.03.08",
    packages=find_packages(),
    include_package_data=True,
    description="A demo flask application",
    install_requires=[
        "flask",
        "pyjwt",
        "gunicorn",
        "ujson",
        "cryptography",
        "psycopg2",
    ],
)

from setuptools import setup, find_packages

__version__ = None
with open('socketlabs/injectionapi/version.py') as f:
    exec(f.read())

with open("README.md", "r", encoding='utf-8') as ld:
    long_description = ld.read()

setup(
    name="socketlabs_injectionapi",
    version=__version__,
    author="David Schrenker, Matt Reibach, Ryan Lydzinski",
    author_email="support@socketlabs.com",
    description="SocketLabs Email Delivery Python client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests', '*test_*.py', ]),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/socketlabs/socketlabs-python",
    license='MIT',
    project_urls={
        'Organization': 'https://github.com/socketlabs',
        'Bug Reports': 'https://github.com/socketlabs/socketlabs-python/issues',
        'Source': 'https://github.com/socketlabs/socketlabs-python',
        'License': 'https://github.com/socketlabs/socketlabs-python/blob/master/LICENSE',
    }
)

from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'match_tool_by_nikhilgilbertv2',
    version = '0.0.1',
    author = 'Nikhil Gilbert',
    author_email = 'gilbert.nikhil@gmail.com',
    license = 'licence',
    description = 'cli tool to calculate match scoring',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = '',
    py_modules = ['match_tool', 'match_calculator'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        match=match_tool:cli
    '''
)
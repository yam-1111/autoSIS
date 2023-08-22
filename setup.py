from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='autoSIS',                # Set your library name
    version='0.1.0',               # Set your library version
    packages=['autoSIS'],
    install_requires=requirements,  # Use the list from requirements.txt
    author='Anthony John',
    # author_email='your@email.com',
    description='simple python api for viewing grades',
    # url='https://github.com/your-username/your-repo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 6 - Mature',
        'Development Status :: 7 - Inactive',
        'Development Status :: 8 - Planning',
        'Development Status :: 9 - Pre-Alpha',
        'Development Status :: 10 - Unstable',
        'Development Status :: 11 - Canary',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

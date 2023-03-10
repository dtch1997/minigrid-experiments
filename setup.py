import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)

base_package = 'minigrid_experiments'
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, 'minigrid_experiments', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))

with open('README.rst', 'r') as f:
    readme = f.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements/main.txt')
dev_requirements = parse_requirements('requirements/dev.txt')

if __name__ == '__main__':
    setup(
        name='minigrid_experiments',
        description='Experiments in Minigrid',
        long_description='\n\n'.join([readme]),
        license='MIT license',
        url='https://github.com/dtch1997/minigrid_experiments',
        version=version,
        author='Daniel C.H. Tan',
        author_email='dtch1997@users.noreply.github.com',
        maintainer='Daniel C.H. Tan',
        maintainer_email='dtch1997@users.noreply.github.com',
        install_requires=requirements,
        extras_require={
            'develop': dev_requirements,
        },
        keywords=['minigrid_experiments'],
        packages=find_packages(),
        zip_safe=False,
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8']
    )

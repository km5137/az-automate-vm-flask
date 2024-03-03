from setuptools import find_packages, setup

setup(
    name='BlogCapstone',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask', 'requests', 'azure-identity'
    ],
    entry_points={
        'console_scripts': [
            'blogcapstone=app.run:main',
        ],
    },
)

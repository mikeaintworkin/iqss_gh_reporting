from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='iqss_gh_reporting',
    version='0.1',
    description='collects raw data from github and transforms it into a format that can be used for reporting',
    author='Mike Reekie',
    author_email='mike@reekie.us',
    url='https://github.com/thisaintwork/iqss_gh_reporting/tree/master/workflows',
    license='MIT',
    packages=find_packages(exclude=['deprecated', 'tests']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'PyGithub',
        'gql',
        'pathvalidate',
        'pandas',
        'pyyaml'
    ],
    scripts=['workflows/create_iq_snapshot_init',
             'workflows/create_iq_snapshot',
             'workflows/process_labels'
             ],
)

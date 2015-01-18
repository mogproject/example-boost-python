from setuptools import setup, find_packages, Extension


setup(
    name='example-boost-python',
    version='0.0.1',
    description='Example for Boost.Python',
    author='your-name',
    author_email='your-name@example.com',
    url='https://example.com/your-repo',
    install_requires=[],
    tests_require=[],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    test_suite='tests',
    entry_points='',
    ext_modules=[
        Extension(
            name='chello',
            sources=['src/chello/chello.cpp'],
            include_dirs=['/usr/local/include/boost'],
            library_dirs=['/usr/lib', '/usr/local/lib'],
            libraries=['boost_python3'],
            extra_compile_args=['-std=c++11', '-Wall'],
            extra_link_args=[],
        )
    ],
)

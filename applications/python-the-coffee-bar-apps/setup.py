from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='the-coffee-bar',
    version='0.2.0',
    description='The Coffee Bar - OpenTelemetry instrumented demo application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sanyaku/the-coffee-bar',
    author='Mateusz "mat" Rumian',
    author_email='mrumian@sumologic.com',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='the-coffee-bar opentelemetry auto instrumentation setuptools development',

    packages=find_packages(),
    python_requires='>=3.8, <4',

    install_requires=['APScheduler==3.8.1',
                      'cron-descriptor==1.2.24',
                      'Flask==2.0.2',
                      'flask-cors==3.0.10',
                      'opentelemetry-distro==0.26b1',
                      'opentelemetry-exporter-jaeger==1.7.1',
                      'opentelemetry-exporter-otlp-proto-http==1.7.1',
                      'opentelemetry-exporter-zipkin==1.7.1',
                      'opentelemetry-instrumentation==0.26b1',
                      'opentelemetry-sdk==1.7.1',
                      'opentelemetry-propagator-aws-xray==1.0.1',
                      'opentelemetry-propagator-b3==1.7.1',
                      'paste==3.5.0',
                      'psycopg2==2.9.3',
                      'pyjson==1.3.0',
                      'requests==2.26.0',
                      'statsd==3.3.0',
                      'tcconfig==0.27.1',
                      'waitress==2.0.0',
                      ],
    data_files=[],
    entry_points={
        'console_scripts': [
            'the-coffee-bar=src.bin.the_coffee_bar:main',
            'the-coffee-machine=src.bin.the_coffee_machine:main',
            'the-cashdesk=src.bin.the_cashdesk:main',
            'the-coffee-lover=src.bin.the_coffee_lover:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Sumologic/the-coffee-bar/issues',
        'Source': 'https://github.com/Sumologic/the-coffee-bar/applications/python-the-coffee-bar-apps',
    },
)

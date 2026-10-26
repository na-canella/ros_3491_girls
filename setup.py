from setuptools import setup

package_name = 'super_na_canella_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='na-canella',
    maintainer_email='na-canella@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'time_printer = super_na_canella_study_pkg.time_printer:main',
            'even_pub = super_na_canella_study_pkg.even_number_publisher:main',
            'overflow_listener = super_na_canella_study_pkg.overflow_listener:main',  # <-- НОВАЯ СТРОКА
        ],
    },
)

from setuptools import setup

package_name = 'reachy_controllers'

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
    maintainer='Pollen-Robotics',
    maintainer_email='contact@pollen-robotics.com',
    description='ROS2 Foxy controllers for Reachy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_controller = reachy_controllers.joint_controller:main'
        ],
    },
)

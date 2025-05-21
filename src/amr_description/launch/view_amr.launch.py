import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    amr_share_dir = get_package_share_directory('amr_description')

    # URDF 파일 경로
    urdf_file = os.path.join(amr_share_dir, 'urdf', 'amr_robot.urdf')
    rviz_config_file = os.path.join(amr_share_dir, 'rviz', 'amr_description.rviz')

    # URDF 파일 내용 읽기
    with open(urdf_file, 'r') as infp:
        robot_description_content = infp.read()

    model_arg = DeclareLaunchArgument(
        'model',
        default_value='',
        description='Robot model (optional)'
    )

    return LaunchDescription([
        model_arg,
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen',
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file]
        ),
    ])

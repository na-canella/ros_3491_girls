from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description='Режим работы: fast или slow'
    )
    
    mode = LaunchConfiguration('mode')

    freq = PythonExpression(["20.0 if '", mode, "' == 'fast' else 5.0"])
    threshold = PythonExpression(["50 if '", mode, "' == 'fast' else 150"])
    topic = PythonExpression(["'/even_numbers_fast' if '", mode, "' == 'fast' else '/even_numbers_slow'"])

    return LaunchDescription([
        mode_arg,

        Node(
            package='super_na_canella_study_pkg',
            executable='even_pub',
            name='even_pub',
            parameters=[{
                'publish_frequency': freq,
                'overflow_threshold': threshold,
                'topic_name': topic,
            }],
            output='screen',
        ),

        Node(
            package='super_na_canella_study_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])

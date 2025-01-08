import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='mem_usage_publisher',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='test_sub',
        output='screen'
        )

    return launch.LaunchDescription([talker, listener])   

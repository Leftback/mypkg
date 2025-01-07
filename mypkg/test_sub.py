# SPDX-FileCopyrightText: 2024 Leftback
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MemUsageSubscriber(Node):
    def __init__(self, node_name='mem_usage_subscriber') -> None:
        super().__init__(node_name)
        self.declare_parameter('node_name', node_name)
        self.subscription = self.create_subscription(
            String,
            'mem_usage',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg: String) -> None:
        self.get_logger().info(f'{msg.data}')

def main(args=None) -> None:
    rclpy.init(args=args)
    node = MemUsageSubscriber()
    node_name = node.get_parameter('node_name').get_parameter_value().string_value
    node.get_logger().info(f'{node_name} start!')

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.exceptions.ExternalShutdownException):
        pass
    finally:
        rclpy.shutdown()
        node.destroy_node()

if __name__ == '__main__':
    main()


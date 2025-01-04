# SPDX-FileCopyrightText: 2024 Leftback
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MemUsageSubscriber(Node):

    def __init__(self) -> None:
        super().__init__('mem_usage_subscriber')
        self.subscription = self.create_subscription(
            String,
            'mem_usage',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: String) -> None:
        self.get_logger().info(f'受信メッセージ: {msg.data}')

def main(args=None) -> None:
    rclpy.init(args=args)
    node = MemUsageSubscriber()
    node.get_logger().info('mem_usage_subscriber start!')

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        rclpy.shutdown()
        node.destroy_node()

if __name__ == '__main__':
    main()

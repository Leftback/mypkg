# SPDX-FileCopyrightText: 2024 Leftback
# SPDX-License-Identifier: BSD-3-Clause

import os
import sys

# third_party のパスを設定
current_dir = os.path.dirname(os.path.abspath(__file__))
third_party_dir = os.path.join(current_dir, '..', 'third_party', 'psutil')
sys.path.insert(0, third_party_dir)

import rclpy
from rclpy.node import Node
import psutil
from std_msgs.msg import String

class MemUsagePublisher(Node):
    def __init__(self) -> None:
        super().__init__('mem_usage_publisher')
        self.publisher = self.create_publisher(String, 'mem_usage', 10)
        self.timer = self.create_timer(1.0, self.publish_mem_usage)

    def publish_mem_usage(self) -> None:
        used_mem = psutil.virtual_memory().used / (1024 ** 2)
        msg = String(data=f'使用メモリ: {used_mem:.2f} MB')
        self.publisher.publish(msg)
        self.get_logger().info(f'Published memory usage: {used_mem:.2f} MB')

def main(args=None) -> None:
    rclpy.init(args=args)
    node = MemUsagePublisher()

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.exceptions.ROSInterruptException):
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


# SPDX-FileCopyrightText: 2024 Leftback
# SPDX-License-Identifier: BSD-3-Clause

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

def main(args=None) -> None:
    rclpy.init(args=args)
    node = MemUsagePublisher()

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.exceptions.ROSInterruptException):
        pass
    finally:
        rclpy.shutdown()
        node.destroy_node()

if __name__ == '__main__':
    main()


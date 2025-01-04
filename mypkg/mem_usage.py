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
        self.get_logger().info(f'{msg.data}')

def main(args=None) -> None:
    rclpy.init(args=args)
    node = MemUsagePublisher()
    node.get_logger().info('mem_usage_publisher start!')

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        rclpy.shutdown()
        node.destroy_node()

if __name__ == '__main__':
    main()
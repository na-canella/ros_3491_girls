#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        # Подписываемся на топик /overflow
        self.subscription = self.create_subscription(
            Int32, 'overflow', self.callback, 10)
        self.get_logger().info("Слушатель переполнения запущен!")

    def callback(self, msg):
        # Используем .warn, чтобы сообщение было желтым (предупреждение)
        self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Получено значение: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        # Создаем два публикатора: для четных чисел и для переполнения
        self.publisher_ = self.create_publisher(Int32, 'even_numbers', 10)
        self.overflow_pub = self.create_publisher(Int32, 'overflow', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.num = 0

    def timer_callback(self):
        if self.num >= 100:
            # Если дошли до 100 - отправляем в топик overflow
            overflow_msg = Int32()
            overflow_msg.data = 100
            self.overflow_pub.publish(overflow_msg)
            self.get_logger().info('--- ПЕРЕПОЛНЕНИЕ! СБРОС НА 0 ---')
            self.num = 0
        else:
            # Иначе публикуем четное число
            msg = Int32()
            msg.data = self.num
            self.publisher_.publish(msg)
            self.get_logger().info(f'Публикую: {msg.data}')
            self.num += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

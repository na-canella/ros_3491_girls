#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # 1. Объявляем параметры (наши "ручки настройки")
        self.declare_parameter('publish_frequency', 10.0)
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_name', '/even_numbers')

        # 2. Читаем их значения
        freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        topic = self.get_parameter('topic_name').value

        self.publisher_ = self.create_publisher(Int32, topic, 10)
        self.overflow_pub = self.create_publisher(Int32, '/overflow', 10)
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)
        self.num = 0

    def timer_callback(self):
        if self.num >= self.threshold:
            overflow_msg = Int32()
            overflow_msg.data = self.num
            self.overflow_pub.publish(overflow_msg)
            self.get_logger().info(f'--- ПЕРЕПОЛНЕНИЕ! СБРОС НА 0 (Порог: {self.threshold}) ---')
            self.num = 0
        else:
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

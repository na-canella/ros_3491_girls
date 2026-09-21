#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from datetime import datetime

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        self.timer = self.create_timer(5.0, self.timer_callback)

    def timer_callback(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.get_logger().info(f"Текущее время: {now}")

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

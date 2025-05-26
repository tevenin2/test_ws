import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.pub = self.create_publisher(Twist, '/my_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.1
        msg.angular.z = 0.1
        self.pub.publish(msg)
        self.get_logger().info(
            f'Published → linear.x: {msg.linear.x}, angular.z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

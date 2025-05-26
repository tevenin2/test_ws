import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.sub = self.create_subscription(
            Twist, '/my_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received ← linear.x: {msg.linear.x}, angular.z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

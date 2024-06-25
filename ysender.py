import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import String

class ButtonPub(Node):
    def __init__(self):
        super().__init__('button_publisher')
        self.publisher = self.create_publisher(String,"topic",10)
        self.button = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        msg=String()
        while True:
            if GPIO.input(self.button)==0:
                msg.data = "on"
                self.publisher.publish(msg)
                self.get_logger().info('Publishing : "%s"' %msg.data)
            elif GPIO.input(self.button)==1:
                msg.data = "on"
                self.publisher.publish(msg)
                self.get_logger().info('Publishing : "%s"' %msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = ButtonPub()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

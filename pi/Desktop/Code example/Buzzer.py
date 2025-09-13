import time
import ros_robot_controller_sdk as rrc


board = rrc.Board()
board.set_buzzer(1900, 0.1, 0.9, 1) # 以1900Hz的频率，持续响0.1秒，关闭0.9秒，重复1次
time.sleep(2)
board.set_buzzer(1000, 0.5, 0.5, 0) # 以1000Hz的频率，持续响0.5秒，关闭0.5秒，一直重复
time.sleep(3)
board.set_buzzer(1000, 0.0, 0.0, 1) # 关闭


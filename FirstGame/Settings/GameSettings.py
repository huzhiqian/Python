

class GameSettings(object):
    # 构造函数
    def __init__(self):
        # 初始化设置

        # 设置屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.2  # 移动速度因子

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_maxcount = 20

        # alien设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # -1表示反方向

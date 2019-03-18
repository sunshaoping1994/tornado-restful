# 导入第三方包
from tornado.web import Application
from tornado.options import options, define, parse_command_line
from tornado.ioloop import IOLoop

# 导入自定义包
from handlers import user as user_handlers

# 配置项目默认启动端口
define('port', default=8008, help='项目启动默认端口')


# 定义启动函数
def run():
    # 识别命令行变量操作
    parse_command_line()
    # 定义app
    app = Application(
        [
            # 定义路由
            (r'/api/users', user_handlers.UserListHandler),
            (r'/api/users/(\d+)', user_handlers.UserHandler),
        ],
        # 开启调试模式
        debug=True,
    )
    # 启动项目监听端口
    app.listen(options.port)
    # 启动轮询事件
    IOLoop.current().start()


# 主函数入口
if __name__ == "__main__":
    run()
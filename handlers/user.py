from tornado.web import RequestHandler
from models.user import UserModel
from tornado.escape import json_encode


class UserListHandler(RequestHandler):
    # 获取所有用户信息
    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    # 创建新用户信息
    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        UserModel.create(name, age)
        result = {'status': True, 'msg': 'success'}
        self.write(json_encode(result))


class UserHandler(RequestHandler):
    # 获取单个用户信息
    def get(self, user_id):
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)
        self.write(json_encode(user))

    # 更新用户信息
    def put(self, user_id):
        age = self.get_argument('age')
        UserModel.update(int(user_id), age)
        result = {'status': True, 'msg': 'success'}
        self.write(json_encode(result))

    # 删除个人信息
    def delete(self, user_id):
        try:
            UserModel.delete(int(user_id))
            result = {'status': True, 'msg': 'success'}
            self.write(json_encode(result))
        except KeyError:
            return self.set_status(404)

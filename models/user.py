# 定义用户模型
class UserModel(object):

    # 用户信息字典
    users = {
        1: {'name': 'zan', 'age': 10},
        2: {'name': 'wang', 'age': 12},
        3: {'name': 'li', 'age': 13},
        4: {'name': 'zhu', 'age': 15},
    }

    # 获取指定id用户
    @classmethod
    def get(cls, user_id):
        return cls.users[user_id]

    # 获取所有用户的值
    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    # 创建新用户
    @classmethod
    def create(cls, name, age):
        user_dict = {'name': name, 'age': age}
        max_id = max(cls.users.keys()) + 1
        cls.users[max_id] = user_dict

    # 更新用户信息
    @classmethod
    def update(cls, user_id, age):
        cls.users[user_id]['age'] = age

    # 删除指定用户
    @classmethod
    def delete(cls, user_id):
        if user_id in cls.users:
            return cls.users.pop(user_id)
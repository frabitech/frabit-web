# -*- coding:utf-8 -*-
from web import create_app, db


application = create_app('default')

# 之前遇到的问题，无法初始化一个login manager装饰其，一直报错，现在把它移动到这里，不报错，程序可以正常运行 No user_loader has been installed for this
lm.init_app(application)

@lm.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# 这里可以使用工具连接数据库了，但是有个问题，就是不能同步表到数据库里面，需要手动处理。
# db.create_all(app=app)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=9180, debug=True, threaded=True)

from app import create_app, db
from app.models import Users
from flask_script import Manager, Server


app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = Users)
if __name__ == '__main__':
    app.run()





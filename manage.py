from app import create_app, db
from app.models import Users, Pitches, Role, Comment, Upvote, Downvote
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = Users, Pitches = Pitches, Role = Role, Comment = Comment, Upvote = Upvote, Downvote = Downvote)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.run()




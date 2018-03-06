from flask_test import app


if __name__ == '__main__':
    HOST = app.config.get('SERVER_HOST', 'localhost')
    PORT = app.config.get('SERVER_PORT', 5555)
    app.run(HOST, PORT)

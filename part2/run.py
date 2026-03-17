
from app import create_app

#entry point and starts server

app = create_app('development')
if __name__ == '__main__':
    app.run(debug=True)

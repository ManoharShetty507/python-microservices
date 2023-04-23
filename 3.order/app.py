from flask import Flask
from routes import order_blueprint
from models import db, init_app
from flask_migrate import Migrate
app = Flask(__name__)

app.config  ['SECRET_KEY'] = 'vZK7siKrV8BL46KsyAIPoQ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config [ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users\Manohar Shetty/Desktop/Store-Website/3.order/database/order.db'

app.register_blueprint(order_blueprint)
init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
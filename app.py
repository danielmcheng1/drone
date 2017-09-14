from flask import Flask
import routes 
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'

#init_api_routes(app)
routes.init_website_routes(app)
#init_error_handlers(app)


if __name__ == "__main__":
    app.run(debug=True)

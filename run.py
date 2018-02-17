import app
import config

app = app.create_app(config.DevelopmentConfig)
#app = app.create_app(config.TestingConfig)

from bot.server import app


if __name__ == "__main__":
    app.debug = False
    app.run()

from app.main import main as app
if __name__ == '__main__':
    if app.config["DEBUG"] == True:
        app.run(host="localhost", ssl_context=('./cert.pem', './key.pem'))
    else:
        app.run()

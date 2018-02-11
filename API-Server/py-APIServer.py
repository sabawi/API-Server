from app import app

if __name__ == "__main__":
    import socket

    print(socket.gethostbyname_ex(socket.gethostname())[0])
    app.run(port=8080)

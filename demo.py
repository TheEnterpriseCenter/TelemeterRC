from TelemeterRC import TelemeterRcDaemon

if __name__ == "__main__":
    app = TelemeterRcDaemon("b827ebd50755", "00e060000060")
    app.push()

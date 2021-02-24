import base64


def decodeSound(soundfile, fileName):
    soundData = base64.b64decode(soundfile)
    with open(fileName, 'wb') as f:
        f.write(soundData)
        f.close()

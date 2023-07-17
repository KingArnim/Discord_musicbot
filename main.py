from Music.BkdInitializer import BkdInitializer
from Config.Folder import Folder

if __name__ == '__main__':
    folder = Folder()
    initializer = BkdInitializer(willListen=True)
    BkdBot = initializer.getBot()
    BkdBot.startBot()

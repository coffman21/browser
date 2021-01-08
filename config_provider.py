from configparser import ConfigParser

class ConfigProvider:
    parser = ConfigParser()

    @staticmethod    
    def read():
        ConfigProvider.parser.read('config.ini')
    
    @staticmethod
    def getLibraryPath():
        return ConfigProvider.parser['DEFAULT']['LibraryPath']

    @staticmethod
    def getDbPath():
        return ConfigProvider.parser['DEFAULT']['DatabasePath']

ConfigProvider.read()

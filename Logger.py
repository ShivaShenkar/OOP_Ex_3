class Logger:
    _instance = None  # Class attribute to store the singleton instance

    def get_instance(self, filename):
        if self._instance is None:
            self._instance = self.__new__(self)
            self._instance.filename = filename
            self._instance.file = open(filename, 'w')
        return self._instance

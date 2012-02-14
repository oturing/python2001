# PopReader - class to read POP mail

import poplib, StringIO, mimetools, string

class PopReader:
    """This class is a front-end to poplib;
    it reads mail from a POP account, with settings stored in the
    instance, and returns a list of mimetools.Message instances
    """
    def __init__(self, host=None, user=None, password=None):
        if host: self.setHost(host)
        if user: self.setUser(user)
        if password: self.setPassword(password)
    
    def setHost(self, host):
        self.host = host
    
    def setUser(self, user):
        self.user = user
    
    def setPassword(self, password):
        self.password = password
    
    def __getBox(self):
        M = poplib.POP3(self.host)
        M.user(self.user)
        M.pass_(self.password)
        return M
    
    def __len__(self):
        "How many messages we have waiting"
        M = self.__getBox()
        try:
            l = len(M.list()[1])
        finally:
            M.quit()
        return l
    
    def getMail(self, delete=0):
        "Read the mail (return a list of mimetools.Message instances)"
        M = self.__getBox()
        try:
            l = len(M.list()[1])
            messages = []
            for i in range(1, l+1):
                messages.append(mimetools.Message(
                    StringIO.StringIO(string.join(M.retr(i)[1], '\n'))))
                if delete:
                    M.dele(i)
        finally:
            M.quit()
        return messages

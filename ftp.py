from ftplib import FTP
from StringIO import StringIO

HOST = 'ftp.br.yahoo.com'
PORT = '21'
USER = 'magnet'
PASSWORD = 'mg!47z@'


def ftp(nome_arq, dados):
    arq = StringIO(dados)
    ftp = FTP()
    ftp.connect(HOST, PORT)
    ftp.login(USER, PASSWORD)
    command = 'STOR ' + nome_arq
    ftp.storlines(command, arq)
    ftp.close()
    
def ftpdir():
    linhas = []
    ftp = FTP()
    ftp.connect(HOST, PORT)
    ftp.login(USER, PASSWORD)
    command = " LIST"
    ftp.retrlines(command, listar)
    ftp.close()
    return linhas
    
def ftp_teste():
    str = '''
    the time has come the walrus said
    to speak of many things
    of ships and sails and sealing wax
    of cabbages and kings'''
    str.strip()
    ftp('lixo123.txt', str)    

def ftpdir_teste():
    linhas = ftpdir()
    
def listar(linha):
    print '>' + linha
    
    #print linhas    
    
if __name__=='__main__':
    ftpdir_teste()
    
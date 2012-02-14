#!/usr/local/bin/python

import cgi, mSQL, os, string, sys;

class Domain:
    def __init__(self, host, db):
        self.server = host;
        self.database = db;
        
    def doGet(self):
        self.printHeader();
        form = cgi.FieldStorage();
        self.printTitle();
        print "<BODY>";
        print "<H1>Enter Host Information</H1>";
        print "<P>";
        print "Please enter the desired host name as well as the host type.";
        print "</P>";
        print "<FORM ACTION=/cgi/Domain.py METHOD=POST>";
        print "<INPUT TYPE=TEXT NAME=name SIZE=20>";
        print "<SELECT NAME=type SIZE=1>";
        print "<OPTION>Host Type";
        print "<OPTION>Workstation";
        print "<OPTION>Server";
        print "<OPTION>Virtual Host";
        print "</SELECT>";
        print "<INPUT TYPE=submit>";
        print "</FORM>";
        self.printFooter();
        
    def doPost(self):
        try:
            self.printHeader();
            form = cgi.FieldStorage();
            self.printTitle();
            print "<BODY>";
            if not form.has_key("type"):
                self.printError("You must choose a host type.");
                return;
            else:
                type = string.strip(form["type"].value);
                if type == 'Host Type':
                    self.printError("You must choose a host type.");
                    return;
            if not form.has_key("name"):
                self.printError("You must choose a name for the host.");
                return;
            else:
                host = string.strip(form["name"].value);
                if host == '':
                     self.printError("You must choose a name for the host.");
                     return;
            ip = self.selectIP(type, host);
            if ip == '':
                self.printError("No more IP's are available for this type.");
                return;
            print "<H1>IP for " + host + "</H1>";
            print "<P>";
            print "The IP assigned to " + host + " is: <EM>" + ip + "</EM>";
            print "</P>";
            self.printFooter();
        except:
            print "Error!";
            print sys.exc_type, sys.exc_value;
        
    def printError(self, msg):
        print "<H1>Error</H1>";
        print "<P>";
        print msg;
        print "</P>";
        self.printFooter();

    def printFooter(self):
        print "</BODY>";
        print "</HTML>";
        
    def printHeader(self):
        print "Content-type: text/html";
        print;

    def printTitle(self):
        print "<HTML>";
        print "<HEAD>";
        print "<TITLE>IP Selector</TITLE>";
        print "</HEAD>";

    def selectIP(self, type, host):
        sql = "SELECT ip FROM hosts WHERE type = '" + type  + "' and name = ''";
        db = mSQL.connect(self.server);
        db.selectdb(self.database);
        result = db.query(sql);
        if len(result) < 1:
            db.close();
            return "";
        else:
            ip = result[0][0];
            sql = "UPDATE hosts SET name = '" + host +  "' WHERE ip = '" + ip + "'";
            db.query(sql);
            db.close();
            return ip;
        
if __name__ == '__main__':
    domain = Domain('athens.imaginary.com', 'db_test');
    if not os.environ.has_key('REQUEST_METHOD'):
        domain.doGet();
    elif os.environ['REQUEST_METHOD'] == 'GET':
        domain.doGet();
    else:
        domain.doPost();

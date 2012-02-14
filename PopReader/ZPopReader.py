# ZPopReader - Zope wrapper for PopReader

from PopReader import PopReader
from Shared.DC.Scripts.Script import Script, BindingsUI
from Shared.DC.Scripts.Signature import FuncCode
from OFS.SimpleItem import SimpleItem
from AccessControl import getSecurityManager, ClassSecurityInfo
from OFS.History import Historical, html_diff
from OFS.Cache import Cacheable
from OFS.Traversable import Traversable
from Globals import DTMLFile

class ZPopReader(Script, PopReader, Historical, Cacheable, Traversable):
    "Read mail from a POP server"
    
    meta_type = 'Z Pop Reader'

    func_defaults = None
    func_code = FuncCode((), 0)

    manage_options = (
        {'label':'Edit', 'action':'zpopr_editForm'},
        {'label':'Test', 'action':'ZScriptHTML_tryForm'},
        ) + Historical.manage_options + SimpleItem.manage_options + \
        Cacheable.manage_options
    
    def __init__(self, id, host=None, user=None, password=None):
        self.id = id
        if host: self.setHost(host)
        if user: self.setUser(user)
        if password: self.setPassword(password)

    security = ClassSecurityInfo()

    security.declareObjectProtected('Read POP Mail')
    security.declareProtected('Read POP Mail', '__call__',
        'zpopr_editForm', 'zpopr_editAction')

    security.declareProtected('View management screens',
      'ZScriptHTML_tryForm', 'PrincipiaSearchSource',
      'document_src')

    def zpopr_editAction(self, REQUEST):
        "Change attributes"
        self.setUser(REQUEST['user'])
        self.setHost(REQUEST['host'])
        self.setUser(REQUEST['user'])
        self.setPassword(REQUEST['password'])
        return self.zpopr_editForm(manage_tabs_message='Saved changes.')
    
    zpopr_editForm = DTMLFile('Edit', globals())
    
    def ZScriptHTML_tryParams(self):
        "Parameters to run with."
        return ['delete']
    
    def _exec(self, bound_names, args, kw):
        "Get mail"
        if kw.has_key('delete'):
            delete = kw['delete']
        elif len(args) > 0:
            delete = args[0]
        else:
            delete = 0
        return self.getMail(delete)

manage_addZPopReaderForm = DTMLFile('Add', globals())

def manage_addZPopReader(container, id, REQUEST=None):
    "Create a POP reader in 'container'"
    id = str(id)
    container._setObject(id, ZPopReader(id,
        REQUEST['host'], REQUEST['user'], REQUEST['password']))
    if hasattr(REQUEST, 'RESPONSE'):
        try: u = container.DestinationURL()
        except: u = REQUEST['URL1']
        REQUEST.RESPONSE.redirect(u+'/manage_main')

def initialize(context):
    context.registerClass(
        ZPopReader,
        permission='Add Pop Readers',
        constructors=(manage_addZPopReaderForm,
                      manage_addZPopReader)
        )

#!/usr/bin/python

# YTombola.py: classe base para ZClasses baseadas na classe Tombola

__doc__ = """YTombola product module."""

__version__ = '0.1'

from Tombola import Tombola

from Globals import HTMLFile		# fakes a method from a DTML file
from Globals import MessageDialog	# provides Zope message dialogs
from Globals import Persistent		# makes an object stick in the ZODB

import OFS.SimpleItem
import Acquisition
import AccessControl.Role

manage_addForm = HTMLFile('tombolaAdd', globals())

def manage_add(self, id, title, bolas, REQUEST=None):
	"""Add a Tombola to a folder."""
	self._setObject(id, YTombola(id, title, bolas))
	if REQUEST is not None:
		return self.manage_main(self, REQUEST)

class YTombola(
	OFS.SimpleItem.Item,			# A simple Principia object. Not Folderish.
	Persistent,						# Make us persistent. Yaah!
	Acquisition.Implicit,			# Uh, whatever.
	AccessControl.Role.RoleManager	# Security manager.
	):
	"""Tombola class."""

	meta_type = 'YTombola'

	def __init__(self, id, title, bolas):
		"""initialise a new instance of Tombola"""
		self.tombola = Tombola(bolas)
		#apply(Tombola.__init__, (self, bolas))
		self.id = id
		self.title = title
		#self.tombola.__allow_access_to_unprotected_subobjects__ = 1
		#self.sortear = self.tombola.sortear

	def sortear(self):
		'''sorteia o próximo item'''
		return self.tombola.sortear()

	def __getattr__(self, attr):
		if hasattr(self.tombola, attr):
			return getattr(self.tombola, attr)
		else:
			raise AttributeError, "procuramos mas não achamos '%s'" % attr

	manage_options = (
		{'label': 'Edit',		'action': 'manage_main'		},
		{'label': 'View',		'action': ''				}, # invocar a própria instância (call->index_html)
		{'label': 'Security',	'action': 'manage_access'	},
		{'label': 'Sortear',	'action': 'sortear'			},
	)

	__ac_permissions__=(
		('View management screens',	('manage_tabs','manage_main')	),
		('Change permissions',		('manage_access',)				),
		('Change Tômbola',			('manage_edit',)				),
		('View Tômbola',			('',)							),
		('Use Tômbola',				('sortear','misturar')			),
	)

	index_html = HTMLFile('index', globals())			# View Interface

	manage_main = HTMLFile('tombolaEdit', globals())	# Management Interface

	def manage_edit(self, title, bolas, REQUEST=None):
		"""proc"""
		self.title = title
		self.bolas = bolas
		if REQUEST is not None:
			return MessageDialog(
				title = 'Edited',
				message = "Properties for %s changed." % self.id,
				action = './manage_main',
			)



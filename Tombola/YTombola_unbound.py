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

from whrandom import random

manage_addForm = HTMLFile('tombolaAdd', globals())

def manage_add(self, id, title, bolas, REQUEST=None):
	"""Add a Tombola to a folder."""
	self._setObject(id, YTombola(id, title, bolas))
	if REQUEST is not None:
		return self.manage_main(self, REQUEST)

class YTombola(
	Tombola,						# A classe que interessa!
	OFS.SimpleItem.Item,			# A simple Principia object. Not Folderish.
	Persistent,						# Make us persistent. Yaah!
	Acquisition.Implicit,			# Uh, whatever.
	AccessControl.Role.RoleManager	# Security manager.
	):
	"""Tombola class."""

	meta_type = 'YTombola'

	def __init__(self, id, title, bolas):
		"""initialise a new instance of Tombola"""
		Tombola.__init__(self, bolas)
		#apply(Tombola.__init__, (self, bolas))
		self.id = id
		self.title = title

	manage_options = (
		{'label': 'Edit',		'action': 'manage_main'		},
		{'label': 'View',		'action': ''				}, # defaults to index_html
		{'label': 'Security',	'action': 'manage_access'	},
		{'label': 'Sortear',	'action': 'sortear'			},
	)

	__ac_permissions__=(
		('View management screens',	('manage_tabs','manage_main')	),
		('Change permissions',		('manage_access',)				),
		('Change T�mbola',			('manage_edit',)				),
		('View T�mbola',			('',)							),
		('Use T�mbola',				('sortear',)					),
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



# Documentation string. I wonder what ever refers to it?

__doc__ = """Tombola initialization module."""

# Version string. Usually updated automatically by CVS.

__version__ = '0.1'

import YTombola

def initialize(context):
	"""Initialize the Tombola product."""

	try:
		"""Try to register the product."""

		context.registerClass(

			YTombola.YTombola,				# Which is the addable bit?

			constructors = (				# The first of these is called
				YTombola.manage_addForm, 	# when someone adds the product;
				YTombola.manage_add),		# the second is named here so we
											# can give people permission to
											# call it.

				icon = 'bola3.gif'
			)

	except:
		"""	If you can't register the product, tell someone
			(assuming you're running Zope in debug mode)"""

		import sys, traceback, string
		type, val, tb = sys.exc_info()
		sys.stderr.write(string.join(traceback.format_exception(type, val, tb), ''))
		del type, val, tb

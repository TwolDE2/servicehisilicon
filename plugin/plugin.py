from __future__ import absolute_import
from Plugins.Plugin import PluginDescriptor
from Components.config import config


def autostart(reason, **kwargs):
	from . import servicehisilicon


def Plugins(**kwargs):
	try:
		if config.misc.disableServiceHiSilicon.value:
			return []
	except Exception:
		pass
	return [
		PluginDescriptor(where=PluginDescriptor.WHERE_AUTOSTART, needsRestart=True, fnc=autostart)
	]

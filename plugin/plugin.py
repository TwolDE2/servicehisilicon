from Components.config import config
from Plugins.Plugin import PluginDescriptor


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

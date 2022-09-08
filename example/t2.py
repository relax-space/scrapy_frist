'''
测试: _get_commands_from_module
'''

from asset.b2 import _get_commands_from_module

cmds = _get_commands_from_module('asset.b3', True)
print(cmds)

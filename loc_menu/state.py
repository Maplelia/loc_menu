# -*- coding: utf-8 -*-
"""
运行时状态：config 的加载、保存
"""
import copy

from loc_menu.constants import CONFIG_FILE, DEFAULT_CONFIG

config = copy.deepcopy(DEFAULT_CONFIG)


def load_config(server):
    result = server.load_config_simple(
        CONFIG_FILE,
        default_config=copy.deepcopy(DEFAULT_CONFIG),
        echo_in_console=True,
    )
    config.clear()
    config.update(result)
    for key, value in DEFAULT_CONFIG.items():
        config.setdefault(key, value)


def save_config(server):
    server.save_config_simple(config, CONFIG_FILE)

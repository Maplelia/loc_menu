# -*- coding: utf-8 -*-
"""
常量定义：插件 ID、配置文件名、默认配置、维度映射
"""

PLUGIN_ID = "loc_menu"
CONFIG_FILE = "loc_menu.json"

DEFAULT_CONFIG = {
    "command_prefix": "!!lm",
    "menu_title": "【位置列表】",
    "group_selection_title": "请选择分组：",
    "buttons_per_row": 3,
    "button_format": "[{index}]",
    "group_button_format": "[{display}]",
    "location_format": "【{name}】 ({x}, {y}, {z}) @{dim}",
    "groups": {
        "红石": {
            "waypoints": [
                {"name": "出生点", "x": 0, "y": 64, "z": 0, "dim": "0"},
                {"name": "红石区", "x": 500, "y": 64, "z": 0, "dim": "0"}
            ]
        },
        "建筑": {
            "waypoints": [
                {"name": "出生点", "x": 0, "y": 64, "z": 0, "dim": "0"},
                {"name": "建筑区", "x": -500, "y": 64, "z": 0, "dim": "0"}
            ]
        }
    }
}

DIMENSION_NUM_TO_ID = {
    "0": "minecraft:overworld",
    "-1": "minecraft:the_nether",
    "1": "minecraft:the_end",
}

DIMENSION_NUM_TO_NAME = {
    "0": "主世界",
    "-1": "下界",
    "1": "末地",
}

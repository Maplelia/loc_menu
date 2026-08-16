# -*- coding: utf-8 -*-
"""
工具函数：维度转换、编号索引
"""
from loc_menu.constants import DIMENSION_NUM_TO_ID, DIMENSION_NUM_TO_NAME


def dim_to_stored(dim):
    d = str(dim).strip().lower()
    if d in DIMENSION_NUM_TO_ID:
        return d
    if d in ("overworld", "minecraft:overworld", "主世界"):
        return "0"
    if d in ("nether", "the_nether", "minecraft:the_nether", "下界"):
        return "-1"
    if d in ("end", "the_end", "minecraft:the_end", "末地"):
        return "1"
    return str(dim)


def dim_to_command(dim):
    d = str(dim).strip()
    return DIMENSION_NUM_TO_ID.get(d, d)


def dim_to_display(dim):
    d = str(dim).strip()
    return DIMENSION_NUM_TO_NAME.get(d, d)


def get_waypoint_from_index(waypoints, idx):
    if 1 <= idx <= len(waypoints):
        return waypoints[idx - 1]
    return None

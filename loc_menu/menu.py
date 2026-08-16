# -*- coding: utf-8 -*-
"""
RText 菜单构建：位置列表、分组选择界面
"""
from mcdreforged.api.all import *
from loc_menu import state
from loc_menu.utils import dim_to_display


def build_menu(waypoints, group_name=None):
    """生成分组位置列表（点击发送位置到聊天栏，点击 × 删除）"""
    lines = RTextList()
    lines.append(RText(state.config["menu_title"] + "\n", color=RColor.gold))
    for i, wp in enumerate(waypoints, start=1):
        info = state.config["location_format"].format(
            name=wp["name"], x=wp["x"], y=wp["y"], z=wp["z"],
            dim=dim_to_display(wp["dim"])
        )
        btn = (
            RText(state.config["button_format"].format(index=i) + " " + wp["name"], color=RColor.aqua)
            .c(RClickAction.suggest_command, info)
            .h(
                RText(f"位置: {wp['name']}\n", color=RColor.gold),
                RText(f"坐标: {wp['x']}, {wp['y']}, {wp['z']}\n", color=RColor.green),
                RText(f"维度: {dim_to_display(wp['dim'])}\n", color=RColor.aqua),
                RText("点击发送到聊天栏", color=RColor.yellow),
            )
        )
        lines.append(btn)
        if group_name is not None:
            del_cmd = f'{state.config["command_prefix"]} del {group_name} {i}'
            del_btn = (
                RText(" [×]", color=RColor.red)
                .c(RClickAction.suggest_command, del_cmd)
                .h(RText("点击删除路径点", color=RColor.red))
            )
            lines.append(del_btn)
        lines.append("\n")
    lines.append(RText("点击位置发送到聊天栏，点击 [×] 填入确认命令", color=RColor.gold))
    return lines


def build_group_selection():
    """生成分组选择界面（点击分组自动填入 group 命令）"""
    lines = RTextList()
    lines.append(RText(state.config["group_selection_title"] + "\n", color=RColor.gold))
    per_row = max(1, state.config["buttons_per_row"])
    group_names = list(state.config["groups"].keys())
    for row_start in range(0, len(group_names), per_row):
        row = RTextList()
        for offset in range(per_row):
            idx = row_start + offset
            if idx >= len(group_names):
                break
            gname = group_names[idx]
            gdata = state.config["groups"][gname]
            btn = (
                RText(state.config["group_button_format"].format(
                    display=gname
                ), color=RColor.aqua)
                .c(RClickAction.suggest_command,
                   f'{state.config["command_prefix"]} group {gname}')
                .h(RText(f"分组: {gname}\n"
                         f"位置数量: {len(gdata['waypoints'])}\n"
                         "点击自动填入查看命令"))
            )
            row.append(btn)
            row.append(RText("  ", color=RColor.white))
        lines.append(row)
        lines.append("\n")
    lines.append(RText("点击分组后回车，即可查看该组位置", color=RColor.gold))
    return lines

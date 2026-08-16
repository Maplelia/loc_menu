# -*- coding: utf-8 -*-
"""
命令处理函数
"""
from mcdreforged.api.all import *
from loc_menu import state
from loc_menu import menu
from loc_menu.constants import PLUGIN_ID
from loc_menu.utils import dim_to_stored, dim_to_command, dim_to_display, get_waypoint_from_index
import minecraft_data_api as api


def show_help(source, args=None):
    """显示帮助信息"""
    prefix = state.config["command_prefix"]
    lines = RTextList()
    lines.append(RText(f"===== {prefix} 帮助 =====\n", color=RColor.gold))
    help_map = [
        ("", "显示本帮助"),
        ("list", "选择分组查看坐标"),
        ("list <组名>", "查看指定分组的坐标"),
        ("group", "选择分组查看坐标"),
        ("group <组名>", "查看指定分组的坐标"),
        ("add <组> <名称> <x> <y> <z> [维度]", "添加坐标点"),
        ("add here <组> <名称>", "添加当前位置为坐标点"),
        ("tp <组> <编号>", "传送到坐标（仅创造模式）"),
        ("del <组> <编号>", "请求删除坐标点"),
        ("confirm <组> <编号>", "确认删除坐标点"),
        ("reload", "重载配置"),
    ]
    for cmd, desc in help_map:
        if cmd:
            cmd_text = f"{prefix} {cmd}"
        else:
            cmd_text = prefix
        lines.append(RText(f"  {cmd_text}", color=RColor.aqua))
        lines.append(RText(f" - {desc}\n", color=RColor.gray))
    lines.append(RText("维度数字: 0=主世界, -1=下界, 1=末地", color=RColor.dark_green))
    source.reply(lines)


@new_thread(PLUGIN_ID)
def open_menu(source, args):
    """!!lm - 显示帮助"""
    show_help(source, args)


@new_thread(PLUGIN_ID)
def show_group_selection(source, args):
    """!!lm list / !!lm group - 显示分组选择"""
    source.reply(menu.build_group_selection())


@new_thread(PLUGIN_ID)
def list_waypoints(source, args):
    """!!lm list <组名> / !!lm group <组名> - 显示指定分组坐标"""
    group = args["group"]
    if group not in state.config["groups"]:
        source.reply(RText(f"分组 {group} 不存在", color=RColor.red))
        return
    source.reply(menu.build_menu(state.config["groups"][group]["waypoints"], group))


@new_thread(PLUGIN_ID)
def add_waypoint(source, args):
    group = args["group"]
    if group not in state.config["groups"]:
        source.reply(RText(f"分组 {group} 不存在", color=RColor.red))
        return
    name = args["name"]
    try:
        x = int(args["x"])
        y = int(args["y"])
        z = int(args["z"])
    except ValueError:
        source.reply(RText("坐标必须为整数，请检查输入", color=RColor.red))
        return
    dim = dim_to_stored(args.get("dim", "0"))
    state.config["groups"][group]["waypoints"].append(
        {"name": name, "x": x, "y": y, "z": z, "dim": dim}
    )
    state.save_config(source.get_server())
    wp_index = len(state.config["groups"][group]["waypoints"])
    source.reply(RText(f"已添加: [{wp_index}] {name} ({x}, {y}, {z}) 到分组 {group}", color=RColor.green))


@new_thread(PLUGIN_ID)
def add_here(source, args):
    """!!lm add here <组> <名称> - 添加玩家当前位置为坐标点"""
    if not isinstance(source, PlayerCommandSource):
        source.reply(RText("仅玩家可使用此命令", color=RColor.red))
        return
    group = args["group"]
    if group not in state.config["groups"]:
        state.config["groups"][group] = {"waypoints": []}
        state.save_config(source.get_server())
        source.reply(RText("[WARNING: 已自动创建新分组]", color=RColor.red))
    name = args["name"]
    player = source.player
    try:
        pos = api.get_player_coordinate(player)
        dim = api.get_player_dimension(player)
    except Exception:
        source.reply(RText("无法获取玩家位置，请稍后再试", color=RColor.red))
        return
    x, y, z = round(pos.x), round(pos.y), round(pos.z)
    dim = dim_to_stored(dim)
    state.config["groups"][group]["waypoints"].append(
        {"name": name, "x": x, "y": y, "z": z, "dim": dim}
    )
    state.save_config(source.get_server())
    wp_index = len(state.config["groups"][group]["waypoints"])
    source.reply(RText(f"已添加: [{wp_index}] {name} ({x}, {y}, {z}) @{dim_to_display(dim)} 到分组 {group}", color=RColor.green))


def _resolve_waypoint(source, group, index):
    """校验分组与编号，返回 (waypoint, waypoints, idx)；失败返回 None"""
    if group not in state.config["groups"]:
        source.reply(RText(f"分组 {group} 不存在", color=RColor.red))
        return None
    try:
        idx = int(index)
    except ValueError:
        source.reply(RText("编号必须为整数", color=RColor.red))
        return None
    waypoints = state.config["groups"][group]["waypoints"]
    wp = get_waypoint_from_index(waypoints, idx)
    if wp is None:
        source.reply(RText(f"编号 {idx} 不存在", color=RColor.red))
        return None
    return wp, waypoints, idx


@new_thread(PLUGIN_ID)
def tp_waypoint(source, args):
    """!!lm tp <组> <编号> - 传送到指定坐标（仅创造模式）"""
    if not isinstance(source, PlayerCommandSource):
        source.reply(RText("仅玩家可用", color=RColor.red))
        return
    player = source.player
    try:
        gamemode = api.get_player_info(player, 'playerGameType')
    except Exception:
        source.reply(RText("无法获取玩家游戏模式", color=RColor.red))
        return
    if gamemode != 1:
        source.reply(RText("仅创造模式可使用此命令", color=RColor.red))
        return
    resolved = _resolve_waypoint(source, args["group"], args["index"])
    if resolved is None:
        return
    wp, _, _ = resolved
    cmd = f"/execute in {dim_to_command(wp['dim'])} run tp {player} {wp['x']} {wp['y']} {wp['z']}"
    source.get_server().execute(cmd)
    source.reply(RText(f"已传送 {player} 到 {wp['name']} ({wp['x']}, {wp['y']}, {wp['z']}) @{dim_to_display(wp['dim'])}", color=RColor.green))


@new_thread(PLUGIN_ID)
def del_waypoint(source, args):
    """!!lm del <组> <编号> - 请求删除坐标点（需 confirm 确认）"""
    resolved = _resolve_waypoint(source, args["group"], args["index"])
    if resolved is None:
        return
    wp, _, idx = resolved
    confirm_cmd = f'{state.config["command_prefix"]} confirm {args["group"]} {idx}'
    source.reply(RTextList(
        RText(f"确认删除 [{idx}] {wp['name']}? ", color=RColor.gold),
        RText("[确认]", color=RColor.red)
        .c(RClickAction.suggest_command, confirm_cmd)
        .h(RText("点击填入确认命令，回车后删除", color=RColor.red))
    ))


@new_thread(PLUGIN_ID)
def confirm_remove(source, args):
    """!!lm confirm <组> <编号> - 确认删除坐标点"""
    resolved = _resolve_waypoint(source, args["group"], args["index"])
    if resolved is None:
        return
    wp, waypoints, idx = resolved
    waypoints.remove(wp)
    state.save_config(source.get_server())
    source.reply(RText(f"已删除: [{idx}] {wp['name']} 从分组 {group}", color=RColor.green))


@new_thread(PLUGIN_ID)
def reload_plugin(source, args):
    server = source.get_server()
    state.load_config(server)
    source.reply(RText("配置已重载", color=RColor.green))


def player_joined(server, player, info):
    """玩家进服时自动发送分组选择界面"""
    server.tell(player, menu.build_group_selection())

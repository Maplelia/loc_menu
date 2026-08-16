# -*- coding: utf-8 -*-
"""
loc_menu 插件入口：注册命令与事件监听
"""
from mcdreforged.api.all import *
from loc_menu import state
from loc_menu import commands


def register(server):
    state.load_config(server)
    prefix = state.config["command_prefix"]
    server.register_help_message(prefix, "按分组查看坐标")
    builder = SimpleCommandBuilder()
    builder.arg("group", Text)
    builder.arg("name", QuotableText)
    builder.arg("x", Text)
    builder.arg("y", Text)
    builder.arg("z", Text)
    builder.arg("dim", Text)
    builder.arg("index", Text)
    builder.command(prefix, commands.open_menu)
    builder.command(prefix + " list", commands.show_group_selection)
    builder.command(prefix + " list <group>", commands.list_waypoints)
    builder.command(prefix + " group", commands.show_group_selection)
    builder.command(prefix + " group <group>", commands.list_waypoints)
    builder.command(prefix + " add <group> <name> <x> <y> <z>", commands.add_waypoint)
    builder.command(prefix + " add <group> <name> <x> <y> <z> <dim>", commands.add_waypoint)
    builder.command(prefix + " add here <group> <name>", commands.add_here)
    builder.command(prefix + " tp <group> <index>", commands.tp_waypoint)
    builder.command(prefix + " del <group> <index>", commands.del_waypoint)
    builder.command(prefix + " confirm <group> <index>", commands.confirm_remove)
    builder.command(prefix + " reload", commands.reload_plugin)
    builder.register(server)
    server.register_event_listener(MCDRPluginEvents.PLAYER_JOINED, commands.player_joined)


def on_load(server, old_module):
    register(server)

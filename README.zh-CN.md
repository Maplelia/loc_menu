<div align="center">

# LocMenu for MCDReforged

[English](/README.md) | 简体中文

</div>

> [!NOTE]
> LocMenu 是一个按分组展示坐标的 [MCDReforged](https://github.com/MCDReforged/MCDReforged) 插件。点击位置即可将坐标发送到聊天栏，支持悬停查看坐标维度、两步确认删除、添加当前位置和创造模式传送。

<details>
<summary>目录(点击展示)</summary>

- [LocMenu for MCDReforged](#locmenu-for-mcdreforged)
  - [使用](#使用)
  - [配置](#配置)
  - [故障排查](#故障排查)
  - [许可证](#许可证)

</details>

## 使用

输入 `!!lm` 以显示本插件的所有功能

### 分组

|指令|用途|
|---|---|
|`!!lm list`|显示分组选择（点击分组自动填入 `!!lm group <分组>`）|
|`!!lm list <分组>`|查看指定分组的坐标列表|
|`!!lm group`|同 `!!lm list`|
|`!!lm group <分组>`|同 `!!lm list <分组>`|

> [!TIP]
> 坐标列表中，点击位置可将其发送到聊天栏；悬停可查看名称、坐标和维度；点击红色 `[×]` 可请求删除。

---

### 添加坐标

|指令|用途|
|---|---|
|`!!lm add <分组> <路径> <x> <y> <z> [维度]`|手动添加坐标点|
|`!!lm add here <分组> <路径>`|添加当前玩家位置（分组不存在时自动新建）|

> 维度值：`0`/`-1`/`1`，或 `overworld`/`nether`/`end`，或 `主世界`/`下界`/`末地`

---

### 删除坐标

|指令|用途|
|---|---|
|`!!lm del <分组> <路径>`|请求删除坐标点（显示确认按钮）|
|`!!lm confirm <分组> <路径>`|确认删除坐标点|

> [!TIP]
> 删除采用两步确认：`del` 请求 → 点击 `[确认]` → `confirm` 删除，避免误删。

---

### 传送

|指令|用途|
|---|---|
|`!!lm tp <分组> <路径>`|传送到指定坐标点|

> [!WARNING]
> `tp` 仅限**创造模式**的玩家使用。

---

### 其他

|指令|用途|
|---|---|
|`!!lm reload`|重新加载配置文件|

## 配置

配置文件路径：`config/loc_menu/loc_menu.json`（首次加载自动生成）

默认配置如下：

```json
{
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
                {"name": "出生点", "x": 0, "y": 64, "z": 0, "dim": "0"}
            ]
        }
    }
}
```

---

以下是每个参数的简介：

### 1.command_prefix
值的类型: str

默认值: `!!lm`

命令前缀，所有命令都以它开头。

### 2.menu_title
值的类型: str

默认值: `【位置列表】`

坐标列表的标题。

### 3.group_selection_title
值的类型: str

默认值: `请选择分组：`

分组选择界面的标题。

### 4.buttons_per_row
值的类型: int

默认值: `3`

分组选择界面中每行显示的分组按钮数量。

### 5.button_format
值的类型: str

默认值: `[{index}]`

坐标列表中编号的显示格式，`{index}` 会被替换为编号。

### 6.group_button_format
值的类型: str

默认值: `[{display}]`

分组按钮的显示格式，`{display}` 会被替换为分组名。

### 7.location_format
值的类型: str

默认值: `【{name}】 ({x}, {y}, {z}) @{dim}`

点击坐标时发送到聊天栏的位置信息格式。`{name}`/`{x}`/`{y}`/`{z}`/`{dim}` 会被替换为对应值。

### 8.groups
值的类型: dict

默认值: 见上方

分组配置。每个分组以**分组名**为 key（显示和操作同名），包含一个 `waypoints` 列表。

每个坐标点包含：
- `name` — 显示名称
- `x`、`y`、`z` — 坐标
- `dim` — 维度（`"0"` 主世界，`"-1"` 下界，`"1"` 末地）

> [!TIP]
> 修改配置后使用 `!!lm reload` 使更改生效，无需重启 MCDR。

## 故障排查

|症状|可能原因|解决方法|
|---|---|---|
|`分组 X 不存在`|分组名拼写错误或未创建|用 `!!lm list` 查看现有分组，或用 `!!lm add here X <名称>` 自动创建|
|`无法获取玩家位置`|玩家数据未就绪或查询超时|稍后重试|
|`仅创造模式可使用此命令`|`tp` 仅限创造模式|切换为创造模式（`/gamemode creative`）|
|`编号必须为整数`|编号输入了非数字|输入正确的数字编号|
|`编号 X 不存在`|编号超出范围|用 `!!lm list <分组>` 查看当前编号|

## 许可证
MIT License, Copyright (c) 2026 LocMenu Contributors

<div align = "center">

---

[回到顶部](#locmenu-for-mcdreforged)

</div>

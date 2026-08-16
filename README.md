<div align="center">

# LocMenu for MCDReforged

English | [简体中文](/README.zh-CN.md)

</div>

> [!NOTE]
> LocMenu is a [MCDReforged](https://github.com/MCDReforged/MCDReforged) plugin that displays coordinates organized by group. Click a location to share it to chat, hover to view its coordinates and dimension, with two-step deletion, add-current-location and creative-mode teleport.

<details>
<summary>Table of Contents</summary>

- [LocMenu for MCDReforged](#locmenu-for-mcdreforged)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)

</details>

## Usage

Type `!!lm` to show all features of this plugin

### Groups

|Command|Description|
|---|---|
|`!!lm list`|Show group selection (click a group to auto-fill `!!lm group <group>`)|
|`!!lm list <group>`|Show a group's location list|
|`!!lm group`|Same as `!!lm list`|
|`!!lm group <group>`|Same as `!!lm list <group>`|

> [!TIP]
> In the location list, click a location to send it to chat; hover to view its name, coordinates and dimension; click the red `[×]` to request deletion.

---

### Add locations

|Command|Description|
|---|---|
|`!!lm add <group> <waypoint> <x> <y> <z> [dim]`|Add a location manually|
|`!!lm add here <group> <waypoint>`|Add the player's current location (auto-creates the group)|

> Dimension values: `0`/`-1`/`1`, or `overworld`/`nether`/`end`, or `主世界`/`下界`/`末地`

---

### Delete locations

|Command|Description|
|---|---|
|`!!lm del <group> <waypoint>`|Request deletion of a location (shows a confirm button)|
|`!!lm confirm <group> <waypoint>`|Confirm deletion of a location|

> [!TIP]
> Deletion uses two-step confirmation: `del` requests → click `[confirm]` → `confirm` deletes, preventing accidental removal.

---

### Teleport

|Command|Description|
|---|---|
|`!!lm tp <group> <waypoint>`|Teleport to a location|

> [!WARNING]
> `tp` is only available to players in **creative mode**.

---

### Other

|Command|Description|
|---|---|
|`!!lm reload`|Reload the config file|

## Configuration

Config file: `config/loc_menu/loc_menu.json` (generated automatically on first load)

Default config:

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

Description of each parameter:

### 1.command_prefix
Type: str

Default: `!!lm`

The command prefix. All commands start with it.

### 2.menu_title
Type: str

Default: `【位置列表】`

The title of the location list.

### 3.group_selection_title
Type: str

Default: `请选择分组：`

The title of the group selection screen.

### 4.buttons_per_row
Type: int

Default: `3`

The number of group buttons per row in the group selection screen.

### 5.button_format
Type: str

Default: `[{index}]`

The display format of the index in the location list. `{index}` is replaced by the index.

### 6.group_button_format
Type: str

Default: `[{display}]`

The display format of group buttons. `{display}` is replaced by the group name.

### 7.location_format
Type: str

Default: `【{name}】 ({x}, {y}, {z}) @{dim}`

The location info format sent to chat when clicking a location. `{name}`/`{x}`/`{y}`/`{z}`/`{dim}` are replaced with the corresponding values.

### 8.groups
Type: dict

Default: see above

Group configuration. Each group is keyed by its **name** (display and command share the same name), and contains a `waypoints` list.

Each waypoint contains:
- `name` — display name
- `x`, `y`, `z` — coordinates
- `dim` — dimension (`"0"` overworld, `"-1"` nether, `"1"` end)

> [!TIP]
> After modifying the config, run `!!lm reload` to apply changes without restarting MCDR.

## Troubleshooting

|Symptom|Possible cause|Solution|
|---|---|---|
|`Group X does not exist`|Typo or the group is not created|Use `!!lm list` to view groups, or `!!lm add here X <name>` to auto-create|
|`Cannot get player position`|Player data not ready or query timed out|Try again later|
|`Creative mode only`|`tp` is creative-only|Switch to creative (`/gamemode creative`)|
|`Index must be an integer`|Index is not a number|Enter a valid number|
|`Index X does not exist`|Index out of range|Use `!!lm list <group>` to check current indexes|

## License
MIT License, Copyright (c) 2026 LocMenu Contributors

<div align = "center">

---

[Back to top](#locmenu-for-mcdreforged)

</div>

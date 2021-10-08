# VDM Plugin Template

> For Virtual Domain Manager v1.0.0
> (Only python version supported now)

### SRC API

The VDM framework will load plugin, and execute it via `SRC API` defined below. Specifically, the working directory for the plugin will be a random temporary directory, and the execution will be in separated thread.

|             API NAME              |                    DESCRIPTION                     |
| :-------------------------------: | :------------------------------------------------: |
|        `onStart() -> uint`        |         Execute when the plugin is loaded          |
|        `onStop() -> uint`         |         Execute when the plugin is exited          |
|  `onSave(stat_file:str) -> uint`  |      Execute to save status into `stat_file`       |
| `onResume(stat_file:str) -> uint` |     Execute to resume status from `stat_file`      |
|        `onClose() -> uint`        |          Execute to close the application          |
|       `onDaemon() -> None`        | (Optional) Execute as daemon service in VDM daemon |


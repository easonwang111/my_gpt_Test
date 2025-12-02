# my_gpt_Test

a lightweight、文本驱动的 CSGO 风格原型已经添加到 `csgo_like/` 包中。运行入口：

```bash
python -m csgo_like.main
```

主要模块：
- `config.py`：基础配置与曲线参数。
- `engine.py`：固定时间步的循环调度器。
- `entities.py`：玩家、Bot、武器与投掷物等实体定义。
- `weapons.py`：自动生成的 250 个武器系列数据，行数超过 6000 行，方便后续扩展。
- `hud.py`：文本 HUD 快照。
- `main.py`：组合各子系统并运行一轮演示。

该原型面向学习目的，逻辑简单、运行节奏刻意放慢，便于阅读与修改。

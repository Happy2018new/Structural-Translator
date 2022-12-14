# 更新日志(旧)
- `v40.5 - 2022/10/10 Midnight`
   - 修复了翻译 `JSON` 时 `链命令方块` 永远会丢失数据的问题 & 于 [1e22a37](https://github.com/Happy2018new/Structural-Translator/commit/1e22a37f438c618660889d09cc7c230be4cbbbaf) 修复
- `v40.3 - 2022/10/07 Midnight`
   - 修复了翻译 `JSON` 时命令方块永远是 `红石控制` 的问题 & 于 [293d98f](https://github.com/Happy2018new/Structural-Translator/commit/293d98fb400010fc88c05e3dce8b8c7e00ccb796) 修复
- `v40.1 - 2022/10/04 Afternoon`
   - 修复了在解析 `JSON` 时因容器内物品解析失败而造成的可能的方块错位的问题 & 于 [6345487](https://github.com/Happy2018new/Structural-Translator/commit/634548711e7b932bfb14308e7acd231525f116b0) 修复
- `v40.0 - 2022/10/04 Afternoon`
   - 支持了作弊软件 `白墙` 导出的 `JSON` 文件中的命令方块和容器数据 & 于 [25a70b5](https://github.com/Happy2018new/Structural-Translator/commit/25a70b55fd74f567f88791897b44b71fb214a553) 更新
     > **注意事项**<br>
     > 由于 `v40.0` 更新，因此您可能会安装失败或更新失败，原因是依赖库 `numpy` 无法成功安装。<br>
     > 欲解决此问题，请参考 [此文章](https://www.bilibili.com/read/mobile?id=14467258) 中的解决方案，谢谢。<br>
- `v34.7 - 2022/09/06 Night`
   - 修复了前景层为 `None` 时会翻译失败的问题、修复了部分文案问题 & 于 [92c3c23](https://github.com/Happy2018new/Structural-Translator/commit/92c3c230d26fa1da8b6376809f85113de1546a7b) 修复
- `v34.5 - 2022/09/01 Morning`
   - 修复了下述问题并进行了一些技术型更新 & 于 [8270a2d](https://github.com/Happy2018new/Structural-Translator/commit/8270a2defafc16865c3f8ff51a5c52053cd3d0f4) 更新和修复
     - 大型箱子或大型陷阱箱将不会错误拼接，现在将自动拆分为单个的箱子
     - 修复了输出的 `ans.json` 无法显示中文的问题
     - 修复了输出的日志中，中文是乱码的问题
- `v34.1 - 2022/08/23 Noon`
   - 现在输出的由 `.mcstructure` 转换为的 `.json` 文件将会展开 & 于 [8583c48](https://github.com/Happy2018new/Structural-Translator/commit/8583c483082b3e0e661e38701d7f64510d991e10) 更新
- `v34.0 - 2022/08/23 Morning`
   - 现在 `组件 - 替换方块ID` 将区分替换的是 `方块池` 中的方块还是 `容器` 中的物品 & 于 [3af2fa0](https://github.com/Happy2018new/Structural-Translator/commit/3af2fa02dc33a59840715cd52aae5c283dcdae89) 更新
- `v33.5 - 2022/08/21 Noon`
   - 列表中的数据类型将不再丢失，现在将完整翻译 `.mcstructure` 中的数据 & 于 [48eab3c](https://github.com/Happy2018new/Structural-Translator/commit/48eab3cf0958771ce7b5e6bba55528f0322a96d4) 更新
- `v33.1 - 2022/08/21 Morning`
   - 修复了在翻译命令方块时可能存在的转义问题 & 于 [d7e759c](https://github.com/Happy2018new/Structural-Translator/commit/d7e759c1604a51f795502e02af5f3c2903e029f4) 和 [a7bb844](https://github.com/Happy2018new/Structural-Translator/commit/a7bb84480cc703dd221ec9afa1f32814f1c1bb07) 更新
- `v33.0 - 2022/08/20 Afternoon`
   - 现在将完整解析 `.mcstructure` 文件 & 于 [4597049](https://github.com/Happy2018new/Structural-Translator/commit/45970490d6f1312c012255c94270939d8db14307) 更新
- `v32.5 - 2022/08/20 Morning`
   - 现在在移动画笔时使用了其他类型的命令，一定程度上优化了解压后的文件大小 & 于 [b65eabb](https://github.com/Happy2018new/Structural-Translator/commit/b65eabbcb932f4534f25b4bf949e26d49aaafb40) 和 [f85f649](https://github.com/Happy2018new/Structural-Translator/commit/f85f6495b00e8f4c3bc00308808b1fc5e98c18bd) 更新
- `v32.2 - 2022/08/19 Morning`
   - 修复了在使用 `组件 - 替换方块ID` 时可能导致的容器内物品丢失的问题 & 于 [5b38745](https://github.com/Happy2018new/Structural-Translator/commit/5b38745f5a01050212bfaa8a4594b4e15e0c8806) 修复
- `v32.0 - 2022/08/19 Morning`
   - `组件 - 替换方块ID` 将会对容器内的物品生效 & 于 [943ee3d](https://github.com/Happy2018new/Structural-Translator/commit/943ee3d174a0b44442f36cb52233abc639970757) 更新
- `v31.5 - 2022/08/18 Noon`
   - 修复了容器为空时不会放置的问题 & 于 [5cebe8d](https://github.com/Happy2018new/Structural-Translator/commit/5cebe8db0a1b854f30d97102a1bde1aa0d25ea2b) 修复
- `v31.0 - 2022/08/18 Noon`
   - 支持了 `潜影盒` 中的物品(仅限 `物品数据值` ) & 于 [bcbc0dd](https://github.com/Happy2018new/Structural-Translator/commit/bcbc0dd727bf7a1d6698653dddecf47b074db0f4) 更新
- `v30.0 - 2022/08/18 Morning`
   - `实验性功能` - 支持了容器中的物品(仅限 `物品数据值` )，具体如下 & 于 [e7d8f4a](https://github.com/Happy2018new/Structural-Translator/commit/e7d8f4ab88f4584de79ab773b41dbe339956049a) 更新
   ```
   高炉(燃烧的高炉)
   烟熏炉(燃烧的烟熏炉)
   熔炉(燃烧的熔炉)
   木桶
   箱子
   陷阱箱
   讲台
   漏斗
   发射器
   投掷器
   炼药锅(岩浆炼药锅)
   唱片机
   酿造台
   ```
- `v26.4 - 2022/08/13 Afternoon`
   - 修复了在使用 `组件 - 替换方块ID` 时会打印 `方块池` 列表的问题 & 于 [31e43eb](https://github.com/Happy2018new/Structural-Translator/commit/31e43eb705d9b9eb5cc63fd33e7c75c9419ee569) 修复
- `v26.3 - 2022/08/13 Afternoon`
   - 修复了在使用 `组件 - 替换方块ID` 时 `摆烂` 数据会丢失的问题，同时机制变更为如下 & 于 [4b4347b](https://github.com/Happy2018new/Structural-Translator/commit/4b4347b9b368657427b872f03bac33ecb3a51636) 修复
     - 当替换了 `minecraft:double_plant` 时，此方块若原本存在 `摆烂` 标记，则标记会丢失。
     - 如果 `replaceBlockId.txt` 未提到正确的替换 `minecraft:double_plant` 的命令，则相关的 `摆烂` 标记会予以保留。
- `v26.0 - 2022/08/12 Night`<br>
   - 修复了 `minecraft:double_plant` 在放置后会被破坏为掉落物的问题(恢复了原有的 `摆烂` 机制) & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 修复
   - 当被翻译的结构存在 `含水方块` 时，会在翻译即将结束时打印警告 & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 更新
   - 修复了无法正常解析 `带釉陶瓦` 这一类方块的数据值的问题 & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 修复
- `v25.1 - 2022/08/12 Night`
   - 修复了无法正常解析 `minecraft:portal` 的数据值的问题 & 于 [82d043f](https://github.com/Happy2018new/Structural-Translator/commit/82d043ff42741f49bb910a126ecf15a75be78bb7) 和 [fe7eb74](https://github.com/Happy2018new/Structural-Translator/commit/fe7eb749909081234c518739af90b38ed3487db8) 修复
- `v25.0 - 2022/08/12 Afternoon`
   - 修复了无法正常解析下述方块的方块状态的问题 & 于 [9dc98f3](https://github.com/Happy2018new/Structural-Translator/commit/9dc98f3f2930a9257fc6bdb87bed8b4dbc1d8f9c) 修复<br>
      ```
      minecraft:dirt
      minecraft:stained_glass_pane
      minecraft:stained_hardened_clay
      minecraft:carpet
      minecraft:bedrock
      minecraft:cobblestone_wall
      minecraft:lantern
      minecraft:fence
      minecraft:chain
      minecraft:monster_egg
      minecraft:lightning_rod
      minecraft:stripped_warped_hyphae
      minecraft:crimson_hyphae
      minecraft:warped_hyphae
      minecraft:stripped_crimson_hyphae
      minecraft:mangrove_wood
      minecraft:stripped_mangrove_wood
      minecraft:sand
      ```
- `v23.0 - 2022/08/11 Night`
   - 修复了 白墙( `作弊类软件` ) 导出的建筑文件( `JSON` )不能被正常翻译的问题 & 于 [d8f640f](https://github.com/Happy2018new/Structural-Translator/commit/d8f640fb7eada15946f2cb79ac7a2c2393d3b1ca) 修复
- `v22.0 - 2022/08/11 Afternoon`
   - 在一定程度上支持了 白墙( `作弊类软件` ) 导出的建筑文件( `JSON` ) & 于 [3642335](https://github.com/Happy2018new/Structural-Translator/commit/36423355547af1d0141ebb8bc867e364408e272c) 更新
- `v20.5 - 2022/08/11 Morning`
   - 现在在移动画笔时使用了其他类型的命令，一定程度上优化了解压后的文件大小 & 于 [f6cf5ee](https://github.com/Happy2018new/Structural-Translator/commit/f6cf5ee559551f63e6dda714193dbd01c39f32ef) 更新
- `v20.2 - 2022/08/10 Morning`
  - 修复了无法正常解析 `minecraft:planks` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 修复
- `v20.1 - 2022/08/09 Night`
  - 修复了无法正常解析 `minecraft:stone` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 和 [895ac42](https://github.com/Happy2018new/Structural-Translator/commit/895ac4285c2ee1415236905a2017d9ddc06e82f2) 修复
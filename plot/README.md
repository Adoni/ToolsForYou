绘图工具
====

目前支持折线图、柱状图、堆积柱状图

数据格式见[data](./data)文件夹
**注意每一行有多个值得时候，使用tab分隔！**

用法：

    python plot.py [function_name] [data_file_name]

例子：

* 折线图：`python3 plot.py line data/toy_data_for_line_plot.txt`
* 柱状图：`python3 plot.py bar data/toy_data_for_line_plot.txt`
* 堆积柱状图：`python3 plot.py stack_bar data/toy_data_for_line_plot.txt`

程序内存监测
====

首先安装依赖库：`pip3 install psutil`

使用方法：


    python3 name cmd

其中，`name`指的是要存的名字，不能有空格，例如，如果`name`值为`baseline1`，那么监测数据就会保存在`name.monitor_info.data`这个文件中,`cmd`指的是原本要执行的命令

例如：

    python3 test_file python test.py

就是说对`python3 test.py`这一条原本要执行的命令进行监测，数据会保存到`test_file.monitor_info.data`中

另外，附加了一个`show_results.py`文件，目的是分析保存的监测数据，目前仅仅是把实际使用的内存的曲线和虚拟内存曲线画出来，使用方法是 `python3 show_results.py file_name`

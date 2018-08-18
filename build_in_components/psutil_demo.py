import psutil


def cpu_fun():
    psutil.cpu_count()  # CPU逻辑数量
    psutil.cpu_count(logical=False)  # CPU物理核心
    # 2说明是双核超线程, 4则是4核非超线程
    psutil.cpu_times()  # 统计CPU的用户／系统／空闲时间

    for x in range(10):
        psutil.cpu_percent(interval=1, percpu=True)


# 获取内存信息
def memory_fun():
    psutil.virtual_memory()
    psutil.swap_memory()


# 获取磁盘信息
def disk_fun():
    psutil.disk_partitions()
    psutil.disk_usage("/")
    psutil.disk_io_counters()


# 获取网络信息
def network_fun():
    psutil.net_io_counters()
    psutil.net_if_addrs()
    psutil.net_if_stats()
    psutil.net_connections()


# 获取进程信息
def process_fun():
    psutil.pids()
    psutil.test()


cpu_fun()
memory_fun()
disk_fun()
network_fun()
process_fun()

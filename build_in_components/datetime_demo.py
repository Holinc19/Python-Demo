from datetime import datetime

print(datetime.now())  # 获取当前datetime
print(datetime(2015, 4, 19, 12, 20, 30))  # 用指定日期时间创建datetime
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))

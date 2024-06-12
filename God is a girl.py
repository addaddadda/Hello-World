import subprocess
import time

start_time = time.time()  # 记录程序开始时间
try:
    while True:
        # 获取当前小时（24小时制）
        current_hour = int(time.strftime('%H'))

        present_time = time.time() - start_time  # 记录当前时间

        # 当前时间晚于等于晚上9点时执行
        if current_hour >= 21 or present_time >= 3600:
            # 立即强制关机
            subprocess.run(["shutdown", "-s", "-f", "-t", '1'])
            exit()  # 程序执行关机命令后退出

        # 检查频率：每10秒一次
        time.sleep(10)

except Exception as e:
    # 记录异常日志
    with open('error_log.txt', 'a') as f:
        f.write(f"An error occurred at {time.strftime('%Y-%m-%d %H:%M:%S')}: {str(e)}\n")
        f.close()

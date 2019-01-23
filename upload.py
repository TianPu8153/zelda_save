import subprocess 
import shlex 
import os
import time
import psutil
'''
思路：
1.先进入对应文件目录
2.pull一边代码（如果没有更新可以跳过）
3.打开exe文件并且记录pid
4.while true循环查看pid是否存活time.sleep(60)
5.pid不存活时，将需要的文件上传到git
'''
#先读取设置
f = open("settings.txt","r")   #设置文件对象
data = f.readlines()  #直接将文件中按行读到list里，效果与方法2一样
auto_pull=bool(data[0].split("=")[1].split("\n")[0])
auto_push=bool(data[1].split("=")[1].split("\n")[0])
f.close()
#写pull的代码
# if(auto_pull==True):
# 	os.system("git fetch")
# 	os.system("git diff origin/master")
# 	os.system("git merge origin master")
p = subprocess.Popen(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe") 
q = psutil.Process(p.pid) 
while(True):
	time.sleep(2)
	try:
		q.status()
	except :
		#pid对应的进程结束
		#这里写文件上传的代码
		break

os.system("git add .")
os.system(r'git commit -m "auto"')
os.system('git push origin master')



import subprocess 
import shlex 
import os
import time
import psutil
'''
思路：
1.先读取settings文件的设置
2.pull一遍代码（如果没有必要可以跳过）
3.打开exe文件并且记录pid
4.while true循环查看pid是否存活time.sleep(60)
5.pid不存活时，如有需要，将目标文件夹下的文件上传到git
'''
#先读取设置
# f = open("settings.txt","r")   #设置文件
# data = f.readlines()  #直接将文件中按行读到list里
# auto_pull=bool(data[0].split("=")[1].split("\n")[0])
# auto_push=bool(data[1].split("=")[1].split("\n")[0])
# f.close()
auto_pull=False
auto_push=True
if(auto_pull==True):
	#将远程库的存档覆盖现存档
	os.system("git fetch")
	os.system("git diff origin/master")
	os.system("git merge origin master")
p = subprocess.Popen(r"E:\Cemu+1.8.0+V0.25\cemu.exe") 
q = psutil.Process(p.pid) #os.kill(pid,0)与subprocess.Popen配合有问题
while(True):
	time.sleep(30)
	try:
		q.status()#这里验证打开的程序是否已经关闭
	except :
		#pid对应的进程结束
		#这里写文件上传的代码
		if(auto_push==True):
			os.system("git add .")
			os.system(r'git commit -m "auto"')
			os.system('git push origin master')
		break




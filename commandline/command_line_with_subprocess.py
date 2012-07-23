import os
import subprocess

p = subprocess.Popen('ls', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout_text, stderr_text = p.communicate()
print(stdout_text)


import os

os.makedirs("/var/logs/app", exist_ok=True)

with open("/var/logs/app/log.txt", "a") as f:
    f.write("Log de execução\n")

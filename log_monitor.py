failed_attempts = {}

with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    parts = log.strip().split()

    status = parts[2]
    ip = parts[3]

    if status == "LOGIN_FAILED":
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("=== Security Alert Report ===")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"Suspicious IP: {ip} | Failed Attempts: {count}")
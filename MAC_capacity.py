import paramiko

# SSH 접속 함수
def ssh_and_execute(ip, username, password, script_path):
    try:
        # SSH 클라이언트 생성
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # SSH 접속
        print(f"Connecting to {ip}...")
        ssh.connect(ip, username=username, password=password)

        # sh 파일 실행
        command = f"sh {script_path}"
        print(f"Executing: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)

        # 결과 출력
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(f"Output from {ip}:")
            print(output)
        if error:
            print(f"Error from {ip}:")
            print(error)

        # SSH 연결 종료
        ssh.close()

    except Exception as e:
        print(f"Failed to connect or execute command on {ip}: {e}")

# 여러 IP에 대해 실행
ips = ["192.168.100.100", "192.168.100.101", "192.168.100.102","192.168.100.103","192.168.100.104","192.168.100.105","192.168.100.106","192.168.100.107"]  # 접속할 IP 목록
username = "cm"  # SSH 사용자명
password = "cmcm"  # SSH 비밀번호
script_path = "Desktop/JD/script.sh"  # 고정된 sh 파일 경로

for ip in ips:
    ssh_and_execute(ip, username, password, script_path)

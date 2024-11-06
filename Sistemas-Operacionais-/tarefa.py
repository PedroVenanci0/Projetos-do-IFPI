import psutil
import subprocess
import time

def iniciar_processo(programa):
    try:
        processo = subprocess.Popen([programa])
        print(f"Processo '{programa}' iniciado com PID {processo.pid}.")
        return processo
    except FileNotFoundError:
        print(f"Erro: O programa '{programa}' não foi encontrado.")

def monitorar_processo(processo):
    pid_alvo = processo.pid
    try:
        proc = psutil.Process(pid_alvo)
        print(f"Monitorando processo com PID {pid_alvo}...\n")

        while proc.is_running():
            status = proc.status()
            cpu_percent = proc.cpu_percent(interval=1)
            memoria = proc.memory_info().rss / (1024 ** 2)

            print(f"Status: {status} | CPU: {cpu_percent}% | Memória: {memoria:.2f} MB")
            time.sleep(2)

        print(f"O processo com PID {pid_alvo} foi finalizado.")
    
    except psutil.NoSuchProcess:
        print(f"O processo com PID {pid_alvo} não foi encontrado.")
    except psutil.AccessDenied:
        print(f"Sem permissão para acessar o processo com PID {pid_alvo}.")

def main():
    programa = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Caminho completo para o Chrome
    processo = iniciar_processo(programa)
    if processo:
        monitorar_processo(processo)

if __name__ == "__main__":
    main()

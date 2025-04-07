from datetime import datetime, timedelta
import random
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Altere o import para testar COPY ou executemany:
from process_log_copy import process_log
# from process_log_executemany import process_log

def gerar_logs(qtd):
    base_time = datetime.now()
    niveis = ['INFO', 'WARNING', 'ERROR']
    logs = []
    for i in range(qtd):
        logs.append({
            "timestamp": base_time + timedelta(seconds=i),
            "level": random.choice(niveis),
            "message": f"Log gerado automaticamente {i}"
        })
    return logs

@pytest.mark.parametrize("qtd", [0, 1, 5, 10])
def test_process_log(qtd):
    logs = gerar_logs(qtd)
    try:
        process_log(logs)
    except Exception as e:
        pytest.fail(f"Erro ao processar logs com quantidade {qtd}: {e}")

if __name__ == "__main__":
    logs = gerar_logs(10)
    process_log(logs)
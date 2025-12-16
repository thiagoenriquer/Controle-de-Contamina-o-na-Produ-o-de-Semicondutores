import random
import time
import json

# Simulação do RF01: Exibir níveis de contaminação em tempo real 
# Simulação do RF04: Emitir alarmes se ultrapassar limites [cite: 116]

LIMITE_CRITICO_PARTICULAS = 100  # Valor hipotético para alarme
ID_SENSOR = "SENSOR_PARTICULAS_01"

def ler_sensor():
    """Simula a leitura de dados do CLP"""
    return random.randint(50, 120)

def monitorar_processo():
    print(f"Iniciando monitoramento do sensor {ID_SENSOR}...")
    
    try:
        while True:
            valor_atual = ler_sensor()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            payload = {
                "timestamp": timestamp,
                "sensor_id": ID_SENSOR,
                "valor": valor_atual,
                "status": "NORMAL"
            }

            # Lógica de Alarme (RF04)
            if valor_atual > LIMITE_CRITICO_PARTICULAS:
                payload["status"] = "CRITICO - ALARME"
                print(f"[ALARME] {timestamp} - Valor {valor_atual} excedeu o limite!")
            else:
                print(f"[INFO] {timestamp} - Leitura: {valor_atual}")
            
            # Aqui entraria o código de envio para o Gateway/IHM (MQTT/OPC-UA)
            
            time.sleep(2) # Simula intervalo de leitura (RF01 pede tempo real)

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")

if __name__ == "__main__":
    monitorar_processo()

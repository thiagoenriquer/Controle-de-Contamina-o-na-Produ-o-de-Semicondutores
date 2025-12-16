# Sistema de Supervisão: Controle de Contaminação na Produção de Semicondutores

## Sobre o Projeto
Este projeto consiste em uma solução de supervisão industrial voltada ao monitoramento do processo de inspeção e limpeza de wafers na fabricação de semicondutores. O objetivo é garantir o controle contínuo de parâmetros críticos (partículas, pressão, vazão) e integrar dados com sistemas MES.

##  Objetivos
* Minimização da contaminação e maior confiabilidade do produto final.
* Monitoramento em tempo real e emissão de alarmes.
* Rastreabilidade de lotes e histórico de produção.

## Arquitetura
]O sistema segue uma **Arquitetura em Camadas**:
1.  **Camada de Campo:** Sensores e Atuadores.
2.  **Camada de Controle:** CLP/Controlador.
3.  **Edge/Gateway:** Tradução de protocolos (Modbus/Profinet para MQTT/OPC-UA).
4.  **Back-end:** Banco de dados de séries temporais (Historian).
5.  **Apresentação:** IHM e Dashboards para o operador.

##  Ferramentas
* **Linguagens/Frameworks:** Python, C++ (previsto).
* **Protocolos:** MQTT, OPC-UA, Modbus.
* **Documentação:** LaTeX/Overleaf.

##  Autores
* Thiago Henrique de Oliveira Silva.  
* Universidade Federal de Campina Grande (UFCG)

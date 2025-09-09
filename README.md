# PythonESP32

---

## Sobre

Neste projeto, deveriamos montar 4 circuitos com ESP32, responsáveis por:
- Detector de Luminosidade
- Detector de Presença
- Detector de Umidade do Solo
- E por último, resolver um desafio para a empresa Alpha Corp. Para desenvolver uma solução para o
time da produção.
Feito no [SENAI Jandira](https://sp.senai.br/unidade/jandira/)

---

## Tecnologias

- ESP32 (DevKit-C ou equivalente)
- MicroPython v1.22.0 (ambiente usado nos diagramas do Wokwi)
- Python 3.10+ no PC
- Thonny (IDE) ou `mpremote` (linha de comando)
- Wokwi (simulador online)

---

## Pré-requisitos

- Python instalado (3.10 ou superior).
- Instalar a ferramenta de linha de comando `mpremote`:

  ```bash
  pip install mpremote
  ```

- Gravar o firmware do MicroPython na sua ESP32 (se for executar na placa):
  - Baixe em: https://micropython.org/download/ESP32/
  - Grave com a ferramenta de sua preferência (esptool, Thonny, etc.).
- Descobrir a porta serial da sua ESP32 (no Windows, algo como `COM3`).

---

## Clonar o repositório

```bash
git clone https://github.com/lucsnobre/pythonESP32

cd PythonESP32
```

---

## Como executar

Você pode rodar de três formas: Wokwi (simulador), Thonny (IDE) ou `mpremote` (CLI).

### 1) Simular no Wokwi (recomendado para testar rápido)

- Luminosidade: https://wokwi.com/projects/440370533040088065
- Ultrassônico: https://wokwi.com/projects/440379462482355201
- Umidade do Solo: sem link neste repositório — use a placa física ou crie seu próprio projeto no Wokwi.

Abra o link, clique em "Run" e veja o console/LEDs no simulador.

### 2) Rodar na placa com Thonny

1. Conecte a ESP32 no PC e abra o Thonny.
2. Selecione o interpretador: MicroPython (ESP32).
3. Abra uma das pastas (`Luminosidade/`, `Ultrassônico/` ou `Umidade/`).
4. Envie `main.py` para a placa como `main.py` e pressione reset (ou use "Run current script on MicroPython device").

### 3) Rodar na placa via `mpremote` (linha de comando)

Troque `COMX` pela sua porta serial (ex.: `COM3`). No Windows, coloque o caminho entre aspas quando houver acentos.

- Luminosidade

  ```bash
  mpremote connect COMX fs cp "Luminosidade/main.py" :main.py
  mpremote connect COMX reset
  ```

- Ultrassônico

  ```bash
  mpremote connect COMX fs cp "Ultrassônico/main.py" :main.py
  mpremote connect COMX reset
  ```

- Umidade do Solo

  ```bash
  mpremote connect COMX fs cp "Umidade/main.py" :main.py
  mpremote connect COMX reset
  ```

Após o reset, o script `main.py` será executado automaticamente na ESP32.

## Participantes

- [Lucas Nobre](https://www.linkedin.com/in/lucas-rodrigues-nobre-01941b327/)
- [Felipe Bahia](https://www.linkedin.com/in/felipe-bahia-430711324/?trk=opento_sprofile_details)

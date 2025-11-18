# EnergyWise – Análise Inteligente de Consumo Energético

Este projeto faz parte da Global Solution 2025 e realiza uma **análise baseada em dados de consumo energético**, identificando desperdícios e propondo **ganhos ambientais e econômicos**.

## Objetivo
Demonstrar como a análise de dados pode melhorar ambientes de trabalho por meio da **eficiência energética**, reduzindo custos e impactos ambientais.

---

## Solução Desenvolvida – EnergyWise

O EnergyWise é uma solução de análise inteligente que utiliza dados de consumo energético
para identificar desperdícios e propor ações práticas de otimização.

A solução funciona em três etapas:

### 1. Análise de Consumo
O sistema lê dados de consumo horário (kWh) e identifica padrões críticos, como:
- picos elevados de energia,
- horários com sobrecarga,
- desperdícios por uso desnecessário.

### 2. Diagnóstico e Otimização
Com base na análise, o EnergyWise recomenda:
- melhor distribuição de cargas elétricas,
- ajustes nos horários de climatização e iluminação,
- redução de consumo em horários ociosos,
- preparação para futura automação com IoT e integração com energia solar.

### 3. Ganhos Estimados
A solução calcula:
- energia desperdiçada por dia,
- economia mensal e anual em reais,
- redução potencial de CO₂.

Essa análise apoia decisões sustentáveis e melhora a eficiência no ambiente de trabalho.

---

## Impacto no Ambiente de Trabalho e Futuro do Trabalho

A solução EnergyWise melhora diretamente ambientes corporativos ao:

### Reduzir Desperdícios
A análise identifica pontos de uso excessivo de energia, permitindo ajustes imediatos.

### Otimizar Rotinas e Conforto
Redução de picos reduz a sobrecarga do ar-condicionado, melhora o conforto térmico
e diminui custos operacionais.

### Apoiar Decisões Inteligentes
Os relatórios ajudam gestores a tomar decisões baseadas em dados sobre:
- uso de renováveis,
- readequação de horários,
- automação inteligente.

### Preparar para Automação Futuras (IoT)
O diagnóstico pode ser conectado a sensores e sistemas automáticos para:
- desligar iluminação automaticamente,
- controlar climatização,
- gerenciar cargas em tempo real.

Isso representa diretamente o futuro do trabalho: ambientes eficientes, inteligentes e sustentáveis.

# Metodologia

### 1. Coleta de dados
Foram utilizados dados simulados de consumo horário (kWh) em um ambiente corporativo.

### 2. Análise
- Média
- Máximo/mínimo
- Identificação de picos (>80 kWh)
- Estimativa de desperdício
- Cálculo de economia potencial

### 3. Resultados gerados
Incluem:
- Gráfico de consumo ao longo do dia
- Gráfico destacando picos
- Relatório com métricas e estimativas de economia

---



# Estrutura do Projeto

```yaml
data/consumo_energia.csv
docs/desenvolvimento_da_solucao.md
src/analise_energywise.py
outputs/grafico_consumo.png
outputs/grafico_picos.png
outputs/relatorio_resultados.md
```
---

# Como Executar

1. Instale as dependências:
pip install pandas matplotlib

2. Rode:
python src/analise_energywise.py

3. Veja os arquivos resultantes em `/outputs`.

---

# Conexão com o Futuro do Trabalho

Ambientes de trabalho inteligentes precisam:
- monitorar energia em tempo real
- reduzir picos com automações
- prever consumo
- integrar fontes renováveis

A análise ajuda empresas a economizarem e reduzirem CO₂.

---

## Fonte dos Dados

Os dados de consumo energético utilizados são **simulados**, porém baseados em padrões
reais divulgados pela ANEEL sobre consumo típico de escritórios brasileiros.

O arquivo `consumo_energia.csv` representa o consumo de um dia completo, com medições
horárias, refletindo padrões reais de carga elétrica.


---

# Vídeo
O link do vídeo está incluído no arquivo ZIP enviado na plataforma.

# 💰 Projeto FinCatch – Sistema de Controle Financeiro Pessoal

📆 **Período de Execução:** 15 a 31 de outubro de 2025  
🕐 **Tempo disponível:** 2h/dia para desenvolvimento + 2h/dia para estudo (Python e SQL)  
🧠 **Metodologia:** Kanban (Tarefas em “A Fazer”, “Em Progresso” e “Concluído”)  
🗂️ **Controle de Versão:** GitHub  
🗄️ **Banco de Dados:** PostgreSQL  
🐍 **Linguagem:** Python 3 (com `dataclasses`, `customtkinter`, `psycopg2`)  

---

## 🎯 **Objetivo Geral**
Desenvolver um sistema pessoal de controle financeiro — **FinCatch** — para registrar, classificar e visualizar receitas e despesas, organizadas por categorias e contas, com filtros e relatórios mensais.

---

## 🧱 **Etapa 1 – Modelagem e Banco de Dados**  
📅 **Prazo sugerido:** 15 a 18 de outubro  

**Objetivo:** Criar a base lógica e estrutural do sistema (tabelas, triggers e views).  

### 📋 Tarefas:
- [ ] Criar banco de dados `fincatch_db` no PostgreSQL  
- [ ] Criar tabela `categorias`  
- [ ] Criar tabela `transacoes`  
- [ ] (Opcional) Criar tabela `contas`  
- [ ] Criar view `resumo_mensal` (agrupando receitas, despesas e saldo por mês)  
- [ ] Criar trigger `BEFORE INSERT` para transformar despesas em valores negativos  
- [ ] Criar função/procedure `resumo_categoria(mes, ano)`  

### 🧩 Estrutura Básica das Tabelas

#### Tabela: `categorias`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id | SERIAL PK | Identificador único |
| nome | VARCHAR(100) | Nome da categoria | - Lazer
| tipo | VARCHAR(20) | 'receita' ou 'despesa' |
| descricao | TEXT | (opcional) detalhes |

#### Tabela: `transacoes`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id | SERIAL PK | Identificador |
| id_categoria | INT FK → categorias(id) | Categoria vinculada |
| tipo | VARCHAR(20) | 'receita' ou 'despesa' |
| valor | DECIMAL(10,2) | Valor da transação |
| descricao | VARCHAR(200) | Ex: “Mercado”, “Salário” |
| data_transacao | DATE | Data real da movimentação |
| data_registro | TIMESTAMP DEFAULT NOW() | Data de registro |

#### (Opcional) Tabela: `contas`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id | SERIAL PK | Identificador |
| nome | VARCHAR(100) | Nome da conta (ex: Nubank) |
| saldo_inicial | DECIMAL(10,2) | Valor inicial da conta |

---

## 🧰 **Etapa 2 – Backend e Camada de Dados (Model + Controller)**  
📅 **Prazo sugerido:** 19 a 22 de outubro  

**Objetivo:** Implementar as classes base com `dataclasses` e funções CRUD.  

### 📋 Tarefas:
- [ ] Criar módulo `model/` com `dataclasses`:
  - `Categoria`
  - `Transacao`
  - (opcional) `Conta`
- [ ] Criar módulo `controller/` com classes:
  - `CategoriaController`
  - `TransacaoController`
- [ ] Implementar métodos:
  - `inserir()`, `listar_todos()`, `listar_por_id()`, `atualizar()`, `deletar()`
- [ ] Testar no console cada operação CRUD isoladamente  
- [ ] Adicionar logs (`logging`) para auditoria  

🧠 **Dica:**  
> Usar `dataclasses` facilita o mapeamento de cada registro para objetos, deixando o código mais limpo.

---

## 💻 **Etapa 3 – Interface Gráfica (CustomTkinter)**  
📅 **Prazo sugerido:** 23 a 27 de outubro  

**Objetivo:** Construir uma interface moderna e responsiva para o usuário final.  

### 📋 Tarefas:
- [ ] Criar `main.py` com menu principal e navegação entre telas  
- [ ] Criar tela `tela_categorias.py` com cadastro e listagem  
- [ ] Criar tela `tela_transacoes.py` com inserção, edição e filtro por mês  
- [ ] Criar tela `tela_resumo.py` com resumo geral (receita – despesa = saldo)  
- [ ] Padronizar cores e fontes:
  - Cor primária: `#3498DB`
  - Hover: `#2980B9`
  - Fundo: `#F5F6FA`
  - Fonte: `("Segoe UI", 12)`  
- [ ] Adicionar hover e foco visual nos botões  
- [ ] Implementar `trace_add()` nos campos de busca (atualização em tempo real)

---

## 📊 **Etapa 4 – Relatórios e Otimização Final**  
📅 **Prazo sugerido:** 28 a 31 de outubro  

**Objetivo:** Criar resumo financeiro e preparar versão estável.  

### 📋 Tarefas:
- [ ] Criar gráficos (usando `matplotlib` ou `customtkinter.CTkCanvas`)  
- [ ] Exibir resumo mensal: total de receitas, despesas e saldo  
- [ ] Exportar dados para `.csv`  
- [ ] Fazer testes completos de inserção, deleção e atualização  
- [ ] Documentar código e preparar `README.md` para o GitHub  
- [ ] Fazer último commit com tag `v1.0`

---

## 🗂️ **Quadro Kanban – FinCatch**

| 🟦 A Fazer | 🟨 Em Progresso | 🟩 Concluído |
|-------------|----------------|--------------|
| Criação das tabelas | Modelagem `dataclasses` | Conexão com banco |
| CRUD Categoria | CRUD Transação | CRUD funcionando |
| Interface Transações | Interface Categorias | CRUD testado |
| View resumo mensal | Exportar CSV | Versão final ✅ |

---

## ⚙️ **Ferramentas e Stack**
- **Python 3.12+**
- **PostgreSQL**
- **psycopg2**
- **customtkinter**
- **matplotlib**
- **Git + GitHub**

---

## 📘 **Rotina de Estudo e Desenvolvimento**

| Horário | Atividade | Duração |
|----------|------------|----------|
| 06h00 – 08h00 | Estudo (Python + SQL) | 2h |
| 19h00 – 21h00 | Desenvolvimento FinCatch | 2h |
| Domingo | Revisão geral e commits no GitHub | 1h |

---

## 🧾 **Metas de Curto Prazo**
- [ ] Terminar estrutura do banco até **18/10**
- [ ] CRUD completo com `dataclasses` até **22/10**
- [ ] Interface funcional até **27/10**
- [ ] Entrega da versão 1.0 até **31/10**

---

## ✨ **Notas Finais**
O **FinCatch** será o primeiro sistema pessoal de gestão financeira 100% autoral, com banco de dados real, interface moderna e código escalável.  
Esse projeto consolida:
- Prática em **Python + SQL**
- Uso de **PostgreSQL**
- Aplicação de **MVC + Dataclasses**
- Design com **CustomTkinter**
- Controle de versão com **GitHub**

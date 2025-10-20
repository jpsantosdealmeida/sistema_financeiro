# 📘 Plano de Desenvolvimento — Sistema Financeiro **Fincatch**

## 🎯 Objetivo
Desenvolver um sistema pessoal de controle financeiro (receitas, despesas e categorias) com **Python, PostgreSQL e dataclasses**, aplicando boas práticas de arquitetura (MVC) e versionamento no **GitHub**.

---

## 🧱 Etapa 1 — Estruturação do Projeto (Semana 1)
### 🗓 Período: 20 a 24 de outubro
**Meta:** Garantir que o projeto tenha base sólida (organização, banco e ambiente configurado).

- [x] Criar repositório no **GitHub**: `fincatch`
- [x] Estruturar pastas:
fincatch/
├── model/
├── controller/
├── view/
├── database/
└── main.py
- [x] Configurar ambiente virtual (`venv`) e instalar dependências:
- psycopg2  
- customtkinter  
- python-dotenv  
- [x] Criar `.env` com variáveis do PostgreSQL
- [x] Configurar `database.py` com conexão ao Postgres
- [x] Testar conexão e logar erros no terminal ou arquivo `.log`

---

## 💾 Etapa 2 — Modelagem e Banco de Dados (Semana 2)
### 🗓 Período: 25 a 28 de outubro
**Meta:** Implementar o banco e as entidades com dataclasses.

- [x] Criar tabelas no PostgreSQL:
- categorias  
- transacoes  
- (opcional) contas  
- [ ] Adicionar **constraints e triggers**:
- Trigger `BEFORE INSERT`: tornar despesas negativas  
- View `resumo_mensal`
- [x] Criar `categoria.py` e `transacao.py` usando `@dataclass`
- [x] Testar inserção manual de registros via Python (sem interface)

---

## 🧩 Etapa 3 — CRUD e Controle Lógico (Semana 3)
### 🗓 Período: 29 a 31 de outubro
**Meta:** Implementar toda a lógica CRUD e testar com dados reais.

- [ ] Criar `categoria_controller.py`
- inserir / atualizar / listar / deletar
- [ ] Criar `transacao_controller.py`
- inserir / listar por mês / deletar / filtrar por categoria
- [ ] Validar regras:
- despesas negativas  
- cálculo automático de saldo  
- [ ] Adicionar tratamento de erros (try/except + logging)

---

## 💰 Etapa 4 — Interface e Integração (Início de novembro)
### 🗓 Período: 1 a 8 de novembro
**Meta:** Conectar backend ao CustomTkinter e deixar o sistema funcional.

- [ ] Criar tela principal (`TelaMain`) com menu lateral
- [ ] Criar tela de **categorias**
- listagem + cadastro + exclusão
- [ ] Criar tela de **transações**
- lançamentos de receitas e despesas
- [ ] Adicionar filtros (por mês / categoria / tipo)
- [ ] Exibir resumo mensal (saldo, total de gastos e receitas)
- [ ] Testar navegação entre telas e consistência dos dados

---

## 🚀 Etapa Extra — Melhorias Futuras
**Após o MVP (Produto Mínimo Viável)**

- [ ] Adicionar login com senha
- [ ] Criar gráficos com **matplotlib**
- [ ] Implementar exportação de relatórios em `.csv`
- [ ] Adicionar suporte para múltiplos usuários
- [ ] Publicar no GitHub com README detalhado

---

## 📋 Dica de Organização (Kanban)
Use o quadro com 4 colunas:

| A Fazer | Em Progresso | Em Revisão | Concluído |
|----------|---------------|-------------|------------|
| Tarefas novas | O que você está fazendo hoje | O que precisa testar | Tudo que terminou |

---

## 🧭 Sugestão de Rotina Diária (2h/dia)
- **30 min**: revisar código anterior  
- **45 min**: implementar nova tarefa  
- **30 min**: testar e documentar  
- **15 min**: commit + push para GitHub

---

🗂 **Nome do Projeto:** Fincatch  
💡 **Banco de Dados:** PostgreSQL  
💻 **Linguagem:** Python 3.12+  
🧩 **Paradigma:** MVC + dataclasses  
📅 **Prazo estimado:** até 8 de novembro de 2025  

---

> “Organize como se estivesse construindo para outra pessoa.  
> Isso é o que transforma um código em um sistema.” 🚀

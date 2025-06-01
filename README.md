# Utilização do Plugin Setup Python App no cPanel

## 1: Título

* **Título:** Aplicações Web Python com o Plugin Setup Python App do cPanel
* **Subtítulo:** Configuração e utilização do plugin

---

## 2: Objetivos

* Compreender o que faz o plugin Setup Python App
* Aprender a criar e gerir aplicações Python
* Identificar erros comuns e como os resolver
* Analisar exemplos reais (Flask, FastAPI, Django)
* Rever boas práticas de segurança, registo de logs e manutenção

---

## 3: O Que é o Plugin Setup Python App?

* Parte do CloudLinux + cPanel
* Permite aos utilizadores correr aplicações Python em alojamento partilhado
* Gere:

  * Versão do Python (através do Python Selector)
  * Ambientes virtuais
  * Configuração WSGI (com Passenger)

---

## 4: Ciclo de Vida da Aplicação

* **Criar:**

  * Escolher versão do Python
  * Definir diretório da app, URI e entry points
* **Configurar:**

  * Ficheiro de arranque, função entry point (ex.: `app`)
  * Ficheiro WSGI (ex.: `passenger_wsgi.py`)
* **Manter:**

  * Reiniciar após alterações no código ou configuração
  * Modificar variáveis de ambiente

---

## 5: Boas Práticas de Estrutura de Ficheiros

* Exemplo:

  ```
  ~/appname/
    |-- venv/
    |-- app.py
    |-- passenger_wsgi.py
    |-- templates/
    |-- static/
  ```
* Evitar colocar código em `public_html`
* Manter `venv/` e o código da app privados

---

## 6: Terminal e Virtualenv

* Aceder via Terminal do cPanel ou SSH
* Ativar virtualenv:

  ```bash
  source ~/appname/venv/bin/activate
  ```
* Instalar pacotes:

  ```bash
  pip install flask
  ```
* Reiniciar a app após alterações

---

## 7: Aplicações de Exemplo

* **Flask:** Formulário de contacto com validação e tratamento de erros
* **FastAPI:** API de matemática com input em JSON e erros não tratados
* **Django:** Autenticação + ligação a MySQL (admin e modelos básicos)

---

## 8: Logs e Depuração

* Ver logs no Gestor de Ficheiros ou Terminal:

  * `error_log`
  * `passenger.log`
  * Logs definidos pela app (ex.: `app.log`)
* Usar o módulo `logging` para logs estruturados
* Adicionar nome do ficheiro e linha para melhor rastreio

---

## 9: Problemas Comuns

* App mostra listagem de diretório: WSGI mal configurado
* Erros 502/500: caminhos errados, `venv` em falta, erros de sintaxe
* Erros de pacotes: falta de `wheel`, GCC ou headers

---

## 10: Dicas de Segurança

* Negar acesso a ficheiros `.py` com `.htaccess`:

  ```apache
  <FilesMatch "\.py$">
      Require all denied
  </FilesMatch>
  ```
* Não armazenar `.env`, `.git`, etc. no web root
* Usar permissões `chmod`/`chown` corretas

---

## 11: Atualizações e Manutenção

* Reiniciar a app após:

  * Alteração de variáveis de ambiente
  * Instalação de novos pacotes
* Apagar ambientes virtuais e logs antigos
* Fazer backup de ficheiros gerados por utilizadores

---

## 12: Tópicos adicionais (Opcional)

* Tarefas agendadas (cron jobs) em virtualenv
* Scripts Python em segundo plano (sem interface web)
* Geradores de sites estáticos (ex.: Pelican)

---

## 13: Recursos

* [Documentação cPanel: Setup Python App](https://docs.cpanel.net)
* [Documentação CloudLinux Python Selector](https://docs.cloudlinux.com/)
* Documentação oficial do [Python](https://docs.python.org/3/), [Flask](https://flask.palletsprojects.com/en/stable/), [FastAPI](https://fastapi.tiangolo.com/), [Django](https://docs.djangoproject.com/en/5.2/)

---


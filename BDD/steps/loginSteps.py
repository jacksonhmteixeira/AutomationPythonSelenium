import time
from behave import *
from Page.Login import Login

@Given(u'que estou na tela de login')
def login_page(context):
    context.Login = Login()
    context.Login.abrirNavegadorLogin()

@When(u'eu preencher o campo email com {email}')
def preencher_email(context, email):
    context.Login.preencherEmail(email)

@When(u'preencher o campo senha com {senha}')
def preencher_senha(context, senha):
    context.Login.preencherSenha(senha)

@When(u'clicar no botao ENTRAR')
def clicar_botao_entrar(context):
    context.Login.clicarBotaoEntrar()

@Then(u'o sistema vai direcionar para')
def verificar_pagina_painel(context):
    time.sleep(3)
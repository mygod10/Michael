#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o currículo em PDF de Michael Nunes.
Alterações futuras: edite os textos abaixo e rode `python3 gerar_curriculo.py`.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

AZUL = HexColor("#1a4e8a")
CINZA = HexColor("#444444")
PRETO = HexColor("#222222")
LINHA = HexColor("#d9d9d9")

LARG, ALT = A4  # 595x842 pt
MARGEM = 50
LARGUTIL = LARG - 2 * MARGEM

pdf = canvas.Canvas("curriculo-michael-nunes.pdf", pagesize=A4)
pdf.setTitle("Curriculo - Michael Nunes")
pdf.setAuthor("Michael Nunes")


def texto(x, y, s, fonte="Helvetica", tam=9.5, cor=PRETO):
    pdf.setFont(fonte, tam)
    pdf.setFillColor(cor)
    pdf.drawString(x, y, s)


def linha_divisoria(y):
    pdf.setStrokeColor(LINHA)
    pdf.setLineWidth(0.7)
    pdf.line(MARGEM, y, LARG - MARGEM, y)


def paragrafo(s, y, x=MARGEM, larg=LARGUTIL, fonte="Helvetica", tam=9.5, cor=PRETO, entrelinha=13):
    for lin in simpleSplit(s, fonte, tam, larg):
        texto(x, y, lin, fonte, tam, cor)
        y -= entrelinha
    return y


def secao(titulo, y):
    y -= 6
    texto(MARGEM, y, titulo.upper(), "Helvetica-Bold", 11, AZUL)
    y -= 4
    linha_divisoria(y)
    return y - 14


def bullet(s, y, larg=LARGUTIL - 14):
    y = paragrafo("•  " + s, y, MARGEM + 14, larg, entrelinha=12.5)
    return y


y = ALT - 55

# ===== Cabeçalho =====
texto(MARGEM, y, "MICHAEL NUNES", "Helvetica-Bold", 22, AZUL)
y -= 18
texto(MARGEM, y, "Product Builder | SaaS | UX/UI | Desenvolvimento Assistido por IA", "Helvetica", 10, CINZA)
y -= 16
contato = "(75) 98808-3538   •   maykon.nunes30@gmail.com   •   Cavunge - BA   •   goagendy.com   •   linkedin.com/in/michael-nunes-6910631b2/"
texto(MARGEM, y, contato, "Helvetica", 8.5, CINZA)
y -= 6

# Link clicável (e-mail e goagendy) — mantidos do original
pdf.linkURL("mailto:maykon.nunes30@gmail.com", rect=(MARGEM, y, LARG - MARGEM, y + 10))
y -= 10
linha_divisoria(y)
y -= 14

# ===== Perfil =====
y = secao("Perfil Profissional", y)
y = paragrafo(
    "Profissional com experiência em liderança, vendas, atendimento e operações, atualmente focado também na "
    "criação e evolução de produtos digitais. Uno visão de negócio, experiência do usuário e tecnologia para "
    "transformar problemas reais em soluções mais simples e organizadas. Utilizo o OpenAI Codex como ferramenta "
    "de apoio ao desenvolvimento, testes, análise e melhoria de sistemas.",
    y, entrelinha=13)
y -= 10

# ===== Projeto em destaque =====
y = secao("Projeto em Destaque", y)
texto(MARGEM, y, "GoAgendy", "Helvetica-Bold", 10.5)
pdf.linkURL("https://goagendy.com", rect=(MARGEM, y - 2, MARGEM + 60, y + 9))
texto(MARGEM + 62, y, "— Cofundador | Product Builder", "Helvetica", 9.5, CINZA)
y -= 12
y = paragrafo(
    "SaaS de gestão e agendamento - https://goagendy.com", y, tam=9, cor=CINZA, entrelinha=11.5)
y -= 2
y = paragrafo(
    "Participo da criação e evolução da GoAgendy, uma plataforma para empresas e profissionais de serviços. "
    "Minha atuação envolve definição de funcionalidades, UX/UI, organização de fluxos, testes, melhorias de "
    "experiência e desenvolvimento assistido por IA.",
    y, entrelinha=12.5)
y -= 6
y = bullet("Produto e experiência: definição de funcionalidades, fluxos, UX/UI, responsividade e melhoria contínua.", y)
y = bullet("Negócio: visão comercial, necessidades do cliente, processos e experiência de uso.", y)
y = bullet("Tecnologia: uso do OpenAI Codex como apoio na implementação, debugging, análise e refatoração de código.", y)
y -= 10

# ===== Experiência =====
y = secao("Experiência Profissional", y)

texto(MARGEM, y, "Supervisor de Operações", "Helvetica-Bold", 10.5)
pdf.drawRightString(LARG - MARGEM, y, "Atento - Feira de Santana/BA")
y -= 12
y = paragrafo(
    "Progressão interna na Atento: iniciei como Operador, fui promovido a Assistente de Vendas e, em seguida, "
    "a Supervisor de Operações.", y, tam=9, cor=CINZA, entrelinha=11.5)
y = paragrafo(
    "Liderança de equipes, acompanhamento de KPIs e metas, desenvolvimento de colaboradores, treinamento, "
    "engajamento e melhoria de processos.",
    y, entrelinha=12.5)
y -= 12

texto(MARGEM, y, "Líder do Setor Comercial", "Helvetica-Bold", 10.5)
y -= 12
y = paragrafo(
    "Clínica Prodent — Gestão da equipe comercial, acompanhamento de metas e indicadores de conversão, "
    "estratégias de vendas, retenção de clientes e treinamento da equipe.",
    y, entrelinha=12.5)
y -= 12

texto(MARGEM, y, "Operador", "Helvetica-Bold", 10.5)
y -= 12
y = paragrafo(
    "DAS - Santo Estêvão/BA — Atuação em rotinas operacionais, cumprimento de processos e suporte à operação.",
    y, entrelinha=12.5)
y -= 10

# ===== Formação e competências =====
y = secao("Formação e Competências", y)
texto(MARGEM, y, "FORMAÇÃO", "Helvetica-Bold", 9.5, AZUL)
y -= 12
y = paragrafo("Tecnologia da Informação — Estácio", y, entrelinha=12)
y -= 8
texto(MARGEM, y, "CURSOS E BASE TÉCNICA", "Helvetica-Bold", 9.5, AZUL)
y -= 12
y = bullet("Lógica de Programação", y)
y = bullet("Desenvolvimento e Estruturação de Sistemas", y)
y = bullet("Informática Avançada e Pacote Office", y)
y = bullet("Hardware e Software", y)
y -= 8
texto(MARGEM, y, "PRINCIPAIS COMPETÊNCIAS", "Helvetica-Bold", 9.5, AZUL)
y -= 12
y = bullet("Product Thinking e SaaS", y)
y = bullet("UX/UI e experiência do usuário", y)
y = bullet("OpenAI Codex e desenvolvimento assistido por IA", y)
y = bullet("Liderança e gestão de pessoas", y)
y = bullet("Vendas, negociação e relacionamento", y)
y = bullet("Indicadores, processos e melhoria contínua", y)
y -= 14
linha_divisoria(y)
y -= 12
texto(MARGEM, y, "Michael Nunes - Currículo profissional", "Helvetica", 8, CINZA)
texto(LARG - MARGEM - 40, y, "CNH A e B", "Helvetica", 8, CINZA)
pdf.drawRightString(LARG - MARGEM, y, "CNH A e B")

pdf.save()
print("curriculo-michael-nunes.pdf gerado.")

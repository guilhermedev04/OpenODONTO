
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime, timedelta 
def create_image(valor, endereço, cpf, nome):
    now = datetime.now()
    tdy = now.strftime('%d-%m-%Y')
    vencimento = (datetime.now() + timedelta(3)).strftime('%d-%m-%Y')
    imagem = Image.open("bobo.png")
    draw = ImageDraw.Draw(imagem)
    font_type = ImageFont.truetype("arial.ttf", 18)
    draw.text((15,105),"OPEN ODONTO SA",(0,0,0), font=font_type)
    draw.text((15,150),tdy,(0,0,0), font=font_type)
    draw.text((886,59),vencimento,(0,0,0), font=font_type)
    draw.text((886,389),valor,(0,0,0), font=ImageFont.truetype("arial.ttf", 29))
    draw.text((15,455),f"NOME: {nome} CPF: {cpf}\nENDEREÇO: {endereço}",(0,0,0), font=ImageFont.truetype("arial.ttf", 14))

    imagem.save("bobo2.png")
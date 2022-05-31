import os

def formata_tamanho(tamanho):

    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')


caminho = "D:\Certificados-documentos\Documentos Luiz"
termo_procura = 'Luiz'

conta = 0

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print(f"Arquivo localizado: {arquivo}")
                print(f"Caminho: {caminho_completo}")
                print(f'Nome {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho em bytes: {tamanho}')
                print(f'Tamanho formatado: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print('Sem permissão')
            except FileNotFoundError as e:
                print('Não encontrado!')
            except Exception as e:
                print('Erro desconhecido: ', e)
    print()
    print(f'{conta} arquivo(s) encontrado(s).')

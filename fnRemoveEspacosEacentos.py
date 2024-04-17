import pandas as pd
import re

def remover_espacos_acentuacao(texto):
    # Remove espaços no início e no final da string
    texto = str(texto).strip()
    
    # Substitui múltiplos espaços entre palavras por um único espaço
    texto = re.sub(r'\s+', ' ', texto)
    
    # Remove espaços em branco extras no final do texto
    texto = texto.rstrip()
    
    # Remove espaço em branco após o último caractere, se houver
    texto = re.sub(r'\s+$', '', texto)
    
    # Dicionário para mapear caracteres acentuados para suas versões não acentuadas
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ẽ': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'ĩ': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'ũ': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ẽ': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Ĩ': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Ũ': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C'
    }
    
    # Substitui caracteres acentuados pelos equivalentes não acentuados
    for acento, sem_acento in acentos.items():
        texto = texto.replace(acento, sem_acento)
    
    return texto

# Caminho para o arquivo CSV
caminho_arquivo = 'C:/Users/amanda.nascimento_te/Desktop/teste/dados.csv'

# Tente ler o arquivo com a codificação 'utf-8' e, se falhar, tente 'latin1'
try:
    dados = pd.read_csv(caminho_arquivo, encoding='utf-8')
except UnicodeDecodeError:
    try:
        dados = pd.read_csv(caminho_arquivo, encoding='latin1')
    except Exception as e:
        print("Não foi possível ler o arquivo:", e)
        exit()

# Copiar o DataFrame original
dados_original = dados.copy()

# Aplicar a função para remover espaços, acentuação e múltiplos espaços em todas as colunas
dados = dados.apply(lambda x: x.map(remover_espacos_acentuacao) if x.dtype == "object" else x)

# Verificar se o DataFrame foi alterado
if dados.equals(dados_original):
    print("Não foram encontradas palavras para corrigir.")
else:
    palavras_corrigidas = sum([sum(dados[coluna] != dados_original[coluna]) for coluna in dados.columns])
    print("Correção bem-sucedida. Total de palavras corrigidas:", palavras_corrigidas)

    # Salvar o arquivo CSV sobrepondo o original
    dados.to_csv(caminho_arquivo, index=False)

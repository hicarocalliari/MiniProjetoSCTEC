def padroniza_genero(df):
    """
    Converte os códigos numéricos da coluna CL_EC, usando o .map para substituir 'F' por 'FEMININO','M' por 'MASCULINO'
    'F': 'FEMININO',
    'M': 'MASCULINO',

    Parâmetros:
        df: DataFrame contendo a coluna CL_GENERO
    Retorna:
        df['CL_GENERO'] atualizado
    
    """
    return df['CL_GENERO'].str.upper().map({'F':'FEMININO','M':'MASCULINO'})

def padroniza_estado_civil(df):
    """
    Converte os códigos numéricos da coluna CL_EC, usando um dicionário catalogando cada valor correspondente em str
    
    1 -> Casado ou união estável
    2 -> Divorciado
    3 -> Separado
    4 -> Solteiro
    5 -> Viúvo

    Parâmetros:
        df: DataFrame contendo a coluna CL_EC
    Retorna:
        df['CL_EC'] atualizado
    """

    dicionario = ({ 

        1: 'CASADO OU UNIÃO ESTÁVEL',
        2: 'DIVORCIADO',
        3: 'SEPARADO',
        4: 'SOLTEIRO',
        5: 'VIÚVO'

    })
    return df['CL_EC'].map(dicionario)
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
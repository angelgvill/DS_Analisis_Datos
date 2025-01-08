import pandas as pd

class Display(object):
    """Mostrar la representación HTML de varios objetos"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    
    def __init__(self, *args, context=None):
        # Si no se pasa un contexto, se usa el entorno local por defecto
        if context is None:
            context = globals()
        
        # Convertir los nombres de variables a objetos reales si son cadenas
        self.args = [eval(a, context) if isinstance(a, str) else a for a in args]
        self.arg_names = [a if isinstance(a, str) else repr(a) for a in args]
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(name, obj._repr_html_())
                         for name, obj in zip(self.arg_names, self.args))
    
    def __repr__(self):
        return '\n\n'.join(name + '\n' + repr(obj)
                           for name, obj in zip(self.arg_names, self.args))
    
def ini_inspec(df):
    # Tamaño y estructura de los datos
    print("=== TAMAÑO Y ESTRUCTURA DE LOS DATOS ===")
    print(f"Número total de registros (filas): {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    print(f"Uso de memoria: {df.memory_usage().sum() / 1024:.2f} KB")
    print("\n")

    # Tipos de datos y nombres de columnas
    print("=== TIPOS DE DATOS Y NOMBRES DE COLUMNAS ===")
    print(df.dtypes)
    print("\n")
    print("Información detallada del DataFrame:")
    print(df.info())
    print("\n")

    # Identificación de problemas iniciales
    print("=== IDENTIFICACIÓN DE PROBLEMAS INICIALES ===")
    print(f"Número de filas duplicadas: {df.duplicated().sum()}")
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    # Mostrar las primeras filas para verificar la estructura
    print("\nPrimeras filas del dataset:")
    print(df.head())

    # Mostrar las ultimas filas para verificar la estructura
    print("\nÚltimas filas del dataset:")
    print(df.tail(10))
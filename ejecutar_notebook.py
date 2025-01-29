import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Ruta al archivo .ipynb
notebook_path = r"C:\Users\ERBC\Desktop\curso henry\Analisis_evolutivo_NBA\Analisis_evolutivo_NBA\carga_ingesta_SQL.ipynb"

# Cargar el notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Ejecutar el notebook
# El ExecutePreprocessor es el encargado de ejecutar el notebook.
# timeout: Es el tiempo máximo (en segundos) que se permitirá que el notebook se ejecute. 
# Si el notebook tarda más que este tiempo, se detendrá. Por ejemplo, timeout=600 permite 10 minutos.

#kernel_name: Es el nombre del kernel de Jupyter que se utilizará para ejecutar el notebook.

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': r"C:\Users\ERBC\Desktop\curso henry\Analisis_evolutivo_NBA\Analisis_evolutivo_NBA"}})

print("Ejecutado correctamente")
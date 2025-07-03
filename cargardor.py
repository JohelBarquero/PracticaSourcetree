import pandas as pd
from tkinter import Tk, filedialog
import os

# Para trabajar con extensiones de archivo

class CargadorCSV:

    def cargar(self):
        # Se inicia y oculta la ventana principal de Tkinter
        root = Tk()
        root.withdraw()

        # Mostrar el diálogo para seleccionar archivo
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de datos",
            filetypes=[("Archivos CSV y Excel", "*.csv *.xls *.xlsx")]
        )

        # Si no se selecciona nada
        if not file_path:
            print("No se seleccionó ningún archivo.")
            return pd.DataFrame()

        try:
            # Se obtiene la extensión del archivo (.csv, .xlsx, etc.)
            extension = os.path.splitext(file_path)[1].lower()
            # Se carga el archivo según la extensión
            if extension == ".csv":
                df = pd.read_csv(file_path)
            elif extension in [".xls", ".xlsx"]:
                df = pd.read_excel(file_path)
            else:
                print(" Formato no soportado.")
                return pd.DataFrame()
            # Se muestra la confirmación y una vista previa del dataset

            print(f"Archivo cargado exitosamente: {file_path}")
            print(df.head())
            return df

        except Exception as e:
            print(f"️ Error al cargar el archivo: {e}")
            return pd.DataFrame()

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "86a1e27d-d407-45b9-9dfb-7908fbdd2c63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Protocolo asignado: Protocolo_2\n"
     ]
    }
   ],
   "source": [
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "# Cargar el modelo entrenado\n",
    "modelo = joblib.load('modelo_protocolo.pkl')\n",
    "\n",
    "# Función de inferencia\n",
    "def predecir_protocolo(datos_dict):\n",
    "    # Convertir entrada a DataFrame\n",
    "    df = pd.DataFrame([datos_dict])\n",
    "\n",
    "    # Codificar variables categóricas (ajustar según entrenamiento)\n",
    "    df['Procedencia'] = df['Procedencia'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3})\n",
    "    df['Manipulacion'] = df['Manipulacion'].map({'normal': 0, 'frágil': 1})\n",
    "    df['Temperatura'] = df['Temperatura'].map({'ambiente': 0, 'refrigerado': 1})\n",
    "\n",
    "    # Predecir\n",
    "    pred = modelo.predict(df)\n",
    "    return 'Protocolo_1' if pred[0] == 0 else 'Protocolo_2'\n",
    "\n",
    "# Ejemplo de uso\n",
    "if __name__ == '__main__':\n",
    "    muestra = {\n",
    "        'Embalaje': 2,\n",
    "        'Ancho': 60.0,\n",
    "        'Largo': 70.0,\n",
    "        'Alto': 65.0,\n",
    "        'Peso (kg)': 12.5,\n",
    "        'Procedencia': 'A',\n",
    "        'Manipulacion': 'normal',\n",
    "        'Temperatura': 'ambiente'\n",
    "    }\n",
    "    resultado = predecir_protocolo(muestra)\n",
    "    print(\"Protocolo asignado:\", resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39ddc91f-3f60-4333-bf46-64f6b768f417",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

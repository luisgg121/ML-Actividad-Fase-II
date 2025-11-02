{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fab482fe-7a24-400e-9df1-91007288a753",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "from pydantic import BaseModel\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Inicializar la aplicación\n",
    "app = FastAPI(title=\"API de Protocolo\")\n",
    "\n",
    "# Cargar el modelo entrenado\n",
    "modelo = joblib.load(\"modelo_protocolo.pkl\")\n",
    "\n",
    "# Definir el esquema de entrada (ajusta los campos a tu dataset real)\n",
    "class Muestra(BaseModel):\n",
    "    Embalaje: int\n",
    "    Ancho: float\n",
    "    Largo: float\n",
    "    Alto: float\n",
    "    Peso: float\n",
    "    Procedencia: str\n",
    "    Manipulacion: str\n",
    "    Temperatura: str\n",
    "\n",
    "@app.get(\"/\")\n",
    "def home():\n",
    "    return {\"mensaje\": \"API de predicción de protocolos activa\"}\n",
    "\n",
    "@app.post(\"/predict\")\n",
    "def predict(muestra: Muestra):\n",
    "    # Convertir a vector de entrada\n",
    "    features = [\n",
    "        muestra.Embalaje,\n",
    "        muestra.Ancho,\n",
    "        muestra.Largo,\n",
    "        muestra.Alto,\n",
    "        muestra.Peso,\n",
    "        muestra.Procedencia,\n",
    "        muestra.Manipulacion,\n",
    "        muestra.Temperatura\n",
    "    ]\n",
    "    data = np.array([features], dtype=object)\n",
    "\n",
    "    # Predicción\n",
    "    pred = modelo.predict(data)[0]\n",
    "    return {\"protocolo_asignado\": str(pred)}\n"
   ]
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

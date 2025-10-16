# 🚀 Guía de Instalación - AI Youtube Shorts Generator
## Python 3.10.11 | Windows & Linux | Sin Docker

---

## 📋 **Requisitos Previos**

### **1. Python 3.10.11**
Verifica que tienes Python 3.10.11 instalado:

```bash
python --version
# o
python3 --version
```

Si no lo tienes, descárgalo desde: https://www.python.org/downloads/release/python-31011/

---

### **2. FFmpeg** (OBLIGATORIO)

FFmpeg es esencial para el procesamiento de video y audio.

#### **Windows:**

**Opción A - Usando Chocolatey (Recomendado):**
```powershell
# Instalar Chocolatey si no lo tienes
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar FFmpeg
choco install ffmpeg
```

**Opción B - Manual:**
1. Descarga FFmpeg desde: https://github.com/BtbN/FFmpeg-Builds/releases
2. Extrae el archivo ZIP
3. Agrega la carpeta `bin` al PATH de Windows
4. Reinicia el terminal

**Verificar instalación:**
```powershell
ffmpeg -version
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install -y ffmpeg libsm6 libxext6 build-essential
```

#### **Linux (Fedora/RHEL):**
```bash
sudo dnf install -y ffmpeg libSM libXext gcc gcc-c++ make
```

#### **macOS:**
```bash
brew install ffmpeg
```

---

## 🔧 **Instalación Paso a Paso**

### **Paso 1: Clonar o Descargar el Proyecto**

```bash
cd C:\Users\jhuan\Downloads\IA-Generative\AI-Youtube-Shorts-Generator
```

---

### **Paso 2: Crear Entorno Virtual**

#### **Windows (PowerShell):**
```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Si hay error de ejecución de scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### **Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### **Linux/macOS:**
```bash
# Crear entorno virtual
python3.10 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

**Verificar que el entorno está activo:**
Deberías ver `(venv)` al inicio de tu línea de comando.

---

### **Paso 3: Actualizar pip**

```bash
python -m pip install --upgrade pip setuptools wheel
```

---

### **Paso 4: Instalar Dependencias**

```bash
pip install -r requirements-py310.txt
```

**Nota:** La instalación puede tardar 5-15 minutos dependiendo de tu conexión.

---

### **Paso 5: Instalar PyTorch (Opcional - Solo si tienes GPU NVIDIA)**

Si tienes una GPU NVIDIA y quieres acelerar la transcripción con Whisper:

```bash
# Para CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Para CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Si solo tienes CPU (sin GPU), las dependencias ya instaladas son suficientes.

---

### **Paso 6: Configurar API Key de OpenAI**

Crea un archivo `.env` en la raíz del proyecto:

#### **Windows:**
```powershell
New-Item -Path .env -ItemType File
notepad .env
```

#### **Linux/macOS:**
```bash
touch .env
nano .env
```

**Contenido del archivo `.env`:**
```env
OPENAI_API=tu_api_key_de_openai_aqui
```

**Obtener API Key:**
1. Ve a: https://platform.openai.com/api-keys
2. Crea una nueva API key
3. Cópiala y pégala en el archivo `.env`

---

## ✅ **Verificar Instalación**

### **1. Verificar Python y Entorno Virtual:**
```bash
python --version
# Debe mostrar: Python 3.10.11

which python  # Linux/macOS
where python  # Windows
# Debe apuntar a la carpeta venv
```

### **2. Verificar FFmpeg:**
```bash
ffmpeg -version
```

### **3. Verificar Dependencias:**
```bash
pip list | grep -E "faster-whisper|openai|moviepy|opencv|pytubefix"  # Linux/macOS
pip list | Select-String -Pattern "faster-whisper|openai|moviepy|opencv|pytubefix"  # Windows
```

### **4. Test Rápido:**
```bash
python -c "import cv2, moviepy.editor, faster_whisper, openai; print('✅ Todas las dependencias importadas correctamente')"
```

---

## 🎬 **Ejecutar el Proyecto**

```bash
python main.py
```

El programa te pedirá una URL de YouTube y comenzará el proceso.

---

## 🐛 **Solución de Problemas Comunes**

### **Error: "FFmpeg not found"**
- **Solución:** Asegúrate de que FFmpeg esté en el PATH
- **Windows:** Reinicia el terminal después de instalar FFmpeg
- **Linux:** Ejecuta `sudo apt install ffmpeg`

### **Error: "No module named 'cv2'"**
```bash
pip uninstall opencv-python opencv-python-headless
pip install opencv-python==4.7.0.72
```

### **Error: "CUDA not available" (solo si tienes GPU NVIDIA)**
- Verifica que tienes los drivers de NVIDIA actualizados
- Instala PyTorch con soporte CUDA (ver Paso 5)

### **Error: "OpenAI API key not found"**
- Verifica que el archivo `.env` existe
- Verifica que la variable se llama `OPENAI_API` (sin espacios)
- Asegúrate de que el archivo `.env` está en la raíz del proyecto

### **Error: "Permission denied" al descargar video**
- Crea la carpeta `videos` manualmente: `mkdir videos`

### **El video descargado no tiene audio**
- Reinstala FFmpeg
- Verifica: `ffmpeg -version`

---

## 📦 **Estructura de Archivos Esperada**

```
AI-Youtube-Shorts-Generator/
├── venv/                    # Entorno virtual (ignorar en git)
├── videos/                  # Videos descargados (crear si no existe)
├── Components/
│   ├── Edit.py
│   ├── FaceCrop.py
│   ├── LanguageTasks.py
│   ├── Speaker.py
│   ├── SpeakerDetection.py
│   ├── Transcription.py
│   └── YoutubeDownloader.py
├── models/
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000_fp16.caffemodel
├── .env                     # API Keys (no subir a git)
├── main.py
├── requirements-py310.txt
├── INSTALACION.md
└── README.md
```

---

## 🔄 **Desactivar Entorno Virtual**

Cuando termines de trabajar:

```bash
deactivate
```

---

## 💡 **Notas Importantes**

1. **Primera ejecución:** La primera vez que ejecutes el proyecto, Whisper descargará modelos (~150 MB)
2. **GPU vs CPU:** Con GPU NVIDIA la transcripción es 10-20x más rápida
3. **Costos OpenAI:** Cada video procesa aproximadamente 0.01-0.10 USD en API calls
4. **Memoria RAM:** Se recomienda mínimo 8GB de RAM, ideal 16GB
5. **Espacio en disco:** Los videos descargados y procesados pueden ocupar mucho espacio

---

## 📞 **Soporte**

Si encuentras problemas:
1. Verifica que todos los pasos se completaron correctamente
2. Revisa la sección "Solución de Problemas Comunes"
3. Consulta los logs de error completos
4. Abre un issue en el repositorio de GitHub

---

## ✨ **¡Listo para Crear Shorts!**

Ejecuta el proyecto:
```bash
python main.py
```

¡Disfruta creando contenido automático! 🎥🚀

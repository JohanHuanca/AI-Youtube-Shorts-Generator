# 🎬 Guía Completa de Instalación de FFmpeg
## Windows, Linux y macOS

---

## 🪟 **WINDOWS - Instalación Manual (Recomendada)**

### **Opción 1: Instalación Rápida desde GitHub (MÁS FÁCIL)** ⭐

#### **Paso 1: Descargar FFmpeg**

1. Ve a: **https://github.com/BtbN/FFmpeg-Builds/releases**
2. Busca la versión más reciente (ej: `ffmpeg-master-latest-win64-gpl.zip`)
3. Descarga el archivo que dice: **`ffmpeg-master-latest-win64-gpl.zip`**
   - Si tu sistema es de 32 bits (poco común), descarga `win32` en su lugar

#### **Paso 2: Extraer el Archivo**

1. Abre el archivo ZIP descargado
2. Extrae la carpeta completa a: `C:\ffmpeg`
   - Puedes usar cualquier ubicación, pero esta es más fácil de recordar
3. La estructura debería quedar así:
   ```
   C:\ffmpeg\
   ├── bin\
   │   ├── ffmpeg.exe
   │   ├── ffplay.exe
   │   └── ffprobe.exe
   ├── doc\
   └── presets\
   ```

#### **Paso 3: Agregar FFmpeg al PATH de Windows**

**Opción A - Con Interfaz Gráfica:**

1. Presiona `Win + R` y escribe: `sysdm.cpl` → Enter
2. Ve a la pestaña **"Opciones avanzadas"**
3. Haz clic en **"Variables de entorno"**
4. En **"Variables del sistema"** (sección inferior), busca la variable **"Path"** y selecciónala
5. Haz clic en **"Editar"**
6. Haz clic en **"Nuevo"**
7. Escribe: `C:\ffmpeg\bin`
8. Haz clic en **"Aceptar"** en todas las ventanas

**Opción B - Con PowerShell (como Administrador):**

```powershell
# Ejecutar PowerShell como Administrador
# Clic derecho en el menú inicio > Windows PowerShell (Administrador)

# Agregar FFmpeg al PATH
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\ffmpeg\bin", "Machine")

# Verificar
$env:Path -split ';' | Select-String ffmpeg
```

#### **Paso 4: Verificar la Instalación**

```powershell
# IMPORTANTE: Cierra y abre un NUEVO terminal PowerShell

# Verificar FFmpeg
ffmpeg -version

# Deberías ver algo como:
# ffmpeg version N-XXXXX-gXXXXXXX Copyright (c) 2000-2025 the FFmpeg developers
```

**Si sigue sin funcionar:**
```powershell
# Cerrar TODOS los terminales abiertos
# Reiniciar el sistema
# Abrir un nuevo PowerShell y probar de nuevo
```

---

### **Opción 2: Instalación desde FFmpeg.org (Oficial)**

#### **Paso 1: Descargar**

1. Ve a: **https://ffmpeg.org/download.html**
2. Haz clic en el logo de **Windows**
3. Elige uno de estos proveedores:
   - **gyan.dev** (Recomendado): https://www.gyan.dev/ffmpeg/builds/
   - **BtbN GitHub**: https://github.com/BtbN/FFmpeg-Builds/releases

#### **Desde gyan.dev:**
1. Descarga: **`ffmpeg-release-essentials.zip`** (más pequeño)
   - O **`ffmpeg-release-full.zip`** (completo)
2. Extrae a `C:\ffmpeg`
3. Sigue los pasos 3 y 4 de la Opción 1

---

### **Opción 3: Instalación con Chocolatey (Automática)**

Si tienes Chocolatey instalado:

```powershell
# Ejecutar PowerShell como Administrador
choco install ffmpeg -y

# Verificar
ffmpeg -version
```

**Instalar Chocolatey primero (si no lo tienes):**
```powershell
# PowerShell como Administrador
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Luego instalar FFmpeg
choco install ffmpeg -y
```

---

### **Opción 4: Instalación con Scoop (Alternativa)**

```powershell
# Instalar Scoop (si no lo tienes)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Instalar FFmpeg
scoop install ffmpeg

# Verificar
ffmpeg -version
```

---

### **Opción 5: Instalación con winget (Windows 11)**

```powershell
# Windows 11 / Windows 10 actualizado
winget install Gyan.FFmpeg

# Verificar (reiniciar terminal primero)
ffmpeg -version
```

---

## 🐧 **LINUX - Instalación**

### **Ubuntu / Debian / Linux Mint:**

```bash
# Actualizar repositorios
sudo apt update

# Instalar FFmpeg y dependencias
sudo apt install -y ffmpeg libsm6 libxext6 build-essential

# Verificar
ffmpeg -version
```

### **Fedora / RHEL / CentOS:**

```bash
# Habilitar repositorio RPM Fusion (si no está habilitado)
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

# Instalar FFmpeg
sudo dnf install -y ffmpeg libSM libXext gcc gcc-c++ make

# Verificar
ffmpeg -version
```

### **Arch Linux / Manjaro:**

```bash
# Instalar FFmpeg
sudo pacman -S ffmpeg

# Verificar
ffmpeg -version
```

### **Instalación Manual en Linux (desde código fuente):**

```bash
# Descargar desde FFmpeg.org
wget https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
tar xjvf ffmpeg-snapshot.tar.bz2
cd ffmpeg

# Compilar
./configure
make
sudo make install

# Verificar
ffmpeg -version
```

---

## 🍎 **macOS - Instalación**

### **Opción 1: Con Homebrew (Recomendada)**

```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar FFmpeg
brew install ffmpeg

# Verificar
ffmpeg -version
```

### **Opción 2: Con MacPorts**

```bash
# Instalar MacPorts primero desde: https://www.macports.org/install.php

# Instalar FFmpeg
sudo port install ffmpeg

# Verificar
ffmpeg -version
```

### **Opción 3: Descarga directa**

1. Descarga desde: https://evermeet.cx/ffmpeg/
2. Extrae el archivo
3. Mueve `ffmpeg` a `/usr/local/bin/`:
   ```bash
   sudo mv ffmpeg /usr/local/bin/
   sudo chmod +x /usr/local/bin/ffmpeg
   ```
4. Verifica: `ffmpeg -version`

---

## ✅ **Verificar que FFmpeg Funciona Correctamente**

### **Test Básico:**

```bash
# Ver versión
ffmpeg -version

# Ver información de un video (si tienes alguno)
ffmpeg -i video.mp4

# Ver codecs disponibles
ffmpeg -codecs

# Ver formatos disponibles
ffmpeg -formats
```

### **Test en Python:**

```python
import subprocess

# Verificar FFmpeg
try:
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
    print("✅ FFmpeg instalado correctamente:")
    print(result.stdout.split('\n')[0])
except FileNotFoundError:
    print("❌ FFmpeg no encontrado")
```

---

## 🐛 **Solución de Problemas Comunes**

### **Windows: "ffmpeg no se reconoce como comando"**

**Soluciones:**

1. **Verificar que FFmpeg está en la ubicación correcta:**
   ```powershell
   Test-Path C:\ffmpeg\bin\ffmpeg.exe
   # Debe devolver: True
   ```

2. **Verificar el PATH:**
   ```powershell
   $env:Path -split ';' | Select-String ffmpeg
   # Debe mostrar: C:\ffmpeg\bin
   ```

3. **Agregar manualmente al PATH de la sesión actual:**
   ```powershell
   $env:Path += ";C:\ffmpeg\bin"
   ffmpeg -version
   ```

4. **Reiniciar el terminal** (o mejor aún, reiniciar el sistema)

5. **Ejecutar FFmpeg con ruta completa:**
   ```powershell
   C:\ffmpeg\bin\ffmpeg.exe -version
   ```

### **Linux: "Permission denied"**

```bash
# Dar permisos de ejecución
sudo chmod +x /usr/local/bin/ffmpeg
```

### **macOS: "ffmpeg cannot be opened"**

```bash
# Permitir la ejecución (Seguridad de macOS)
xattr -d com.apple.quarantine /usr/local/bin/ffmpeg
```

### **Python: "FileNotFoundError: ffmpeg"**

1. Verifica que FFmpeg funciona en terminal: `ffmpeg -version`
2. Si funciona en terminal pero no en Python, reinicia VS Code
3. Verifica que estás usando el entorno virtual correcto
4. En Python, prueba usar la ruta completa:
   ```python
   # Windows
   ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
   
   # Linux/macOS
   ffmpeg_path = "/usr/local/bin/ffmpeg"
   ```

---

## 📊 **Comparación de Métodos de Instalación (Windows)**

| Método | Dificultad | Velocidad | Actualizaciones |
|--------|-----------|-----------|-----------------|
| **Manual (GitHub)** | ⭐⭐ Fácil | 🚀 Rápida | Manual |
| **Chocolatey** | ⭐ Muy Fácil | 🚀 Rápida | Automáticas |
| **Scoop** | ⭐ Muy Fácil | 🚀 Rápida | Automáticas |
| **winget** | ⭐ Muy Fácil | 🚀 Rápida | Automáticas |
| **FFmpeg.org** | ⭐⭐⭐ Media | 🐢 Lenta | Manual |

---

## 🎯 **Recomendaciones**

### **Para Windows:**
1. **Primera opción**: Manual desde GitHub (BtbN)
2. **Segunda opción**: Chocolatey (si ya lo tienes)
3. **Tercera opción**: winget (Windows 11)

### **Para Linux:**
- Usar el gestor de paquetes de tu distribución (`apt`, `dnf`, `pacman`)

### **Para macOS:**
- Usar Homebrew (es el estándar)

---

## 🔗 **Enlaces Útiles**

- **FFmpeg Oficial**: https://ffmpeg.org/
- **FFmpeg GitHub Builds**: https://github.com/BtbN/FFmpeg-Builds/releases
- **Gyan.dev (Windows)**: https://www.gyan.dev/ffmpeg/builds/
- **Documentación FFmpeg**: https://ffmpeg.org/documentation.html
- **Chocolatey**: https://chocolatey.org/
- **Homebrew**: https://brew.sh/

---

## 💡 **Después de Instalar FFmpeg**

Una vez que FFmpeg esté instalado y funcionando:

1. **Cierra todos los terminales abiertos**
2. **Abre un nuevo terminal**
3. **Verifica**: `ffmpeg -version`
4. **Continúa con la instalación del proyecto**:
   ```powershell
   # Windows
   .\setup.ps1
   
   # Linux/macOS
   ./setup.sh
   ```

---

## ✨ **¡Listo!**

Ahora estás listo para procesar videos con FFmpeg. 🎬🚀

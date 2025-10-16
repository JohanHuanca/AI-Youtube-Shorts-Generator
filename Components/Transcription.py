from faster_whisper import WhisperModel
import torch

def transcribeAudio(audio_path, language="auto"):
    """
    Transcribe audio usando Whisper.
    
    Args:
        audio_path: Ruta del archivo de audio
        language: Código de idioma ('es' para español, 'en' para inglés, 'auto' para detectar automáticamente)
    """
    try:
        print("🎤 Transcribiendo audio...")
        Device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"💻 Dispositivo: {Device}")
        
        # Usar modelo multilenguaje para soportar español
        model_name = "base" if language != "en" else "base.en"
        print(f"🤖 Cargando modelo Whisper: {model_name}")
        
        model = WhisperModel(model_name, device=Device)
        print("✅ Modelo cargado")
        
        # Auto-detectar idioma si es 'auto'
        if language == "auto":
            print("🌍 Detectando idioma automáticamente...")
            segments, info = model.transcribe(audio=audio_path, beam_size=5, max_new_tokens=128, condition_on_previous_text=False)
            detected_lang = info.language
            print(f"✅ Idioma detectado: {detected_lang}")
        else:
            print(f"🌍 Transcribiendo en idioma: {language}")
            segments, info = model.transcribe(audio=audio_path, beam_size=5, language=language, max_new_tokens=128, condition_on_previous_text=False)
        
        segments = list(segments)
        extracted_texts = [[segment.text, segment.start, segment.end] for segment in segments]
        
        print(f"✅ Transcripción completada: {len(extracted_texts)} segmentos")
        return extracted_texts
        
    except Exception as e:
        print(f"❌ Error en la transcripción: {type(e).__name__}")
        print(f"📋 Detalle: {str(e)}")
        return []

if __name__ == "__main__":
    audio_path = "audio.wav"
    transcriptions = transcribeAudio(audio_path)
    # print("Done")
    TransText = ""

    for text, start, end in transcriptions:
        TransText += (f"{start} - {end}: {text}")
    print(TransText)
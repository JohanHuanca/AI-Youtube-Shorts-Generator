from Components.YoutubeDownloader import download_youtube_video
from Components.Edit import extractAudio, crop_video
from Components.Transcription import transcribeAudio
from Components.LanguageTasks import GetHighlight
from Components.FaceCrop import crop_to_vertical, combine_videos

url = input("Enter YouTube video URL: ")
Vid= download_youtube_video(url)
if Vid:
    Vid = Vid.replace(".webm", ".mp4")
    print(f"Downloaded video and audio files successfully! at {Vid}")

    Audio = extractAudio(Vid)
    if Audio:

        # Transcribir con auto-detección de idioma
        # Puedes cambiar 'auto' por 'es' (español) o 'en' (inglés) si lo prefieres
        transcriptions = transcribeAudio(Audio, language="auto")
        if len(transcriptions) > 0:
            TransText = ""

            for text, start, end in transcriptions:
                TransText += (f"{start} - {end}: {text}")

            start , stop = GetHighlight(TransText)
            # Verificar que el highlight sea válido
            # start puede ser 0 (video comienza desde el inicio)
            # stop debe ser mayor que start y ambos deben ser >= 0
            if start >= 0 and stop > 0 and stop > start:
                print(f"\n✂️  Recortando video: {start}s - {stop}s")
                print(f"📏 Duración del highlight: {stop-start} segundos")

                Output = "Out.mp4"

                crop_video(Vid, Output, start, stop)
                croped = "croped.mp4"

                crop_to_vertical("Out.mp4", croped)
                combine_videos("Out.mp4", croped, "Final.mp4")
            else:
                print("\n❌ Error: No se pudo obtener un highlight válido")
                print(f"📊 Valores recibidos: start={start}s, stop={stop}s")
                print("⚠️  Verifica que:")
                print("   - La transcripción tenga contenido válido")
                print("   - El video tenga al menos 10 segundos de duración")
                print("   - Tu API Key de OpenAI tenga créditos disponibles")
        else:
            print("No transcriptions found")
    else:
        print("No audio file found")
else:
    print("Unable to Download the video")
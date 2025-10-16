import cv2
import numpy as np
from moviepy.editor import *
from Components.Speaker import detect_faces_and_speakers, Frames
global Fps

def crop_to_vertical(input_video_path, output_video_path):
    print("\n📱 Iniciando conversión a formato vertical...")
    detect_faces_and_speakers(input_video_path, "DecOut.mp4")
    
    print("📐 Recortando video a formato 9:16 (vertical)...")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(input_video_path, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print("❌ Error: No se pudo abrir el video.")
        return

    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    vertical_height = int(original_height)
    vertical_width = int(vertical_height * 9 / 16)
    print(f"📊 Resolución: {original_width}x{original_height} → {vertical_width}x{vertical_height}")


    if original_width < vertical_width:
        print("Error: Original video width is less than the desired vertical width.")
        return

    x_start = (original_width - vertical_width) // 2
    x_end = x_start + vertical_width
    half_width = vertical_width // 2

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (vertical_width, vertical_height))
    global Fps
    Fps = fps
    
    count = 0
    last_valid_face = None
    last_centerX = None
    
    print(f"⏳ Procesando {total_frames} frames a {fps:.1f} FPS...")
    print(f"📊 Frames con detección de hablantes: {len(Frames)}")
    
    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            print(f"\n⚠️  No se pudo leer el frame {count}")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if len(faces) > -1 and len(faces) > 0:
            # Pick the most relevant face: closest to previous center or largest
            if last_centerX is not None:
                best_face = min(faces, key=lambda f: abs((f[0] + f[2] // 2) - last_centerX))
            else:
                best_face = max(faces, key=lambda f: f[2] * f[3])
            (x, y, w, h) = best_face
            last_valid_face = (x, y, w, h)
            # Center the crop window on the detected face's center
            centerX = x + w // 2
            # Optional: smoothing (simple moving average)
            if last_centerX is not None:
                centerX = int(0.7 * last_centerX + 0.3 * centerX)
            last_centerX = centerX
            x_start = max(0, min(centerX - vertical_width // 2, original_width - vertical_width))
            x_end = x_start + vertical_width
        else:
            # Fallback: center crop (no face detected or not sure)
            x_start = (original_width - vertical_width) // 2
            x_end = x_start + vertical_width
            last_centerX = None  # Reset smoothing when fallback

        # Only check for active face if Frames[count] is valid
        # Verificar que count no exceda el tamaño de Frames
        if count < len(Frames) and Frames[count] is not None and isinstance(Frames[count], (list, tuple)) and len(Frames[count]) == 4:
            (X, Y, W, H) = Frames[count]
        elif last_valid_face is not None:
            (X, Y, W, H) = last_valid_face
        else:
            X = x_start
            Y = 0
            W = vertical_width
            H = vertical_height

        # Inicializar variables por defecto (en caso de que no se detecten caras)
        x, y, w, h = X, Y, W, H
        
        # Buscar la cara activa dentro del área detectada
        for f in faces:
            x1, y1, w1, h1 = f
            center = x1 + w1//2
            if center > X and center < X+W:
                x = x1
                y = y1
                w = w1
                h = h1
                break

        # Calcular el centro de la cara
        centerX = x + (w//2)
        # print(centerX)  # Comentado para evitar spam
        # print(x_start - (centerX - half_width))  # Comentado para evitar spam
        
        # Ajustar el recorte basado en la posición de la cara
        if count == 0:
            # Primer frame: usar posición inicial
            pass
        elif (x_start - (centerX - half_width)) < 1:
            # Si el cambio es mínimo, mantener posición anterior
            pass
        else:
            # Ajustar la posición del recorte para seguir la cara
            x_start = centerX - half_width
            x_end = centerX + half_width

        count += 1
        
        # Mostrar progreso cada 30 frames
        if count % 30 == 0:
            progress = (count / total_frames) * 100
            print(f"⏳ Recortando: {count}/{total_frames} frames ({progress:.1f}%)", end='\r')
        
        # Realizar el recorte
        cropped_frame = frame[:, x_start:x_end]
        
        # Validar que el recorte sea válido
        if cropped_frame.shape[1] == 0 or cropped_frame.shape[1] != vertical_width:
            # Si el recorte no es válido, usar recorte centrado
            x_start = (original_width - vertical_width) // 2
            x_end = x_start + vertical_width
            cropped_frame = frame[:, x_start:x_end]
        
        # print(cropped_frame.shape)  # Comentado para evitar spam

        out.write(cropped_frame)

    cap.release()
    out.release()
    print(f"\n✅ Recorte completado: {count} frames procesados")
    print(f"📁 Video guardado en: {output_video_path}")



def combine_videos(video_with_audio, video_without_audio, output_filename):
    try:
        print("\n🔊 Combinando video con audio...")
        # Load video clips
        clip_with_audio = VideoFileClip(video_with_audio)
        clip_without_audio = VideoFileClip(video_without_audio)

        audio = clip_with_audio.audio

        combined_clip = clip_without_audio.set_audio(audio)

        global Fps
        print(f"💾 Guardando video final...")
        combined_clip.write_videofile(output_filename, codec='libx264', audio_codec='aac', fps=Fps, preset='medium', bitrate='3000k')
        print(f"\n🎉 ¡Video final guardado exitosamente!")
        print(f"📁 Archivo: {output_filename}")
    
    except Exception as e:
        print(f"Error combining video and audio: {str(e)}")



if __name__ == "__main__":
    input_video_path = r'Out.mp4'
    output_video_path = 'Croped_output_video.mp4'
    final_video_path = 'final_video_with_audio.mp4'
    detect_faces_and_speakers(input_video_path, "DecOut.mp4")
    crop_to_vertical(input_video_path, output_video_path)
    combine_videos(input_video_path, output_video_path, final_video_path)




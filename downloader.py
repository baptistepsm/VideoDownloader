import pytube as youtube_dl
from moviepy.editor import *


def convert_file(video, resolution):
    stream = video.streams.filter(progressive=False, file_extension='mp4', res=resolution).first()
    audio = video.streams.get_audio_only()
    audio_file = audio.download()
    video_file = stream.download()
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f'{video.title}.mp4', codec="libx264", audio_codec="aac")

def select_format(resolution, video):
    stream = video.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
    if stream is None:
        convert_file(video, resolution)
    else:
        return stream


def download_video(url, resolution):
    # Récupération de la vidéo
    video = youtube_dl.YouTube(url)
    # Récupération de la meilleure résolution disponible
    if resolution == 'mp3_Audio':
        stream = video.streams.get_audio_only()
        output_directory = stream.download()
        video_title = video.title
    elif resolution == '360p' or resolution == '480p' or resolution == '720p' or resolution == '1080p':
        stream = select_format(resolution, video)
        output_directory = stream.download()
        video_title = video.title
    else:
        raise ValueError('Résolution non supportée.')

    return output_directory, video_title

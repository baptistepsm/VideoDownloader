import yt_dlp as youtube_dl


# Fonction de téléchargement de vidéo
def download_video(url, resolution):
    # Récupération du titre de la vidéo
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(url, download=False)
    title = result['title']

    # Récupération de la résolution demandée
    if resolution == '360p':
        ydl_opts = {
            'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
            'outtmpl': f'{title}.mp4'
        }
    elif resolution == '480p':
        ydl_opts = {
            'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            'outtmpl': f'{title}.mp4'
        }
    elif resolution == '720p':
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'outtmpl': f'{title}.mp4'
        }
    elif resolution == '1080p':
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': f'{title}.mp4'
        }
    elif resolution == 'mp3_Audio':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{title}.mp3'
        }
    else:
        raise ValueError('Résolution non supportée.')

    # Téléchargement de la vidéo
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f'{title}.mp4'

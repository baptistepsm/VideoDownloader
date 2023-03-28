import os


def save_video(video_name, save_directory):
    # Récupération du nom du fichier à partir du chemin d'accès
    video_file_name = os.path.basename(video_name)

    # Création du chemin d'accès complet du fichier de sortie
    output_file_path = os.path.join(save_directory, video_file_name)

    # Vérification si le fichier de sortie existe déjà
    if os.path.exists(output_file_path):
        # Si le fichier existe déjà, on ajoute un suffixe numérique au nom du fichier pour éviter les doublons
        i = 1
        while os.path.exists(f'{output_file_path} ({i})'):
            i += 1
        output_file_path = f'{output_file_path} ({i})'

    # Renommage du fichier de téléchargement selon le format "ask_as_save"
    os.rename(video_name, output_file_path)

    return output_file_path

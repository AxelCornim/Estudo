from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os
from pathlib import Path
import re
import sys

# ======================= CONFIGURAÇÕES =======================
SAVE_PATH = r"C:\Users\Windows 11\Music\Musicas"  # Pasta para salvar os arquivos
# =============================================================

def clean_youtube_url(url):
    """Normaliza diferentes formatos de URL do YouTube"""
    patterns = [
        r'(https?://)?(www\.)?youtube\.com/watch\?v=([\w-]+)',
        r'(https?://)?youtu\.be/([\w-]+)',
        r'(https?://)?(www\.)?youtube\.com/playlist\?list=([\w-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            if 'playlist' in url:
                return f"https://www.youtube.com/playlist?list={match.group(4)}"
            else:
                video_id = match.group(3) if len(match.groups()) > 2 else match.group(2)
                return f"https://www.youtube.com/watch?v={video_id}"
    
    return url

def download_audio(url):
    """Processa uma URL individual"""
    try:
        cleaned_url = clean_youtube_url(url)
        
        # Processar playlists
        if 'playlist' in cleaned_url:
            playlist = Playlist(cleaned_url)
            print(f"\n🎵 Playlist: {playlist.title} ({len(playlist.videos)} vídeos)")
            
            for i, video in enumerate(playlist.videos, 1):
                print(f"\n▶️ [{i}/{len(playlist.videos)}] {video.title}")
                process_video(video.watch_url)
            
            print(f"\n🎉 Playlist completa baixada: {playlist.title}")
            return True
        
        # Processar vídeo individual
        return process_video(cleaned_url)
            
    except Exception as e:
        print(f"\n❌ ERRO: {str(e)}")
        return False

def process_video(url):
    """Processa um vídeo individual"""
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"\n🎵 Título: {yt.title}")
        print(f"👤 Autor: {yt.author}")
        print(f"⏱️ Duração: {yt.length // 60}:{yt.length % 60:02d} min")
        
        # Selecionar melhor stream de áudio
        audio_stream = yt.streams.filter(
            only_audio=True,
            file_extension='mp4'
        ).order_by('abr').desc().first()
        
        if not audio_stream:
            print("🚫 Nenhuma stream de áudio disponível")
            return False

        # Criar diretório se necessário
        Path(SAVE_PATH).mkdir(parents=True, exist_ok=True)
        
        # Download
        print("\n⬇️ Baixando...")
        output_file = audio_stream.download(output_path=SAVE_PATH)
        
        # Renomear para garantir extensão .mp4
        base, ext = os.path.splitext(output_file)
        if ext != '.mp4':
            new_file = base + '.mp4'
            os.rename(output_file, new_file)
            output_file = new_file
        
        # Resultado final
        file_size = os.path.getsize(output_file) // 1024
        print(f"\n✅ Salvo: {os.path.basename(output_file)}")
        print(f"📂 Tamanho: {file_size} KB")
        print(f"📁 Local: {output_file}")
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO: {str(e)}")
        return False

def batch_download():
    """Processa múltiplas URLs de um arquivo"""
    filename = 'urls.txt'
    if not os.path.exists(filename):
        print(f"\n❌ Arquivo {filename} não encontrado!")
        print("Crie um arquivo 'urls.txt' com uma URL por linha")
        return
    
    print("\n" + "=" * 50)
    print(" 🔁 MODO BATCH".center(50))
    print("=" * 50)
    
    with open(filename, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    print(f"📋 URLs encontradas: {len(urls)}")
    print("Iniciando downloads...\n")
    
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"\n🔁 [{i}/{len(urls)}] Processando: {url}")
        if download_audio(url):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"✅ CONCLUSÃO: {success_count}/{len(urls)} baixados com sucesso")
    print("=" * 50)

def show_banner():
    """Exibe o banner inicial"""
    print("\n" + "=" * 50)
    print(" 🎵 YOUTUBE AUDIO DOWNLOADER".center(50))
    print("=" * 50)
    print(f"📂 Pasta de destino: {SAVE_PATH}")
    print("=" * 50)

def main():
    """Função principal do programa"""
    # Menu principal
    while True:
        show_banner()
        
        print("\nMENU PRINCIPAL:")
        print("1. Baixar vídeo/playlist")
        print("2. Baixar lista de URLs (batch)")
        print("3. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        # Baixar vídeo/playlist individual
        if choice == '1':
            url = input("\nCole a URL do YouTube: ").strip()
            if url:
                download_audio(url)
            input("\nPressione Enter para continuar...")
        
        # Modo batch
        elif choice == '2':
            batch_download()
            input("\nPressione Enter para continuar...")
        
        # Sair
        elif choice in ['3', 'sair', 'exit']:
            print("\n🎶 Programa encerrado. Obrigado por usar!")
            break
        
        else:
            print("\n⚠️ Opção inválida!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário")
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {str(e)}")
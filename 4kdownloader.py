from pytubefix import YouTube
import random, string, os, ffmpeg

garis = "="*30

def hdDownloader():
    os.system("rm -rf output.mp4 output.m4a")
    os.system("clear")
    print("""┓┏┳┓  ┳┓       ┓ 
┣┫┃┃━━┃┃┏┓┓┏┏┏┓┃ 
┛┗┻┛  ┻┛┗┛┗┻┛┛┗┗┛""")
    print("""[
  download video youtube dengan
  durasi full atau hanya bagian
  tertentu berdasarkan menitnya

  download video + audio dengan
  resolusi yang tidak dibatasi
  secara gratis.
]""")
    print(garis)
    url = input("[??]. Masukkan url youtube lalu enter: ")
    yt = YouTube(url)
    ytmp3 = YouTube(url).streams.filter(only_audio=True, mime_type="audio/mp4").first().url
    dataRes = {}
    num = 0
    for st in yt.streams:
        if st.resolution and st.mime_type=="video/mp4":
            num += 1
            dataRes[str(num)] = st
    print(garis)
    print("[**]. Pilih resolusi dan fps")
    for key, value in dataRes.items():
        print(f"[{key}]. {value.resolution} {value.fps}fps")

    resC = str(int(input("[??]. Pilih resolusi: ")))
    ytmp4 = dataRes[resC].url
    print(garis)
    print("[**]. Pilih bagian yang ingin didownload lalu enter")
    print("[**]. Format hh:mm:ss")
    print("[**]. Contoh: 00:03:27")
    start = input("[??]. Start dari (hh:mm:ss): ")
    end = input("[??]. End sampai (hh:mm:ss): ")
    print(garis)
    print("[**]. Sedang mengunduh, tunggu sebentar..")
    ffmpeg.input(ytmp4, ss=start, to=end).output("output.mp4", vcodec="copy", acodec="copy").run()
    ffmpeg.input(ytmp3, ss=start, to=end).output("output.m4a", vcodec="copy", acodec="copy").run()
    print("[✓✓]. Selelai")
    print(garis)
    input("[✓✓] Video berhasil didownload, tekan enter untuk menyimpan")
    print("[**]. Sedang menyiapkan video, proses ini tidak menggunakan internet")
    inputVideo = ffmpeg.input("output.mp4")
    inputAudio = ffmpeg.input("output.m4a")
    ffmpeg.concat(inputVideo, inputAudio, v=1, a=1).output("outputFinal.mp4").run()
    os.system("rm -rf output.mp4 output.m4a")
    print(garis)
    print("[✓✓]. Selesai")
    print("[✓✓]. Video disimpan dengan nama outputFinal.mp4")

if __name__ == "__main__":
    hdDownloader()

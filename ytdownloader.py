from pytubefix import YouTube
from google.colab import files
import random, string, os

url = input("[??]. Masukkan url youtube lalu enter: ")
yt = YouTube(url)
ytmp3 = YouTube(url)
namaFileVideo = "".join(random.choice(f"{string.ascii_lowercase}{string.ascii_uppercase}") for n in range(10))
namaFileAudio = "".join(random.choice(f"{string.ascii_lowercase}{string.ascii_uppercase}") for n in range(10))
yt.title = namaFileVideo
ytmp3.title = namaFileAudio
dataRes = {}
num = 0
for st in yt.streams:
    if st.resolution and st.mime_type=="video/mp4":
        num += 1
        dataRes[str(num)] = st
print("\n[**]. Pilih resolusi dan fps")
for key, value in dataRes.items():
    print(f"[{key}]. {value.resolution} {value.fps}fps")

resC = str(int(input("[??]. Pilih resolusi lalu enter: ")))
print("[..]. Sedang mengunduh...")
print("[..]. Tunggu sebentar, proses ini tidak memakan kuota internet")
fileVideo = dataRes[resC].download(output_path="/content")
fileAudio = ytmp3.streams.filter(only_audio=True).first().download(output_path="/content")
os.system("rm -rf /content/outputTmp.mp4 /content/output.mp4")
os.system(f"ffmpeg -i {fileVideo} -i {fileAudio} -map 0:v -map 1:a -c:v copy -c:a copy -shortest /content/outputTmp.mp4")
os.system(f"rm -rf {fileVideo} {fileAudio}")
print("\n[**]. Pilih bagian yang ingin didownload lalu enter")
print("[**]. Format hh:mm:ss")
print("[**]. Contoh: 00:03:27\n")
start = input("[??]. Start dari (hh:mm:ss): ")
end = input("[??]. End sampai (hh:mm:ss): ")
os.system(f"ffmpeg -ss {start} -to {end} -i /content/outputTmp.mp4 -c copy /content/output.mp4")
os.system("rm -rf /content/outputTmp.mp4")

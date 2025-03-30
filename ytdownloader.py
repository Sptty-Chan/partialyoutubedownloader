from pytubefix import YouTube
import random, string, os

url = input("[??]. Masukkan url youtube lalu enter: ")
yt = YouTube(url)
namaFile = "".join(random.choice(f"{string.ascii_lowercase}{string.ascii_uppercase}") for n in range(10))
yt.title = namaFile
dataRes = {}
for num, st in enumerate(yt.streams):
    if st.resolution and st.mime_type=="video/mp4":
        dataRes[str(num + 1)] = st
print("\n[**]. Pilih resolusi dan fps")
for key, value in dataRes.items():
    print(f"[{key}]. {value.resolution} {value.fps}fps")

resC = str(int(input("[??]. Pilih resolusi lalu enter: ")))
print("[..]. Sedang mengunduh...")
print("[..]. Tunggu sebentar, proses ini tidak memakan kuota internet")
dataRes[resC].download(output_path="/content")

print("\n[**]. Pilih bagian yang ingin didownload lalu enter")
print("[**]. Format hh:mm:ss")
print("[**]. Contoh: 00:03:27\n")
start = input("[??]. Start dari (hh:mm:ss): ")
end = input("[??]. End sampai (hh:mm:ss): ")

os.system(f"ffmpeg -ss {start} -to {end} -i /content/{namaFile}.mp4 -c copy /content/output.mp4")

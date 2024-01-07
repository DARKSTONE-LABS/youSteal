import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
from threading import Thread

def download_video():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def on_download_click():
    Thread(target=download_video).start()

# Set up Tkinter window
root = tk.Tk()
root.title("youSteal")
root.configure(bg='black')

# Set window icon (assuming 'hacker.ico' is in the same directory)
root.iconbitmap('hacker.ico')

# URL Entry
tk.Label(root, text="Enter YouTube URL:", bg='black', fg='green').pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Download Button
download_button = tk.Button(root, text="Download Video", command=on_download_click, bg='green', fg='white', height=2, width=20)
download_button.pack(pady=10)

# Button style adjustments for a more squared look
download_button.config(font=("hack.otf", 12))

# Run the application
root.geometry("400x200")
root.mainloop()

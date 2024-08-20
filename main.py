import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from datetime import datetime
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

class SpotlistMDApp:
    def __init__(self, root):
        self.root = root
        root.title("SpotlistMD")
        root.geometry("600x400")

            # Set the icon
        icon_path = r"C:\Users\Owner\Documents\Github_Repositories\SpotlistMD\spotlistmd-icon.png"
        if os.path.exists(icon_path):
            icon = Image.open(icon_path)
            photo = ImageTk.PhotoImage(icon)
            root.wm_iconphoto(True, photo)

        self.style = ttk.Style()
        self.style.theme_use('equilux')  # You can change this to other themes like 'arc', 'breeze', etc.

        self.setup_ui()
        self.load_config()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="SpotlistMD", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=(0, 20))

        self.label = ttk.Label(main_frame, text="Export your Spotify playlists to a beautifully formatted Markdown file.", wraplength=500)
        self.label.pack(pady=10)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        self.fetch_button = ttk.Button(button_frame, text="Fetch Playlists", command=self.fetch_playlists, width=20)
        self.fetch_button.pack(side=tk.LEFT, padx=5)

        self.settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings, width=20)
        self.settings_button.pack(side=tk.LEFT, padx=5)

        self.progress_frame = ttk.Frame(main_frame)
        self.progress_frame.pack(fill=tk.X, pady=20)

        self.progress = ttk.Progressbar(self.progress_frame, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(side=tk.TOP, fill=tk.X)

        self.status_label = ttk.Label(self.progress_frame, text="")
        self.status_label.pack(side=tk.BOTTOM, pady=(5, 0))

        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(20, 0))

        version_label = ttk.Label(footer_frame, text="v1.0", font=("Helvetica", 8))
        version_label.pack(side=tk.LEFT)

        github_link = ttk.Label(footer_frame, text="GitHub", cursor="hand2", font=("Helvetica", 8, "underline"))
        github_link.pack(side=tk.RIGHT)
        github_link.bind("<Button-1>", lambda e: self.open_github())

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "config.json file not found. Please create one with your Spotify credentials.")
            self.root.quit()

    def fetch_playlists(self):
        try:
            self.status_label.config(text="Authenticating...")
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=self.config['SPOTIPY_CLIENT_ID'],
                client_secret=self.config['SPOTIPY_CLIENT_SECRET'],
                redirect_uri=self.config['SPOTIPY_REDIRECT_URI'],
                scope="playlist-read-private"
            ))

            self.status_label.config(text="Fetching playlists...")
            playlists = sp.current_user_playlists()
            total_playlists = len(playlists['items'])

            markdown_content = "# My Spotify Playlists\n\n"
            markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"

            for index, playlist in enumerate(playlists['items']):
                self.progress['value'] = (index + 1) / total_playlists * 100
                self.status_label.config(text=f"Processing playlist {index + 1} of {total_playlists}")
                self.root.update_idletasks()

                markdown_content += f"## {playlist['name']}\n\n"
                markdown_content += f"**Description:** {playlist['description']}\n\n"
                markdown_content += f"**Tracks:** {playlist['tracks']['total']}\n\n"

                markdown_content += "| # | Song | Artist | Album |\n"
                markdown_content += "|---|------|--------|-------|\n"

                tracks = sp.playlist_tracks(playlist['id'])
                for i, item in enumerate(tracks['items'], 1):
                    track = item['track']
                    song_name = track['name'].replace('|', '\\|')
                    artist_name = ', '.join([artist['name'] for artist in track['artists']]).replace('|', '\\|')
                    album_name = track['album']['name'].replace('|', '\\|')
                    markdown_content += f"| {i} | {song_name} | {artist_name} | {album_name} |\n"

                markdown_content += "\n\n"

            file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(markdown_content)

                self.status_label.config(text=f"Completed! File saved as {os.path.basename(file_path)}")
                messagebox.showinfo("Success", f"Markdown file '{os.path.basename(file_path)}' has been created.")
            else:
                self.status_label.config(text="Export cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")

        ttk.Label(settings_window, text="Spotify API Settings", font=("Helvetica", 16, "bold")).pack(pady=10)

        form_frame = ttk.Frame(settings_window, padding="20")
        form_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(form_frame, text="Client ID:").grid(row=0, column=0, sticky="w", pady=5)
        client_id_entry = ttk.Entry(form_frame, width=40)
        client_id_entry.grid(row=0, column=1, pady=5)
        client_id_entry.insert(0, self.config.get('SPOTIPY_CLIENT_ID', ''))

        ttk.Label(form_frame, text="Client Secret:").grid(row=1, column=0, sticky="w", pady=5)
        client_secret_entry = ttk.Entry(form_frame, width=40, show="*")
        client_secret_entry.grid(row=1, column=1, pady=5)
        client_secret_entry.insert(0, self.config.get('SPOTIPY_CLIENT_SECRET', ''))

        ttk.Label(form_frame, text="Redirect URI:").grid(row=2, column=0, sticky="w", pady=5)
        redirect_uri_entry = ttk.Entry(form_frame, width=40)
        redirect_uri_entry.grid(row=2, column=1, pady=5)
        redirect_uri_entry.insert(0, self.config.get('SPOTIPY_REDIRECT_URI', ''))

        def save_settings():
            self.config['SPOTIPY_CLIENT_ID'] = client_id_entry.get()
            self.config['SPOTIPY_CLIENT_SECRET'] = client_secret_entry.get()
            self.config['SPOTIPY_REDIRECT_URI'] = redirect_uri_entry.get()
            with open('config.json', 'w') as f:
                json.dump(self.config, f, indent=4)
            messagebox.showinfo("Success", "Settings saved successfully!")
            settings_window.destroy()

        save_button = ttk.Button(settings_window, text="Save", command=save_settings)
        save_button.pack(pady=20)

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/yourusername/SpotlistMD")

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = SpotlistMDApp(root)
    root.mainloop()
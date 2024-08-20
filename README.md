<img src="spotlistmd-icon.png" alt="SpotlistMD Icon" style="width: 150px; height: 150px; border-radius: 50%; display: block; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);" />


<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1f1f1f; color: #f5f5f5; line-height: 1.6; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">

<h1 style="color: #1db954; text-align: center;">SpotlistMD</h1>

<p style="text-align: center;">SpotlistMD is a user-friendly desktop application that allows Spotify users to easily export their entire playlist library into a beautifully formatted Markdown file. With just a single click, you can create a comprehensive document containing detailed information about each of your Spotify playlists.</p>

<h2 style="color: #1db954;">Features</h2>
<ul style="list-style: none; padding-left: 0;">
    <li style="margin-bottom: 10px;">✔ <strong>One-Click Export</strong>: Quickly fetch all your Spotify playlists and export them to a Markdown file.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Detailed Playlist Information</strong>: Includes playlist names, descriptions, and track counts.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Complete Track Listings</strong>: Each playlist export includes full track details (song title, artist, album).</li>
    <li style="margin-bottom: 10px;">✔ <strong>User-Friendly GUI</strong>: Clean and intuitive interface built with tkinter and ttkthemes.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Progress Tracking</strong>: Real-time progress bar and status updates during the export process.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Customizable Save Location</strong>: Choose where to save your exported Markdown file.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Secure Configuration</strong>: Spotify API credentials are stored securely in a local configuration file.</li>
    <li style="margin-bottom: 10px;">✔ <strong>Dark Mode</strong>: Sleek dark-themed interface for comfortable use in low-light environments.</li>
</ul>

<h2 style="color: #1db954;">Installation</h2>
<ol style="padding-left: 20px;">
    <li>Clone this repository:</li>
    <div style="background-color: #1c1c1c; padding: 15px; border-radius: 4px; margin: 10px 0;">
        <pre style="margin: 0; color: #dcdcdc;">git clone https://github.com/spragginsdesigns/SpotlistMD.git</pre>
    </div>
    <li>Navigate to the project directory:</li>
    <div style="background-color: #1c1c1c; padding: 15px; border-radius: 4px; margin: 10px 0;">
        <pre style="margin: 0; color: #dcdcdc;">cd SpotlistMD</pre>
    </div>
    <li>Install the required dependencies:</li>
    <div style="background-color: #1c1c1c; padding: 15px; border-radius: 4px; margin: 10px 0;">
        <pre style="margin: 0; color: #dcdcdc;">pip install -r requirements.txt</pre>
    </div>
</ol>

<h2 style="color: #1db954;">Configuration</h2>
<p>Before using SpotlistMD, you need to set up your Spotify API credentials:</p>
<ol style="padding-left: 20px;">
    <li>Go to the <a href="https://developer.spotify.com/dashboard/" target="_blank" style="color: #1db954;">Spotify Developer Dashboard</a> and create a new application.</li>
    <li>Copy your Client ID and Client Secret.</li>
    <li>Set the Redirect URI in your Spotify app settings (e.g., <code style="background-color: #1c1c1c; padding: 2px 4px; border-radius: 4px;">http://localhost:8888/callback</code>).</li>
    <li>Create a <code style="background-color: #1c1c1c; padding: 2px 4px; border-radius: 4px;">config.json</code> file in the project root with the following structure:</li>
</ol>

<div style="background-color: #1c1c1c; padding: 15px; border-radius: 4px; margin: 10px 0;">
    <pre style="margin: 0; color: #dcdcdc;">
{
  "SPOTIPY_CLIENT_ID": "your_client_id_here",
  "SPOTIPY_CLIENT_SECRET": "your_client_secret_here",
  "SPOTIPY_REDIRECT_URI": "your_redirect_uri_here"
}
    </pre>
</div>

<h2 style="color: #1db954;">Usage</h2>
<ol style="padding-left: 20px;">
    <li>Run the application:</li>
    <div style="background-color: #1c1c1c; padding: 15px; border-radius: 4px; margin: 10px 0;">
        <pre style="margin: 0; color: #dcdcdc;">python main.py</pre>
    </div>
    <li>Click the "Fetch Playlists" button to start the export process.</li>
    <li>Choose a save location for your Markdown file when prompted.</li>
    <li>Wait for the export to complete. You'll see a success message when it's done.</li>
</ol>

<h2 style="color: #1db954;">Contributing</h2>
<p>Contributions to SpotlistMD are welcome! Please feel free to submit a Pull Request.</p>

<h2 style="color: #1db954;">License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE" target="_blank" style="color: #1db954;">LICENSE</a> file for details.</p>

<h2 style="color: #1db954;">Acknowledgments</h2>
<p>Special thanks to:</p>
<ul style="list-style: none; padding-left: 0;">
    <li style="margin-bottom: 10px;">✔ <a href="https://spotipy.readthedocs.io/" target="_blank" style="color: #1db954;">Spotipy</a> for the excellent Spotify API wrapper.</li>
    <li style="margin-bottom: 10px;">✔ <a href="https://github.com/RedFantom/ttkthemes" target="_blank" style="color: #1db954;">ttkthemes</a> for the beautiful GUI themes.</li>
</ul>

<h2 style="color: #1db954;">Author</h2>
<p><strong>Austin Spraggins</strong></p>
<p>Website: <a href="https://spragginsdesigns.xyz" target="_blank" style="color: #1db954;">SpragginsDesigns.xyz</a></p>
<p>GitHub: <a href="https://github.com/spragginsdesigns" target="_blank" style="color: #1db954;">@spragginsdesigns</a></p>

<h2 style="color: #1db954;">Support</h2>
<p>If you encounter any problems or have any suggestions, please <a href="https://github.com/spragginsdesigns/SpotlistMD/issues" target="_blank" style="color: #1db954;">open an issue</a> on GitHub.</p>

<p style="text-align: center; font-style: italic; color: #8c8c8c;">SpotlistMD - Bringing your Spotify playlists to life in Markdown!</p>

</div>

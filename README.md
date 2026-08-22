# ugli-ferg

have u ever wanted to preview websites on a discord bot instead of opening a browser tab? no? well now you can

docker support too thank you chromium

### features

- save screenshots from strings, html files, and urls (/load_html, /load_html_file, /load_html_url)
- upload saved screenshots from filename (/get_image, /get_all_named_images)
- set resolution of screenshots (/set_image_size)

### usage

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository
   ```
   git clone https://github.com/ducky4life/ugli-ferg.git
   ```
2. move to directory
   ```
   cd ugli-ferg
   ```
3. install dependencies
   ```
   pip install -r requirements.txt
   ```
4. create .env file
   ```
   touch .env
   ```
5. put your secrets in the .env file (without the brackets: `[ ]`)
   ```
   FERG_TOKEN="[your bot token]"
   ```
6. make images directory
   ```
   mkdir images
   ```
7. run ferg.py
   ```
   python ferg.py
   ```

### todo

- [x] search images
- [ ] move images
- [ ] rename images
- [ ] temp file: remove command
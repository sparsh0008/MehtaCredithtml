import webbrowser


def main(path):
    pdf_file_path = path
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(pdf_file_path)

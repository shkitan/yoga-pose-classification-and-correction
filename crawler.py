from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
import sys
import base64
import time
from io import BytesIO
from PIL import Image
import ast
import os
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PARENT_DIR = "downward-facing dog"
POSE_NAME_DIR = "downward-facing dog"
IMAGE_PARENT_TAG_NAME = "h3"
IMAGE_TAG_NAME = "img"
OUTPUT = os.path.join(os.getcwd(), 'new_dataset')
MAX_EXAMPLES_FOR_CLASS = 50
JSON_FILE = "urls.json"
URL_SEPARATOR_TOKEN = "shkitan"

chromedriver = ChromeDriverManager().install()
keywords = {PARENT_DIR:[POSE_NAME_DIR]}
search_url = lambda keyword: 'https://www.google.com/search?q=' + keyword.replace(" ", "+") + '&source=lnms&tbm=isch'


def get_div_child(soup):
    """
     Extracts images from <h3> tags within a BeautifulSoup parsed HTML
     document.
     All of the image objects are under the <h3> tag
    :param soup: The BeautifulSoup parsed HTML document.
    :return: A list of BeautifulSoup objects representing images found
    """
    images = []
    time.sleep(0.3)
    for child in soup.recursiveChildGenerator():
        if child.name == IMAGE_PARENT_TAG_NAME:
            image = child.find_all(IMAGE_TAG_NAME)
            images.append(image)
    return images


def build_browser(search_url_obj):
    """
    Build a browser object a and pointer to the page body, of the search results.
    :param search_url_obj: The search url
    :return: the pointer to the body and browser object
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    try:
        browser = webdriver.Chrome(options=options)
    except Exception as e:
        print('No found chromedriver in this environment.')
        print('Install on your machine. exception: {e}')
        sys.exit()

    browser.set_window_size(1280, 1024)
    browser.get(search_url_obj)
    time.sleep(1)
    body = browser.find_element(By.TAG_NAME, "body")
    return body, browser


def download_urls(urls, output_path):
    """
    Download the images according to the given URL list
    :param urls: A list of the images urls
    :param output_path: The output path
    """
    count = 0
    if urls:
        for url in urls:
            try:
                image_data = base64.b64decode(url.split(',')[1])
                image_stream = BytesIO(image_data)
                image = Image.open(image_stream)
                image.save(output_path + 'img_' + str(count) + '.jpg')
                count += 1
            except Exception as e:
                print('Failed to write rawdata.')
                print(e)


def get_images(output_dir, parent_key, cur_key, search_url_obj, maximum, json_path):
    """
    Executes the search by the given keyword and downloads
    all the search images until the counter crosses the maximum.
    :param cur_key:
    :param json_path: json path
    :param parent_key: The parent_key data name
    :param output_dir: The path where the output should be stored
    :param search_url_obj: The url of the searching
    :param maximum: maximum number to be downloaded
    """
    body, browser = build_browser(search_url_obj)
    urls = []
    while len(urls) < maximum:
        try:
            for i in range(MAX_EXAMPLES_FOR_CLASS):
                scroll_down(body)
            page_source = browser.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            images = get_div_child(soup.body)
            urls += get_url_from_images(images)
        except ElementNotInteractableException:
            break
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    write_urls(json_path, parent_key, cur_key, urls)
    browser.close()


def scroll_down(body):
    """
    Scrolls down the web page by simulating the PAGE_DOWN key press.
    """
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)


def get_url_from_images(html_images):
    """
    Collect all the images url by an html images objects
    :param html_images: a list of the html objects represents the images
    :return: The images urls
    """
    urls = []
    for image in html_images:
        try:
            url = image[0].attrs.get("src")
            urls.append(url)
        except:
            continue
    return urls


def write_urls(path, parent_type, type, urls):
    """
    Writes URLs to a JSON file.
    :param path: The path to the JSON file.
    :param parent_type: The parent_key data name
    :param type: The sub_key data name
    :param urls: A list of URLs to write to the JSON file.
    """
    string_list = (URL_SEPARATOR_TOKEN.join(urls))
    data = dict()
    if os.path.isfile(path):
        with open(path, 'r') as fp:
            data = json.load(fp)
            data = ast.literal_eval(data)
    if parent_type not in data:
        data[parent_type] = dict()
    data[parent_type][type] = string_list
    with open(path, 'w') as fp:
        json.dump(str(data), fp)


def download_from_file(file_path, output_dir):
    """
    Downloads images from URLs stored in a JSON file.
    :param file_path: The directory where files will be downloaded.
    :param output_dir: the output dir
    """
    if os.path.isfile(file_path):
        with open(file_path, 'r') as fp:
            data = json.load(fp)
            data = ast.literal_eval(data)
    for key in keywords:
        for sub_key in keywords[key]:
            path = os.path.join(os.path.join(output_dir, key), sub_key)
            if not os.path.exists(path):
                os.makedirs(path)
            urls = data[key][sub_key]
            urls = urls.split(URL_SEPARATOR_TOKEN)
            download_urls(urls, path)


if __name__ == '__main__':
    for key in keywords:
        for sub_key in keywords[key]:
            path = os.path.join(os.path.join(OUTPUT, key),sub_key)
            get_images(path, key, sub_key, search_url(sub_key), MAX_EXAMPLES_FOR_CLASS, JSON_FILE)
    download_from_file(JSON_FILE, OUTPUT)
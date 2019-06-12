import pyautogui
import os


def convert_pdf_to_images(screen_size, out_dir, skip_first=0, num_pages=50, force=None):
    """
    If pdf is opened in chrome browser, define image region to take screenshot.
    The routine will:
      - click on the center of the region (to activate proper window)
      - take a screenshot and saves in output directory
      - sends right key to go to the next page

    :param screen_size: region on the screen to take screenshot
    :param out_dir: directory where resulting screenshots are saved
    :param skip_first: first page
    :param num_pages: number of screenshots to take
    :param force: if true, retake existing screenshot
    :return:
    """
    # check if output folder exists
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # click on the center of the region to activate chrome pdf viewer
    x_center = (screen_size[0] + screen_size[2]) / 2
    y_center = (screen_size[1] + screen_size[3]) / 2
    pyautogui.click(x=x_center, y=y_center, clicks=1, button='left')

    for page in range(num_pages):
        # skip first pages
        if skip_first > 0:
            for _ in range(skip_first):
                pyautogui.typewrite(['right'])

        out_file = os.path.join(out_dir, f"page_{page}.png")
        if not os.path.exists(out_file) or force:
            pyautogui.screenshot(out_file, region=screen_size)
            pyautogui.typewrite(['right'])


if __name__ == "__main__":
    horizontal_left = 160
    vertical_up = 400
    horizontal_right = 1150
    vertical_down = 1550
    screen_size = [horizontal_left, vertical_up, horizontal_right, vertical_down]
    out_dir = "images"
    convert_pdf_to_images(screen_size, out_dir, skip_first=0, num_pages=66, force=False)
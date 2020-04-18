# tkinter_image_demo.py
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import base64
import io
import matplotlib.image as mpimg
from skimage.io import imsave

db = []


def init_db():
    db.append({"name": "DFMWidget.png", "b64_string": ""})
    db.append({"name": "DFMWidgetSide.png", "b64_string": ""})
    db.append({"name": "DFMWidgetBackSide.png", "b64_string": ""})

    for image in db:
        fn = image["name"]
        b64str = image_file_to_b64("images/{}".format(fn))
        image["b64_string"] = b64str

    return


def image_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def b64_string_to_ndarray(b64_string):
    image_bytes = base64.b64decode(b64_string)
    image_buf = io.BytesIO(image_bytes)
    img_ndarray = mpimg.imread(image_buf, format='JPG')
    return img_ndarray


def ndarray_to_tkinter_image(img_ndarray):
    f = io.BytesIO()
    imsave(f, img_ndarray, plugin="pil")
    out_img = io.BytesIO()
    out_img.write(f.getvalue())
    img_obj = Image.open(out_img)
    tk_image = ImageTk.PhotoImage(img_obj)
    return tk_image


def get_new_image(image_to_find):
    for image in db:
        if image["name"] == image_to_find:
            b64_str = image["b64_string"]
            img_ndarray = b64_string_to_ndarray(b64_str)
            tk_image = ndarray_to_tkinter_image(img_ndarray)
            return tk_image


def main_window():

    def open_button_cmd():
        image_name = organ_choice.get()
        print("You've selected {}".format(image_name))
        tk_image = get_new_image(image_name)
        image_label.image = tk_image
        image_label.configure(image=tk_image)
        return

    root = Tk()

    select_label = ttk.Label(root, text="Select an image:")
    select_label.grid(column=0, row=0)

    organ_choice = StringVar()
    organ_choice_box = ttk.Combobox(root, textvariable=organ_choice)
    organ_choice_box.grid(column=1, row=0)
    organ_choice_box['values'] = ("DFMWidget.png", "DFMWidgetSide.png", "DFMWidgetBackSide.png")

    image_obj = Image.open("images/DFMWidget.png")
    image_obj = image_obj.resize((480, 300))
    tk_image = ImageTk.PhotoImage(image_obj)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=0, row=1, columnspan=2)

    open_button = ttk.Button(root, text="Open", command=open_button_cmd)
    open_button.grid(column=0, row=2, columnspan=2)

    root.mainloop()
    return


if __name__ == "__main__":
    init_db()
    main_window()

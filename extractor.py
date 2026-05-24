import fitz
import os
#
def extract_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    images = []

    os.makedirs("output_images", exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text()

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            img_path = f"output_images/page{page_num}_{img_index}.png"
            with open(img_path, "wb") as f:
                f.write(image_bytes)

            images.append(img_path)

    return text, images
import pdfplumber
pdf = pdfplumber.open('/Users/aryanraj/Downloads/lazarus/drylab.pdf')
page = pdf.pages[0]
images = page.images

for i, img in enumerate(images):

    img_obj = page.within_bbox((img['x0'], img['top'], img['x1'], img['bottom'])).to_image()

    img_obj.save(f"image_{i}.png")


text = page.extract_text()
print(text)
pdf.close()

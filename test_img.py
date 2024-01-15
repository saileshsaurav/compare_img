from PIL import Image, ImageChops


def test_img(image1, image2):
    path_image1 = image1
    path_image2 = image2
# Open Image1 in Photo viewer.
    img1 = Image.open(path_image1)
    img1.show()

# Save Image1 in JPG format.
    img3 = img1.save("image1.jpg")

    # Open Image2 in Photo viewer.
    img2 = Image.open(path_image2)
    img2.show()

    # Find the difference between the images.
    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        diff.show()
        print("Difference occurred at:" + str(diff))

        # Test fails as Assertion Error if images are different.
        assert diff.getbbox == diff
    else:
        diff.show()
        print("\n Images are same ")
        pass


test_img("image1.png", "image2.png")

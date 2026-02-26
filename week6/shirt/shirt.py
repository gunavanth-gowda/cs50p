import os
import sys
from PIL import Image
from PIL import ImageOps


def main():
    viable_formats = ["jpg", "png", "jpeg"]
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif (
        sys.argv[1].rsplit(
            ".",
        )[1]
        not in viable_formats
        or sys.argv[2].rsplit(
            ".",
        )[1]
        not in viable_formats
    ):
        print("Invalid input")
        sys.exit(1)
    elif (
        sys.argv[1].rsplit(
            ".",
        )[1]
        != sys.argv[2].rsplit(
            ".",
        )[1]
    ):
        print("Input and output have different extensions")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        transform(sys.argv[1], sys.argv[2])


def transform(input_image, output_image):
    shirt_image = Image.open("shirt.png")
    with Image.open(input_image) as image_file:
        input_cropped = ImageOps.fit(image_file, shirt_image.size)
        input_cropped.paste(shirt_image, mask=shirt_image)
        input_cropped.save(output_image)


if __name__ == "__main__":
    main()

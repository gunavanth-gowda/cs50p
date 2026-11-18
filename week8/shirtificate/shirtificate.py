from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.set_font("Helvetica", size=48)
    pdf.set_y(20)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")

    shirt_width = 190
    pdf.image("shirtificate.png", x=(pdf.w - shirt_width) / 2, y=60, w=shirt_width)

    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 120)
    pdf.cell(pdf.w - 20, 15, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

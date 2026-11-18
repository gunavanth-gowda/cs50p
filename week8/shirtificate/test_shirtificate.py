from pathlib import Path
import shutil
import subprocess
import sys

import pymupdf
import pytest


@pytest.fixture(params=["guna", "John Harvard", "Ada Lovelace"])
def shirtificate(request, tmp_path):
    project = Path(__file__).resolve().parent
    shutil.copy(project / "shirtificate.png", tmp_path)
    result = subprocess.run(
        [sys.executable, str(project / "shirtificate.py")],
        input=f"{request.param}\n",
        text=True,
        capture_output=True,
        cwd=tmp_path,
        check=True,
    )
    with pymupdf.open(tmp_path / "shirtificate.pdf") as pdf:
        yield request.param, result, pdf


def test_prompts_for_name(shirtificate):
    _, result, _ = shirtificate
    assert result.stdout == "Name: "
    assert result.stderr == ""


def test_single_a4_portrait_page(shirtificate):
    _, _, pdf = shirtificate
    assert len(pdf) == 1
    page = pdf[0]
    assert page.rect.width * 25.4 / 72 == pytest.approx(210, abs=0.1)
    assert page.rect.height * 25.4 / 72 == pytest.approx(297, abs=0.1)


def test_heading_image_and_white_name(shirtificate):
    name, _, pdf = shirtificate
    page = pdf[0]
    spans = [
        span
        for block in page.get_text("dict")["blocks"]
        if "lines" in block
        for line in block["lines"]
        for span in line["spans"]
    ]
    heading = next(span for span in spans if span["text"] == "CS50 Shirtificate")
    label = next(span for span in spans if span["text"] == f"{name} took CS50")
    images = page.get_image_info()
    assert len(images) == 1
    image_rect = pymupdf.Rect(images[0]["bbox"])
    heading_rect = pymupdf.Rect(heading["bbox"])
    label_rect = pymupdf.Rect(label["bbox"])

    for rect in (heading_rect, image_rect, label_rect):
        assert (rect.x0 + rect.x1) / 2 == pytest.approx(
            page.rect.width / 2, abs=1
        )
    assert heading_rect.y1 < image_rect.y0
    assert image_rect.contains(label_rect)
    assert label["color"] == 0xFFFFFF

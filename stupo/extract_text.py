import re

import fitz
import openai
import numpy as np
from openai import OpenAI

client = OpenAI(
)

pdf_path = './Lesefassung_BSc_Informatik-1-3.pdf'
pdf_document = fitz.open(pdf_path)

res_text = ""
for page in pdf_document:
    text = page.get_text("text")

    for text_line in text.splitlines():
        if text_line.endswith('-'):
            res_text += text_line[:-1]
        else:
            res_text += text_line + " "

pdf_document.close()
res_text = res_text.split("I. Allgemeiner Teil")[-1].strip()
pattern = r"§ \d+ -"
paragraphs = re.split(pattern, res_text)
paragraphs = [paragraph.strip() for paragraph in paragraphs if len(paragraph.strip()) > 0]

result_map = {}
for paragraph in paragraphs:

    underpoints = re.split(r"\(\d+\)", paragraph)
    for underpoint in underpoints:
        response = client.embeddings.create(
            input=underpoint.strip(),
            model="text-embedding-ada-002"
        )

        result_map[underpoint] = np.array(response.data[0].embedding)

np.savez('embeddings.npz', **result_map)

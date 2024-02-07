from bs4 import BeautifulSoup
import pyperclip
import re


def clean_html_tags(raw_html):
    cleantext = re.sub(re.compile("<.*?>"), "", raw_html)
    return cleantext


# Load HTML from the Proof file
with open(
    "C:\\Users\\Sarah\\Downloads\\Advanced Creative Writing Sample.html",
    "r",
    encoding="utf8",
) as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all <tw-passagedata> elements
passages = soup.find_all("tw-passagedata")

text_to_copy = ""
word_count_content = ""
word_count = 0

# Extract and accumulate the name and contents of each passage
for passage in passages:
    name = passage.get("name")
    content = passage.text.strip()

    res = len(re.findall(r"\w+", content))
    word_count += int(res)

    text_to_copy += (
        name + "\n" + content + "\n"
    )  # Add passage name and content to the accumulated text
    word_count_content += content

# Copy all the accumulated text to the clipboard
pyperclip.copy(text_to_copy)

to_remove = [
    "Advanced Creative Writing Sample",
    '<<back "←">',
    '<<linkreplace "',
    '" t8n>>',
    "<</linkreplace>>",
]

for t in to_remove:
    content = content.replace(
        t, ""
    )  # Replace with empty string to ensure complete removal

word_count_content = re.sub(r"\\\[", " [", word_count_content)
word_count_content = re.sub(r"\\\]", "] ", word_count_content)

word_count_content = clean_html_tags(word_count_content)

word_count_content = re.sub(r"[ ]+", " ", word_count_content)
word_count_content = re.sub(r">", "", word_count_content)
word_count_content = re.sub(r"\\", "", word_count_content)

word_count = len(word_count_content.strip().split())

print(f"Word Count: {word_count} words")

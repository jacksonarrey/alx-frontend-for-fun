#!/usr/bin/python3

import sys
import os.path
import markdown

def convert_markdown_to_html(md_file, html_file):
    with open(md_file, 'r') as file:
        markdown_content = file.read()

    html_content = markdown.markdown(markdown_content)

    with open(html_file, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":

  input_file = sys.argv[1]
  output_file = sys.argv[2]

  if len(sys.argv) < 3:
      print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
      sys.exit(1)
  else:
        input_md_file = sys.argv[1]
        output_html_file = sys.argv[2]
        convert_markdown_to_html(input_file, output_file)

  if not os.path.isfile(input_file):
      print(f"Missing {input_file}", file=sys.stderr)
      sys.exit(1)

  sys.exit(0)

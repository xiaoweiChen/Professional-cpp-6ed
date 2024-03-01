
part_num = 6
chapter_num = "D"
#chapter_file_prefix = f"content/part{part_num}/chapter{chapter_num}/"
chapter_file_prefix = f"content/part{part_num}/appendix-{chapter_num}/"
section_names = [
"Introduction to UML",
"DIAGRAM TYPES",
"CLASS DIAGRAMS",
"INTERACTION DIAGRAMS",
]

for index, name in enumerate(section_names):

  if index == 0:
    #line = fr"\mySection{{第{chapter_num}章}}{{{name}}}{{{chapter_file_prefix}{index}.tex}}"
    line = fr"\mySection{{附录{chapter_num}}}{{{name}}}{{{chapter_file_prefix}{index}.tex}}"
  else:
    words = name.split()
    real_name = ' '.join([word.capitalize() for word in words])
    line = fr"\mySubsection{{{chapter_num}.{index}.}}{{{real_name}}}{{{chapter_file_prefix}{index}.tex}}"

  print(line)
print(r"\newpage")

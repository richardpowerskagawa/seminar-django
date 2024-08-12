import re

pattern = re.compile(r'歩(?P<minuteonfoot_fromstation>[\d]+)分')

text = """駅から歩5分です。
歩10分です。
こちらは駅から歩3分です。
sdvdvvadva
oavadv
徒歩で15分かかります。"""

# Find all lines with matches
lines = text.split('\n')
matched_lines = []

for line in lines:
    if pattern.search(line):
        matched_lines.append(line)

# Output matched lines
for matched_line in matched_lines:
    print(matched_line)



# # Example string
# text = "駅から歩5分です。"

# # Search for the pattern in the text
# match = pattern.search(text)

# if match:
#     print(f"Minutes on foot from station: {match.group('minuteonfoot_fromstation')}")
# else:
#     print("No match found.")


# results = pattern.finditer("駅から歩5分です。歩10分です。")
# for match in results:
#     print(match.group('minuteonfoot_fromstation'))
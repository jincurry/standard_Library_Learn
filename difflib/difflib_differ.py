import difflib
from difflib_data import *

print("*"*60)
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))
print("*"*60)
diff = difflib.unified_diff(text1_lines, text2_lines, lineterm='')
print('\n'.join(diff))
print("*"*60)
diff = difflib.context_diff(text1_lines, text2_lines, lineterm='')
print('\n'.join(diff))

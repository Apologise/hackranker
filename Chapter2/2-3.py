setence = input('Please input your sentence:')

screen_width = 80
sen_length = len(sentence)
box_length = sen_length + 8
left_margin = (screen_width - box_length) // 2

print()
print(' '*left_margin+'+'+'-'*(box_length-2)+'+')
print(' '*(left_margin+4)+'|'+' '*text_width+' |')
print(' '*(left_margin+4)+'|'+sentence+' |')
print(' '*(left_margin+4)+'|'+' '*text_width+' |')
print(' '*left_margin+'+'+'-'*(box_length-2)+'+')
print()
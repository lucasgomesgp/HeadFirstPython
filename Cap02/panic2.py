phrase = "Don't panic!"
plist = list(phrase)

# plist = plist[1:8:1]
# plist.remove(' ')
# plist.remove("'")
# plist.insert(2,' ')
# plist.extend([plist.pop(),plist.pop()])
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])
print(new_phrase)
print(plist)

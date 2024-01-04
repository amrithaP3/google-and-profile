'''
from PIL import Image
image = Image.open("game.png")
image.save("newimage.png")
print(image)
'''

profile = open("new.html")
full = profile.read()
profile.close()
print(full)
#alist = profile.readlines()
#print(alist)

if 'class="hook"' in full:
    print("yes")
    words = "hi hi hi!!!"
    hook = '      "<h1 class="hook">' + words + '</h1>\n'
    changed = full.replace('      <h1 class="hook">Hello everyone! I\'m Amritha Pramod and I\'m just a girl who loves all things tech!</h1>\n', '      "<h1 class="hook">' + words + '</h1>\n')
    print(changed)

outfile = open("new.html", "w")
outfile.write(changed)
outfile.close()




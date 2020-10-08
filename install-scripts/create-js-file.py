import os
def bpm_createfile(filename, data):
  fil = open(filename + ".js", "w")
  fil.write(data)
  fil.close()
def bpm_deletefile(filename):
  if os.path.exists(filename + ".js"):
    os.remove(filename + ".js")

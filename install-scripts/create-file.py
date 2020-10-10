import os
def bpm_createfile(filename, data):
  fil = open("https://github.com/Brunozhon/bpm/install-scripts/" + filename, "w")
  fil.write(data)
  fil.close()
def bpm_deletefile(filename):
  if os.path.exists("https://github.com/Brunozhon/bpm/install-scripts/" + filename):
    os.remove("https://github.com/Brunozhon/bpm/install-scripts/" + filename)

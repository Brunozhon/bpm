def bpm_install(filename, crfilename):
  try:
    fil = open(filename + ".js", "r")  # Every BPM file is a javascript file, so add .js to the end
    f = open(crfilename + ".js", "w")  # Sets a file to writing mode
    f.write(fil.read())  # Write the readed file
  except:
    print("Failed to open file(s)")
  finally:
    try:
      fil.close() # Close files even if no error oucured
      f.close()
    except NameError:
      print("Varible 'fil' or 'f' is not defined")
    except:
      print("Something else went wrong, but it's not a NameError")

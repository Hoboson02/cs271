def strip(line):
# removes all excess values, such as comments and white space

  value = line[0]
  if value == "\n" or value == "/":
    return ""
  elif value == " ":
    return strip(line[1:])
  else:
    return value + strip(line[1:])
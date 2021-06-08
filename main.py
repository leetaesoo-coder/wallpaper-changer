from change_background import changeBackground

def main():
  
  changeBackground()
  
  print("\n\nDo You Hate Your Wallpaper?\n\n(for yes write 'y', for no write 'n')\n")
  
  answer = input("->")
  
  if answer == "n":
    return
  else: main()
  
main()
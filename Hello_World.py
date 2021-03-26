
if __name__ == "__main__":

  print("Hello World!")
  print("And Goodbye...")
  print("One more change")

  with open("filename.txt", 'w') as f:
    f.write("Testing Testing 1 2 3")
    f.write("This is the second line\n")
    f.write("Again")
    # print(f.read())
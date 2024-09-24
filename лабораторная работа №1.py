def is_palindrome(text):
  text = text.lower().replace(" ", "")
  return text == text[::-1]

text = input("Введите текст: ")
if is_palindrome(text):
  print("Это палиндром!")
else:
  print("Это не палиндром.")

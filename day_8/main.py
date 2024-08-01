from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





def caesar(input_text, shift_amount, direction):
  output_text = ""
  if direction == "decode":
    shift_amount *= -1
    
  for char in input_text:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = index + shift_amount
      if new_index > 25:
        new_index = new_index - 26
      output_text += alphabet[new_index]
      
    else:
      output_text += char
    
  print(f"The {direction}d text is {output_text}")




end_program = False

while not end_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(input_text=text, shift_amount=shift, direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    end_program = True
    print(f"Goodbye")

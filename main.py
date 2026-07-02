import tiktoken 

enc =  tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Ronit Raj"
Tokens = enc.encode(text)

decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 22848, 278, 40516])
print(Tokens)
print(decode)
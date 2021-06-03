import string
alphapet = string.ascii_lowercase
alphapet_list = list(alphapet)

message = input("message>").lower() #hello
message_list = list(message)
shift = int(input("shift>"))
print(message_list)
print(alphapet_list)
index_head = message[0]
index_last = message[-1]

print([index_head, index_last])
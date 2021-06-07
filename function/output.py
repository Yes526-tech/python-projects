# def maskify(cc):
#     last_list = []
#     last_list_str = ""
#     length = len(cc)
#     number_list = []
#     if length <= 4:
#         return cc
#     for num in range(length):
#         number_list += cc[num]
#     first_chars = number_list[:-4]
#     last_four_char = number_list[-4:]
#     for first_chars_item in first_chars:
#         for index in range(len(first_chars_item)):
#             last_list += "#"
#     for item in last_four_char:
#         last_list += item
#     for cencored in last_list:
#         last_list_str += cencored
#
#     return last_list_str
#
# def maskify(cc):
#
#     length = len(cc)
#         last_four = cc[-4:]
#         repeat = "#" * (length - 4)
#         return repeat + last_four
#     return cc

#  const maskify = (cc) => {
#   if (cc.length >= 4) {
#     const last4 = cc.substr(cc.length - 4);
#     const repeat = "*".repeat(cc.length - 4);
#     return repeat + last4;
#   }
#   return cc;
# };


# def maskify(cc):
#     list_letters = []
#     for letter in cc:
#         list_letters += letter
#     for item in list_letters:
#         position = list_letters.index(item)
#         square_item = list_letters[:position - 4]
#         list_letters += square_item
#     return print(list_letters)
# maskify("hello")
# def maskify(cc):
#     return "#"*(len(cc) - 4) + cc[-4:] if len(cc) >= 4 else cc
#
# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]
# def maskify(cc):
#     return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))
def maskify(cc):
    return print(len(cc[:-4])*"#" + cc[-4:])
maskify("1")
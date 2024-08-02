message = "Learning Python for Data Engineering"
notification = 'Saturdays are working'
print(message," ", notification)
#escape codes
escape_Codes = """
\n = new line feed
\r = carriage return
\t = Tab
\' = literal single quote
\" = literal double quote
\\ = literal backslash
"""
#message = 'Good Morning Friend\'s';
# print(escape_Codes)
#string indexing
message = "Learning Python for Data Engineering"
print("The character at position 6 is ", message[5])
#string Slicing
print("The string from the 9th Position:",message[9:])
print("The string till the 9th Position:",message[:9])
print("The string from the 9th Position till 15th Position:",message[9:15])
print("Last 5 characters from the striing:",message[-5:])
print("from 5th postion to len-3 position:",message[5:-3])
print("till len-3 position:",message[:-3])
print("length of string:",len(message))
print("reversal of string:",message[::-1])
print("no of 'in' in the message: ",message.count("in"))
print("upper case message: ",message.upper())
print("find position of 'in' in the message: ",message.find("in"))
print("find position of 'in' in the message from position 9: ",message.find("in",9))
print("find position of 'in' in the message from position 29 till 35: ",message.find("in",29,35))
print("split the message",message.split())
print("split the message",message.split("in"))

'''Recursive functions
----------------------
Recursion is a programming technique where a function calls itself either directly or
indirectly to solve a problem by breaking it into smaller, simpler subproblems.
it is especially useful for problems that can be divided into identical smaller tasks,
such as mathematical calculaions, tree traversals or divide-and-conquer algorithms.
'''

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("☑Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"✘Invalid PIN. Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked.Please contact customer care")
                return False
validate=int(input())
validate_pin(validate)


ok = input("Enter a string: ")
vowel_list = []
con_list = []
def vowel_con(ok,vowel_list,con_list ):
    for i in ok:
        if i in "aeiouAEIOU":
            vowel_list.append(i)
        else:
            con_list.append(i)
    print(f"{vowel_list} are the vowels in the string")
vowel_con(ok,vowel_list,con_list) 

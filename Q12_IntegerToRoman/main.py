class Solution(object):
    def intToRoman(self, num):
        val_sym_pairs = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
         
        roman = "" 

        for value,symbol in val_sym_pairs:
            while num >= value:
                roman += symbol
                num -= value

            return roman

if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer between 1 and 3999: "))
        if 1 <= user_input <= 3999:
            solution = Solution()
            result = solution.intToRoman(user_input)
            print("Roman numeral: ",result)
        
        else:
            print("Please enter a number in the range 1 to 3999.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
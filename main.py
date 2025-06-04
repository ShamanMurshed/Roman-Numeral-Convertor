while True:
    print("Accepted Numerals: I,V,X,L,C,D,M")
    roman = input("Enter a Roman Numeral or Stop: ")
    if roman.lower() == "stop":
        break
    def romanToInt(s: str) -> int:
        ans = 0

        def getValue(rom: str) -> int:
            if rom=="I":
                return 1
            if rom=="V":
                return 5
            if rom=="X":
                return 10
            if rom=="L":
                return 50
            if rom=="C":
                return 100
            if rom=="D":
                return 500
            if rom=="M":
                return 1000

        i = 0
        while i < len(s):
            if i == len(s)-1:
                ans += getValue(s[i])
                i+=1
            else:
                if getValue(s[i]) < getValue(s[i+1]):
                    ans += getValue(s[i+1]) - getValue(s[i])
                    i+=2
                else:
                    ans += getValue(s[i])
                    i+=1
        return ans

    print(f"Integer form of " + roman + " is " + str(romanToInt(roman)) + "\n")
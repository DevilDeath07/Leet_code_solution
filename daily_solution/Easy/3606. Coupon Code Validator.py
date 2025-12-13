class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result_bl = []
        result = []
        #assigning n value using code, businessLine and isActive list
        if len(code)==len(businessLine)==len(isActive):
            n = len(code)
        else:
            return result

        #create a function for validation our string is alphanumeric and also consist of underscore"_" in code list
        def calphanumric(string):
            if not string:        # empty string → False
                return False
            return string.replace("_", "").isalnum() or string.count("_") == len(string)

        #create a function for validation businessLine have all the evements are valid or not
        def cbLine(text):
            bline = ["electronics", "grocery", "pharmacy", "restaurant"]
            if text in bline:
                return True
            return False

            
        #validate the coupon code using validator function like calphanumeric(), cbLine()

        for i in range(n):
            if(calphanumric(code[i]) == True and cbLine(businessLine[i]) == True and isActive[i] == True):
                result.append(code[i])
                result_bl.append(businessLine[i])

        #sorted using priority map
        def sort_by_priority(code, businessLine):
            priority = {
                "electronics": 0,
                "grocery": 1,
                "pharmacy": 2,
                "restaurant": 3
            }

            result = []

            for i in range(len(code)):
                result.append((priority[businessLine[i]], code[i]))

            result.sort()  # sorts by priority first, then code

            return [item[1] for item in result]

        return sort_by_priority(result,result_bl)

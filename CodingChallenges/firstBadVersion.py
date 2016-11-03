# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(versions, n):
        lengthofversion = len(versions)

        left = 0
        right = lengthofversion - 1
        if (n > versions[right] or n< versions[left]):
            return "Not present in given range"
            
        
        while(right > left):
            mid = (left + right)/2
            if (n == versions[mid]):
                return "Found", n
            elif (n > versions[mid]):
                left = mid+1
                
            elif (n < versions[mid]):
                right = mid
            else:
                return "Not Found"
        
        


anwer = firstBadVersion([1,2,3,4,5,6,7,8,9,10],4)
print anwer
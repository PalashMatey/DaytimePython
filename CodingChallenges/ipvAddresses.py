def isIP(IP):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if '.' in IP:
            count = 0 
            for num in IP.split('.'):
                if len(num) > 1:
                    if int(num) >= 0 and int(num) < 256:
                        count += 1
                    else:
                        return "Neither"
                else:
                        count += 1
               
            if count == 4:
                return "IPV4"
        if ':' in IP:
            count = 0
            for num in IP.split(':'):
                if len(num) == 0:
                    return 'Neither'
                elif len(num) == 4:
                    count += 1
                elif int(num) == 0:
                    count += 1
                else:
                    return 'Neither'
            if count == 8:
                return 'IPV6'

answer = isIP("2001:0db8:85a3::0000:8A2E:0370:7334")
print answer    
                    
                



def isIP(IP):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def is_hex(s):
            hex_digits = set(a,b,c,d,e,f,A,B,C,D,E,F,0,1,2,3,4,5,6,7,8,9)
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
            
        ary = IP.split('.')
        if len(ary) == 4:
            for i in xrange(len(ary)):
                if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]>1)):
                    return "Neither"
            return "IPv4"
            
        ary = IP.split(':')
        if len(ary) == 8:
            for i in xrange(len(ary)):
                temp = ary[i]
                if len(temp) == 0 or not len(temp) <= 4 or not is_hex(temp) :
                    return "Neither"
            return "IPv6"
        return "Neither"
            
        # if '.' in IP:
        #     count = 0 
        #     for num in IP.split('.'):
        #         if len(num) > 1:
        #             if int(num) >= 0 and int(num) < 256:
        #                 count += 1
        #             else:
        #                 return "Neither"
        #         else:
        #                 count += 1
               
        #     if count == 4:
        #         return "IPV4"
        # if ':' in IP:
        #     count = 0
        #     for num in IP.split(':'):
        #         if len(num) == 0:
        #             return 'Neither'
        #         elif len(num) == 4:
        #             count += 1
        #         elif int(num) == 0:
        #             count += 1
        #         else:
        #             return 'Neither'
        #     if count == 8:
        #         return 'IPV6'

answer = isIP("172.12.45.1")
print answer    
                    
                



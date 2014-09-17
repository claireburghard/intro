def splitName (name):
    print str(name[:name.find(" ")])
    print str(name[(name.find(" ")+1):])

splitName ("Claire Burghard")

def bondify (name):
    return (
        (name[(name.find(" ")+1):]) + ", " +
        name
        )

print bondify ("Claire Burghard")

def replace (s1, s2, s3):
    x = s1.find
    begn = s1[:x]
    end = s1[(x + len(s2)):]
    return begn + s3 + end

print replace ("I hate cs", "hate", "love")

    

        

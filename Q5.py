def Check(S1,S2):
    if (sorted(S1)==sorted(S2)):
       print("The string are anagrams.")
    else:
       print("not anagrams")
S1=input("GIVE:")
S2=input("GIVE:")
Check(S1,S2)

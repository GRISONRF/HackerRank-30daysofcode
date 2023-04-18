# A website domain "discuss.leetcode.com" consists of various subdomains.
#  At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com".
#  When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.


# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.


# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.


# Example 2:


# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

def subdomain_visits(cpdomains):

    subdomains_count = {}   # sub : count,

    for item in cpdomains:
        count, domain = item.split()
        count = int(count)

        subdomain = domain.split('.')
        print(subdomain)

        for i in range(len(subdomain)):

            if '.'.join(subdomain[i:]) in subdomains_count:
                subdomains_count['.'.join(subdomain[i:])] += count
            else:
                subdomains_count['.'.join(subdomain[i:])] = count
    print(subdomains_count)







print(subdomain_visits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))    
#["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]



# create a dict where I'm gonna store the number of times the domain was visited + domain
# iterate through the domains
# split the number and the domain
# split the domains on dots
# iterate through domain
# store in the dictionary: each peace of the domain + number 
# return the information in the dictionary but as a string, using an f{}.


    # dict  = defaultdict
    #for each domains:
        # split in " " to separate domain count and address
        # count = "900" -> make it into a int
        # domain = "google.mail.com"
        # split domain at '.' = gives as a lisr of all domains [google, mail, com]

   
        #iterate len of domain:  //important: 'google' is not a domain. google.com is. mail.com is. google.mail.com is
            # add at counts: joining each fragment of domain to "." and incrementing the next item. and += the count

    
    #iterate the dictionary to add {domain}{count} into a response list as a string


# def subdomain_visits(domains):

#     counts = collections.defaultdict(int)   #domain : count
#     for item in domains:
#         count, domain = item.split()
        
#         count = int(count)
#         sep_domain = domain.split(".")

#         # print(sep_domain)
#         for i in range(len(sep_domain)):
#             counts[".".join(sep_domain[i:])] += count


#     res = []
#     for d, c in counts.items():
#         res.append(f'{c} {d}')
        
#     print(res)
   
# RUNTIME: O(n) -> O(n) (looping through all the domains) * O(1) (the second loop is always gonna be 3 or 2 items in fragments)
# SPACETIME: O(n) -> (The size of the dict we created depends on the size of the domain list)

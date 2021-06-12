from collections import OrderedDict

def merge_the_tools(string, k):
    num_parts = int(len(string)/k)
    for index in range(num_parts):
        substring = string[index*k: index*k+k]
        substring = remove_duplicates(substring)
        print(substring)


def remove_duplicates(string):
    d = OrderedDict.fromkeys(string)
    return ''.join(d.keys())
    
        
        
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

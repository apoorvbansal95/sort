import sys
import os 
import chardet
def sort_word(file_path, n):
    """
    Sort the content of file in lexicographical order.
    """
    with open(file_path, 'r', encoding='utf-8',  errors='ignore') as file:
        lines=file.readlines()
        sorted_line=sorted(set(line.strip() for line in lines))
        # for line in sorted_line[:n]:
        #     print(line)
        i=0
        while n>0:
            if sorted_line[i].isalpha():
                print(sorted_line[i])
                n-=1
                i+=1
            else:
                i+=1
                

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: python sort.py <file_path> <n>")
        sys.exit(1)
    file_path=sys.argv[1]
    n=int(sys.argv[2])

    sort_word(file_path, n)



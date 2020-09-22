# First VM translator handling math and memaccess 
#INPUT = .vm file 
#OUTPUT = .asm file 
#TESTING: using the VM emulator using the supplied XxxVME.tst script
#IMPLEMENTATION: 9 arithmetic / logical commands of the VM language as well as the VM command push constant x. Add comment to output file for each command for help with debugging. 
#ARITH/LOGIC Commands:
#add, sub, neg, eq, gt, lt, and, or, not
#MEM Commands: 
#pop segment i, push segment i    

url_file = 'C:\\Users\\sammy\\Desktop\\nand2tetris\\projects\\07\\MemoryAccess\\BasicTest\\BasicTest.vm'

def open_file(file):
    f = open(file, 'r')
    print(f.read()) 
    return file

open_file(url_file)


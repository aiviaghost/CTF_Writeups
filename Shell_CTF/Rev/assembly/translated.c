#include <stdio.h>

/*
Nice links:
https://stackoverflow.com/questions/20189262/how-an-assembly-language-works
https://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames
https://stackoverflow.com/questions/3879662/hows-return-value-implemented-in-assembly-level
*/

int fun1(int arg1, int arg2) {
    int temp1 = arg2; // [ebp - 4]
    int temp2 = arg1; // [ebp - 8]

    for ( ; temp2 <= 0x227; ) {
        temp1 += 0x7;
        temp2 += 0x70;
    }

    return temp1;
}

int main() {
    int res = fun1(0x74, 0x6f) + fun1(0x62, 0x69);
    printf("SHELL{%#x}", res); // SHELL{0x117}
}

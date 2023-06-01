#include <stdio.h>
#include <string.h>

// One of these must be True (the other False)
#define WIFI 0
#define BT 1

// Input hex string of the scanned wifi or bluetooth packet
// Ensure there is no leading space
char hex_string[] = "47 5E 09 09 1E B8 06 61 93 D0 70 0A 53 16 FA FF 0D 01 F2 19 03 02 10 31 35 39 36 46 33 35 30 34 35 37 37 39 31 31 35 31 35 32 33 00 00 00 52 00 4E 55 4C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 42 04 00 00 00 00 00 00 00 00 01 00 19 00 00 00 00 10 00 00 00 00 00 00 00";

#if WIFI
// binary of FA 0B BC 0D
const char identifier[] = "11111010000010111011110000001101";  // FA 0B BC is ASTM's OUI (organization unique identifier) 
#endif

#if BT
// binary of 16 FA FF 0D 
const char identifier[] = "00010110111110101111111100001101";  // 16 specifies that the next 16 bits are a UUID, FAFF is ASTM's assigned UUID
#endif

void HexToBin(char* hexdec, char* output_buf) {
    /*
     Takes a hex string and writes the 8-digit binary string equivalent of the first 2 hex chars into output_buf

     output_buf MUST have length at least 8.
     */
    for (int i=0; i<2; i++) {  
        switch (hexdec[i]) {
        case '0':
            strcat(output_buf, "0000");
            break;
        case '1':
            strcat(output_buf, "0001");
            break;
        case '2':
            strcat(output_buf, "0010");
            break;
        case '3':
            strcat(output_buf, "0011");
            break;
        case '4':
            strcat(output_buf, "0100");
            break;
        case '5':
            strcat(output_buf, "0101");
            break;
        case '6':
            strcat(output_buf, "0110");
            break;
        case '7':
            strcat(output_buf, "0111");
            break;
        case '8':
            strcat(output_buf, "1000");
            break;
        case '9':
            strcat(output_buf, "1001");
            break;
        case 'A':
        case 'a':
            strcat(output_buf, "1010");
            break;
        case 'B':
        case 'b':
            strcat(output_buf, "1011");
            break;
        case 'C':
        case 'c':
            strcat(output_buf, "1100");
            break;
        case 'D':
        case 'd':
            strcat(output_buf, "1101");
            break;
        case 'E':
        case 'e':
            strcat(output_buf, "1110");
            break;
        case 'F':
        case 'f':
            strcat(output_buf, "1111");
            break;
        default:
            printf("\nInvalid hexadecimal digit %c", hexdec[i]);
        }
    }
}


int main() {
    printf("===========================BEGIN MAIN===========================\n");

    int binary_string_len = 4 * strlen(hex_string) + 1;  // multiply by 8 since each hex char becomes 4 bin chars
    // printf("%d", binary_string_len);
    char binary_string[1149];  // array to hold output binary string

    char* end = hex_string + sizeof(hex_string);  // pointer to first element beyond hex_string
    char* current_char_hex = hex_string;  // pointer to where we are as we loop through hex string 
    char* current_char_bin = binary_string;  // pointer to where we are as we build the binary string 
    while (current_char_hex < end) {  // loop through hex string 3 chars at a time
        printf("%c%c ", current_char_hex[0], current_char_hex[1]);
        
        HexToBin(current_char_hex, current_char_bin);  // get binary of the 2 hex digits

        current_char_bin += 8;
        current_char_hex += 3;  // if hex_string does not contain spaces separating every two hex chars, change the 3 to a 2
    }
        
    printf("\n\n");

    strcat(binary_string, "\0");  // add null terminator for printing
    printf("bin: %s", binary_string+5);


    if (strstr(binary_string, identifier) != NULL) {  // strstr returns pointer to first occurence of identifier in binary_string
        printf("\nIdentifed found. Confirmed ODID packet.\n");
    }
}